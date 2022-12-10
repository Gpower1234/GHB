from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.core.mail import send_mail
from .forms import RegisterForm, ContactForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, TemplateView, RedirectView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from .models import Gallery
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from .token import token_generator

user_model = get_user_model()
# Create your views here.

def home_view(request):
    images = Gallery.objects.all()
    return render(request, 'home.html', {'images': images})


def about_us_view(request):
    return render(request, 'about_us.html')

@login_required
def profile_view(request):
    user_FName = request.user.first_name
    user_LName = request.user.last_name
    x = user_FName[0]
    y = user_LName[0]
    return render(request, 'profile.html', {'x': x, 'y': y})

def contacts_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']
            html = render_to_string('email_html_strings/contact-form.html', {
                'name': name,
                'subject': subject,
                'email': email,
                'content': content
            })

            send_mail('Mail from GHB customer', html_message=html)
            messages.success(request, f'Hi {name}, your request has been submitted successfully, we will attend to it as soon as possible. ')
            return redirect('index')

    else:
        form = ContactForm()

    return render(request, 'contacts.html', {'form': form})

class SignUpView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('check_email')

    def form_valid(self, form):
        to_return = super().form_valid(form)

        user = form.save()
        user.is_active = False
        user.save()

        form.send_activation_email(self.request, user)

        return to_return

class ActivateView(RedirectView):
    url = reverse_lazy('success')

    # custom get method
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = user_model.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, user_model.DoesNotExist):
            user = None

        if user is not None and token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return super().get(request, uidb64, token)

        else:
            return render(request, 'activate_account_invalid.html')

class CheckEmailView(TemplateView):
    template_name = 'check_email.html'

class SuccessView(TemplateView):
    template_name = 'successful.html'


@login_required
def update_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your profile has been updated successfully!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
    context = {
        'u_form': u_form,
    }

    return render(request, 'update_profile.html', context)





