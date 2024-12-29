from django.urls import path
from . import views



urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/', views.ProfileUpdate.as_view(), name='profile'),
    path('profile/email/', views.EmailUpdate.as_view(), name='profile_email'),
    path('verify/<token>/', views.verify, name='verify'),
    path('token_verification/', views.token_verificated, name='token_verification'),
    path('success/', views.success_registration, name='success_registration'),
    path('token_error/', views.token_error, name='token_error')
]

