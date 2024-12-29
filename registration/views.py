#from django.contrib.auth.forms import UserCreationForm  # formulario generico de django para el registro de usuarios
import uuid
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.generic import CreateView # Clase de la que vamos a heredar para crear una vista de Creación de un registro
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout
from django.views.generic.edit import UpdateView
from django.contrib.auth.views import PasswordResetView
import stripe

from django import forms
from emailmarketing.send_email import send_email
from registration.models import Profile
from .forms import EmailForm, ProfileForm, UserCreationFormWithEmail



# Create your views here.
# Vista basada en clase para el registro de usuarios
class SignUpView(CreateView):
    #form_class = UserCreationForm   # Esta clase es el formulario que nos proporciona django por defecto para el registro de usuarios
    form_class = UserCreationFormWithEmail
    success_url = reverse_lazy('success_registration') # redirigir a la pagina de login despues de registrarse
    template_name = 'registration/signup.html'  # template para el registro de usuario

    def get_success_url(self):
        #return reverse_lazy('login') + '?register'
        return reverse_lazy('success_registration')
    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        # Modificar en tiempo real el formulario
        form.fields['username'].widget = forms.TextInput(
            attrs={
            'class':'form-control mb-2', 
            'placeholder':'Nombre de usuario'
            })
        form.fields['email'].widget = forms.EmailInput(
            attrs={
                'class':'form-control mb-2', 
                'placeholder':'Email'
                })
        form.fields['password1'].widget = forms.PasswordInput(
            attrs={
                'class':'form-control mb-2', 
                'placeholder':'Contraseña'
                })
        form.fields['password2'].widget = forms.PasswordInput(
            attrs={
            'class':'form-control mb-2', 
            'placeholder':'Repita contraseña'
            })
        return form
    
@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        # recuperar el objeto que se va a editar
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['user'] = self.request.user
            profile = Profile.objects.get(user=self.request.user)
            if not profile.is_trial:
                context['trial_month'] = 'No tienes una prueba activa'
            else:
                context['trial_month'] = profile.trial_month
                
            if profile.is_subscribed:
                context['date_subscription'] = profile.date_subscription
                context['subscription_month'] = profile.subscription_month
            else:
                context['date_subscription'] = 'No tienes una subscripción activa'
                context['subscription_month'] = 'No tienes una subscripción activa'
        return context

@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'

    def get_object(self):
        # recuperar el objeto que se va a editar
       
        return self.request.user
    
    def get_form(self, form_class = None):
        form = super(EmailUpdate, self).get_form()
        # Modificar en tiempo real el formulario
        form.fields['email'].widget = forms.EmailInput(
            attrs={
            'class':'form-control mb-2', 
            'placeholder':'Email'
            })
        return form



# vista para comprobar si el usuario ha verificado su correo
def verify(request, token):
    try:
        profile = Profile.objects.get(verification_token=token)
        profile.is_verified = True
        profile.date_verified = timezone.now()
        # Calcular la fecha de finalización de la prueba
        profile.is_trial = True
        profile.trial_month = timezone.now() + timezone.timedelta(days=7)        
        profile.save()

        # enviar correo electrónico de bienvenida
        email = profile.user.email
        subject = 'Bienvenido a Estratebet'
        message = '''
        Hola, {}! Bienvenido a Estratebet.
        Tu cuenta ha sido verificada con éxito. Dispones de un periodo de prueba de 7 días.
        Si quieres disfrutar de todas las funcionalidades de Estratebet, puedes suscribirte en cualquier momento.

        Atentamente, el equipo de Estratebet.
        
        '''.format(profile.user.username)
        send_email(email, subject, message)
        


        return redirect('token_verification')
    except Profile.DoesNotExist:
        return redirect('login')
    except RecursionError:
        return redirect('token_error')

# vista para mostrar mensaje de verificación de correo
def token_verificated(request):
    
    return render(request, 'registration/token_verificated.html')

# vista para mostrar mensaje de registro exitoso
def success_registration(request):
    return render(request, 'registration/success_registration.html')

# vista para RecursionError
def token_error(request):
    return render(request, 'registration/error_token.html')



