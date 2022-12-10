from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from HairStyles.models import HairType
from .models import Appointment
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.template import context


# Create your views here.


@login_required
def AppointmentView(request):
    form = AppointmentForm(request.POST or request.GET)
    hair_types = HairType.objects.all()
    user = request.user
    if request.POST:
        form = AppointmentForm(request.POST)
        if form.is_valid():      
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            booked_item = form.cleaned_data['booked_item']
            html = render_to_string('email_html_strings/booked-notification.html', {
                'name': name,
                'phone_number': phone_number,
                'booked_item': booked_item
            })

            send_mail('Appointment Application', html_message=html)
            form.save()
            messages.success(request, f'Hi {user.first_name}, thanks for booking an appointment, a date will be scheduled for your appointment and sent via Mail from the Goodness Hair Braid team. ')
            return redirect('appointment-history')
    return render(request, 'appointment_form.html', {'form': form, 'hair_types': hair_types})


@login_required
def AppointmentHistory(request):
    user = request.user
    appointments = Appointment.objects.filter(user=user).order_by('applied_on')
    return render(request, 'appointment_history.html', {'appointments': appointments})



class ManageAppointments(ListView):
    model = Appointment
    template_name = 'manage_appointments.html'
    context_object_name = 'appointments'
    login_required = True
    #paginate_by = 6

    def post(self, request):
        date = request.POST.get('date')
        appointment_id = request.POST.get('appointment-id')
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.date_scheduled = date
        name = appointment.name
        item = appointment.booked_item
        appointment.save()

        html = render_to_string('appointments-email.html', {
                'name': name,
                'date': date,
                'item': item
                
            })

        send_mail('Your Appointment has been Accepted and Scheduled', html_message=html)
        messages.success(request, f'Date scheduled successfully for {appointment.name}')
        return HttpResponseRedirect(request.path)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        appointments = Appointment.objects.all().order_by('-applied_on')
        context.update({
            'appointments': appointments,
            'title':'Manage-Appointments'
        })
        return context
