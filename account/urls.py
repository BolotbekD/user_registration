from django.urls import path, include
from account.views import Register
# from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register', Register.as_view(), name='register'),
    # path('password-reset', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
]