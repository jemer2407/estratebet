from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
import stripe
from decimal import Decimal
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from emailmarketing.send_email import send_email
from registration.models import Profile
from forecasts.decorators import subscription_required, verified_required


# Create your views here.


# This is your test secret API key.
stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION

@login_required
@verified_required
def checkout_session(request):
    # Obtener la información del usuario y el plan de suscripción
    user = request.user  # Suponiendo que el usuario está autenticado
    
    try:
        # Crear una sesión de suscripción
        session = stripe.checkout.Session.create(
            payment_method_types=['card', 'paypal','revolut_pay'],
            customer_email=user.email,
            line_items=[
                {
                    'price_data': {
                        'currency': 'eur',
                        'unit_amount': 1000,
                        'product_data': {
                            'name': 'Basico',
                            'description': 'Suscribirse a Estratebet por un periodo de 30 días. Si te suscribes y aun tienes un periodo de prueba, éste lo perderás.'
                        }
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',            
            success_url=settings.DOMAIN + 'payment/success/',
            cancel_url=settings.DOMAIN + 'payment/cancel/'
        )
    except stripe.error.StripeError as e:
        # Manejar errores
        return render(request, 'payment/error.html', {'error': e.user_message})

    # Redirigir al usuario a la página de pago de Stripe
    return redirect(session.url, code=303)

@login_required
@verified_required
def success_payment(request):
    profile = Profile.objects.get(user=request.user)
    email = profile.user.email
    profile.date_subscription = timezone.now()
    profile.subscription_month = timezone.now() + timezone.timedelta(days=30)
    profile.is_subscribed = True
    if profile.is_trial == True:
        profile.is_trial = False
        profile.trial_month = None
        
    profile.save()

    # enviar correo electrónico de bienvenida
    
    subject = 'Suscripción realizada con éxito'
    message = '''
    Hola, {}! Te has suscrito al plan BÁSICO de Estratebet con éxito.
    Ahora puedes disfrutar de todas las funcionalidades de nuestra plataforma.
    Si tienes alguna duda o problema, contacta con nosotros a través de nuestro correo electrónico.
    

    Atentamente, el equipo de Estratebet.
    soporte@estratebet.com
    
    '''.format(profile.user.username)
    send_email(email, subject, message)

    return render(request,'payment/success.html',{
        'title': 'Pago realizado con éxito'
    })

@login_required
@verified_required
def cancel_payment(request):
    return render(request,'payment/cancel.html',{
        'title': 'Pago cancelado'
    })

@login_required
@verified_required
def error_payment(request):
    return render(request,'error.html',{
        'title': 'Error en el Pago'
    })

@login_required
@verified_required
def suscriptions(request):
    title = 'Suscripciones'
    return render(request,'payment/suscriptions.html', {
        'title': title
    })