from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import EmailMessage
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.http import Http404, JsonResponse
import time
from .models import Subscriber
from .forms import SuscriberForm, EmailMarketingForm
from .send_email import send_email
from django.utils.html import strip_tags

# Create your views here.

# vista pública para suscribirse a la newsletter
class SubscriberCreateView(SuccessMessageMixin, CreateView):
    model = Subscriber
    form_class = SuscriberForm
    template_name = 'emailmarketing/subscriber_form.html'
    success_message = "Gracias por suscribirte a nuestra newsletter"
    success_url = reverse_lazy('home')

def validate_email(email):
    # validamos el formato del email
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False

def subscriberView(request):
    json_response = {'created': False}
    
    email = request.GET.get('email')

    if validate_email(email):
        if not Subscriber.objects.filter(email=email):
            suscriber = Subscriber(email=email)
            suscriber.save()
            json_response['created'] = True
            json_response['message'] = 'Gracias por subscribirte a la newsletter'
            # enviar email de bienvenida
            subject = 'Bienvenido a la newsletter de Estratebet'
            message = 'Gracias por suscribirte a nuestra newsletter'
            send_email(email, subject, message)
        else:
            json_response['message'] = 'El email introducido ya existe para otro usuario'
    
    else:
        json_response['message'] = 'El email introducido no es válido'
    return JsonResponse(json_response)
    

# vista privada para listar los suscritores de la newsletter
@method_decorator(staff_member_required, name='dispatch')
class SubscriberListView(ListView):
    model = Subscriber
    template_name = 'emailmarketing/subscribers_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de suscriptores'
        return context

# vista para crear suscriptores desde login
# vista privada para suscribirse a la newsletter
@method_decorator(staff_member_required, name='dispatch')
class LoginSubscriberCreateView(CreateView):
    model = Subscriber
    form_class = SuscriberForm
    template_name = 'emailmarketing/subscriber_maintenance_form.html'
    success_url = reverse_lazy('subscribers-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nuevo Suscriptor'
        return context


# vista para editar un suscriptor
@method_decorator(staff_member_required, name='dispatch')
class SubscriberUpdateView(UpdateView):
    model = Subscriber
    form_class = SuscriberForm
    template_name = 'emailmarketing/subscriber_form.html'
    success_url = reverse_lazy('subscribers-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Suscriptor'
        return context

# vista para eliminar un suscriptor
@method_decorator(staff_member_required, name='dispatch')
class SubscriberDeleteView(DeleteView):
    model = Subscriber
    template_name = 'emailmarketing/subscriber_confirm_delete.html'
    success_url = reverse_lazy('subscribers-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Suscriptor'
        return context

# vista para la campaña de email marketing
# ver https://docs.djangoproject.com/en/5.1/topics/auth/default/
@staff_member_required
def emailMarketing(request):

    title = 'Campaña Email Marketing'
    contact_form = EmailMarketingForm()

    if request.method == 'POST':
        contact_form = EmailMarketingForm(data=request.POST)
        if contact_form.is_valid():
            subject = request.POST.get('subject', '')
            message = request.POST.get('message', '')
            
            # obtenemos los emails de todos los suscriptores

            subscribers = Subscriber.objects.all()
            # Convert HTML message to plain text
            message = strip_tags(message)
            
            # Enviamos el correo y redireccionamos
            message = f"{message}\n\nUn saludo\n\nEl equipo de Estratebet"
            for subscriber in subscribers:
                
                email_receptor = subscriber.email
                
                if send_email(email_receptor, subject, message):
                    continue
                else:
                    return redirect(reverse('subscribers-list') + "?fail")
                time.sleep(8)
                
            return redirect(reverse('subscribers-list') + "?ok")
        
    return render(request, 'emailmarketing/send_email_everyone.html', {
        'title': title,
        'form': contact_form
    })
    


