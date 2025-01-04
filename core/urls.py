from django.urls import path
from .views import HomeView, AboutView, contact, RobotsView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('about/', AboutView.as_view(), name="about"),
    path('contact/', contact, name="contact"),
    path('robots.txt',RobotsView.as_view(template_name="core/robots.txt", content_type="text/plain"))
]