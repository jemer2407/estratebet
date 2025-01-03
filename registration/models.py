import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.core.validators import MinValueValidator
from emailmarketing.send_email import send_email
from django.utils.crypto import get_random_string
from django.conf import settings

def generate_custom_uuid():
    # Genera un UUID y lo convierte en una cadena hexadecimal
    uuid_obj = uuid.uuid4()
    hex_str = uuid_obj.hex
    # Personaliza la cadena según tus necesidades (e.g., tomar solo los primeros 32 caracteres)
    custom_token = hex_str[:32]
    return custom_token



def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profile/' + filename

# Create your models here.

# Modelo para el perfil de usuario
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(verbose_name='Imagen de perfil', upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(verbose_name='Biografía', null=True, blank=True)
    link = models.URLField(verbose_name='Enlace', max_length=200, null=True, blank=True)
    adult = models.BooleanField(default=True, verbose_name='Mayor de edad')
    created = models.DateTimeField(verbose_name='Fecha creación perfil', auto_now_add=True)
    trial_month = models.DateTimeField(verbose_name='Fecha final de prueba', null=True, blank=True, validators=[MinValueValidator(timezone.now)])
    date_subscription = models.DateTimeField(verbose_name='Fecha suscripción', null=True, blank=True, validators=[MinValueValidator(timezone.now)])
    subscription_month = models.DateTimeField(verbose_name='Fecha final suscripción', null=True, blank=True, validators=[MinValueValidator(timezone.now)])
    is_trial = models.BooleanField(default=False, verbose_name='Periodo de prueba')
    is_subscribed = models.BooleanField(default=False, verbose_name='Suscripción activa')
    is_verified = models.BooleanField(default=False, verbose_name='Correo verificado')
    verification_token = models.CharField(max_length=32, verbose_name='Token de verificación')
    date_verified = models.DateTimeField(verbose_name='Fecha verificación', null=True, blank=True)
    verification_update_email_token = models.CharField(max_length=32, verbose_name='Token de verificación de actualización de correo electrónico', null=True, blank=True)
    date_verified_update_email = models.DateTimeField(verbose_name='Fecha verificación de actualización de correo electrónico', null=True, blank=True)
    is_verified_token_update_email = models.BooleanField(verbose_name='Correo modificado verificado', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['user__username']
    


@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
       Profile.objects.get_or_create(user=instance)
       # enviar correo electronico de nuevo usuario al administrador
       email = 'estratebet@gmail.com'
       subject = 'Nuevo usuario registrado'
       message = '''Se ha registrado un nuevo usuario: 
       nombre de susuario: {} 
       correo electrónico: {}'''.format(instance.username, instance.email)
       send_email(email, subject, message)
       
       


@receiver(post_save, sender=Profile)
def update_profile_status(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.get(user=instance.user)
        profile.verification_token = get_random_string(length=32)
        profile.save()
        
        # enviar correo electrónico de verificación
        email = instance.user.email
        subject = 'Verifica tu correo electrónico'
        message = '''
        Hola, {}! Bienvenido a Estratebet.
        Por favor, verifica tu correo electrónico haciendo clic en el siguiente enlace: {}accounts/verify/{} para tener acceso a los 7 días de prueba.
        Éstos 7 días de prueba se activarán automáticamente al verificar tu correo electrónico.
        '''.format(instance.user.username,settings.DOMAIN, profile.verification_token)
        
        send_email(email, subject, message)
        # enviar correo electrónico de bienvenida
        
            


@receiver(post_save, sender=Profile)
def check_trial_expiration(sender, instance, **kwargs):
    if instance.trial_month and instance.trial_month <= timezone.now():
        instance.is_trial = False
        instance.save()



@receiver(post_save, sender=Profile)
def check_subscription_expiration(sender, instance, **kwargs):
    # Esta señal verifica si la suscripción ha expirado
    if instance.subscription_month and instance.subscription_month <= timezone.now():
        instance.is_subscribed = False
        instance.save()