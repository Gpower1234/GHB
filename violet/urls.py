from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from GHB import views
from GHB.views import SignUpView, ActivateView, CheckEmailView, SuccessView
from django.contrib.auth import views as auth_views

app_name = 'GHB'


urlpatterns = [
    path('GHB/', admin.site.urls),
    path('', include('HairStyles.urls')),
    path('', include('appointments.urls')),
    path('', views.home_view, name='index'),
    path('accounts/login/', auth_views.LoginView.as_view()),
    path('about_us/', views.about_us_view, name='about_us'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('profile/', views.profile_view, name='profile'),
    path('update-profile/', views.update_profile, name='update-profile'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('activate/<uidb64>/<token>/', ActivateView.as_view(), name='activate'),
    path('check-email/', CheckEmailView.as_view(), name='check_email'),
    path('success/', SuccessView.as_view(), name='success'),
    path('', include('django.contrib.auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),	
]



urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)