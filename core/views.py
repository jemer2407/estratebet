
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.urls import reverse
from django.conf import settings
from registration.models import Profile
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.utils import timezone
from datetime import datetime
from forecasts.models import Match, Contry, League, Strategy
from forecasts.views import get_next_matches_league
from emailmarketing.send_email import send_email

class HomeView(TemplateView):
    model = Match
    template_name = "core/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Pronosticador de Futbol'
        leagues = League.objects.all()
        context['leagues'] = leagues
        # partidos de hoy
        context['match_today'] = Match.objects.filter(date=timezone.now())
        context['hoy'] = timezone.now().strftime('%d/%m/%Y')
        context['manana'] = (timezone.now() + timezone.timedelta(days=1)).strftime('%d/%m/%Y')
        context['pasado'] = (timezone.now() + timezone.timedelta(days=2)).strftime('%d/%m/%Y')
        
        
        
        # proximos partidos de todas las ligas
        '''next_unplayed_matches = []
        for league in leagues:
            unplayed_matches = Match.objects.filter(league=league.id,gol_home_ht=None)  # aqui obtengo los que no se han jugado aun
            matches = get_next_matches_league(unplayed_matches)
            next_unplayed_matches.append(matches)
        
        context['next_matches_leagues_list'] = next_unplayed_matches'''
        
        if self.request.user.is_authenticated:
            context['user'] = self.request.user
            profile = Profile.objects.get(user=self.request.user)
            context['profile'] = profile
            strategies = Strategy.objects.filter(user=profile.user)
            print(strategies)
            if not strategies:
                context['strategies'] = False
            
        
        return context

class AboutView(TemplateView):
    template_name = "core/about.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'title': 'Sobre nosotros'
        })
    
def contact(request):
    title = 'Contacto'
   
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            subject = 'Mensaje de contacto de Estratebet'

            # Enviamos el correo y redireccionamos
            message = f"Nombre: {name}\nCorreo: {email}\n\n{content}"
            email_receptor = settings.EMAIL_HOST_USER
            if send_email(email_receptor, subject, message):
                return redirect(reverse('contact') + "?ok")
            else:
                return redirect(reverse('contact') + "?fail")

            
    return render(request, 'core/contact.html', {
        'title': title,
        'form': contact_form
    })

# vista para la pagina robots.txt
class RobotsView(TemplateView):
    template_name = "core/robots.txt"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'title': 'robots.txt'
        })