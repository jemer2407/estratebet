"""
Django settings for PronosticadorFutbol project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from pathlib import Path
from decouple import config





# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')



# SECURITY WARNING: don't run with debug turned on in production!

#DEBUG = True   # True para desarrollo, comentado para producción
DEBUG = config('DEBUG', cast=bool)  # comentado para desarrollo


ALLOWED_HOSTS = ['127.0.0.1','estratebet.com','www.estratebet.com']
RENDER_EXTERNAL_HOSTNAME = config('RENDER_EXTERNAL_HOSTNAME')   # comentado para desarrollo
if RENDER_EXTERNAL_HOSTNAME:    # comentado para desarrollo
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)  # comentado para desarrollo


# Application definition

INSTALLED_APPS = [
    'registration',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_summernote',
    "django_flatpickr",
    # apps propias
    'administrator',
    'core',
    'emailmarketing',
    'feeder',
    'forecasts',
    'pages',
    'payment',
    'Profiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'payment.middleware.SubscriptionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    
]

ROOT_URLCONF = 'PronosticadorFutbol.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'pages.processors.ctx_dict',
            ],
        },
    },
]


WSGI_APPLICATION = 'PronosticadorFutbol.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

if DEBUG:
    # configuración para la base de datos en desarrollo
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'estratebet',
            'USER': 'postgres',
            'PASSWORD': 'Halamadrid/01',
            'HOST': 'localhost',
            'PORT': '5432'
        }
    }
else:'''
# configuración para la base de datos en producción
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT', cast=int),
    }
}
'''
DATABASES = {
    'default': dj_database_url.config()
}'''




# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'

# This production code might break development mode, so we check whether we're in DEBUG mode
if not DEBUG:
    # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    # Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
    # and renames the files with unique names for each version to support long-term caching
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


'''STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'staticfiles')
]'''


# Media files 
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGOUT_REDIRECT_URL = 'home'
LOGIN_REDIRECT_URL = 'home'
SIGNUP_REDIRECT_URL = 'success_registration'

# Emails

#if DEBUG:   
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('SMTP_HOST')
EMAIL_PORT = config('SMTP_PORT', cast=int)
EMAIL_HOST_USER = config('SMTP_USER')
EMAIL_HOST_PASSWORD = config('SMTP_PASSWORD')
EMAIL_USE_TLS = True



    
#else:
    # Aquí hay que configurar un email real para producción
#    pass

# para produccion estas variable tienen que ir en variables de entorno para que no se muestren en github
STRIPE_PUBLISHABLE_KEY = config('STRIPE_PUBLISHABLE_KEY')
STRIPE_SECRET_KEY = config('STRIPE_SECRET_KEY')
STRIPE_API_VERSION = config('STRIPE_API_VERSION')

if DEBUG:
    DOMAIN = 'http://127.0.0.1:8000/'
else:
    DOMAIN = 'https://estratebet.com/'

SESSION_COOKIE_AGE = 1209600  # 2 semanas en segundos
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_SAVE_EVERY_REQUEST = False


