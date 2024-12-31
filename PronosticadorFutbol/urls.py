from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('emailmarketing.urls')),
    path('administrator/', include('administrator.urls')),
    path('pages/', include('pages.urls')),
    path('feeder/', include('feeder.urls')),
    path('forecasts/', include('forecasts.urls')),
    path('payment/', include('payment.urls')),
    # paths de Auth. con este path django nos provee de varias urls para manejar autenticacion
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    path('summernote/', include('django_summernote.urls')),
    
]
#if settings.DEBUG:

    # variables MEDIA_URL Y MEDIA_ROOT las tenemos que declarar en el settings del proyecto
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]