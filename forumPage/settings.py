"""
Django settings for forumPage project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from django.contrib.messages import constants as messages
import os
from pathlib import Path
from decouple import config
import django_heroku
import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
ALLOWED_HOSTS = ["desponia-page.herokuapp.com", "127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    "accounts",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "pages",
    "posts",
    "userposts",
    'tinymce',
    "django.forms",
    'crispy_forms',
    'django_cleanup.apps.CleanupConfig',
    "postdetail",
    "django.contrib.humanize",
    'rest_framework',

]
FRAOLA_EDITOR_THIRD_PARTY = ('image_aviary', 'spell_checker')


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'forumPage.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'forumPage.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "desponia_db",
        'USER': 'postgres',
        'PASSWORD': 'Vahandaag3196.',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static")

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
# MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media")
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}


LOGIN_URL = "login"

TINYMCE_DEFAULT_CONFIG = {
    "theme": "silver",
    "height": 500,
    "plugins": 'image',
    "menubar": False,
    "plugins": "advlist,autolink,lists,link,styleselect,image,charmap,print,preview,anchor,"
    "searchreplace,visualblocks,code,fontselect,fullscreen,insertdatetime,media,table,paste,"
    "code,help,wordcount",
    "toolbar": "styleselect fontselect| "
    "bold italic backcolor | alignleft aligncenter "
    " alignjustify | bullist numlist  | "
    "removeformat image link media | preview ",
    
}

# EMAIL CONFIG

EMAIL_HOST = 'smtpout.secureserver.net'
EMAIL_FROM_USER = "no-reply@desponia.com"
EMAIL_HOST_USER = "no-reply@desponia.com"
EMAIL_HOST_PASSWORD = "Vahandaag3196."
EMAIL_USE_SSL = True
EMAIL_USE_TLS = False
EMAIL_PORT = 465
DEFAULT_FROM_EMAIL = 'no-reply@desponia.com'

django_heroku.settings(locals())
