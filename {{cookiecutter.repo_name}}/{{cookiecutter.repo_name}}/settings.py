import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3no72nq3e5p82_^ge=)b(=p85n@4(l8z-1*0yguryvvra_e_z('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ["*"] # risky business, might want to change this


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.accounts',
    'apps.core',
    'apps.static',
    
    'pipeline' ,
    'rest_framework',
	'rest_framework.authtoken',  
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = '{{ cookiecutter.project_name }}.urls'

WSGI_APPLICATION = '{{ cookiecutter.project_name }}.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = (os.path.join(BASE_DIR,'templates'),)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
# static assets
STATIC_ROOT = os.path.join(BASE_DIR, './staticfiles')
STATICFILES_DIRS = ( os.path.join(BASE_DIR, '{{cookiecutter.project_name}}', 'static'), )
STATICFILES_STORAGE = 'apps.core.storage.GzipManifestPipelineStorage'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

# pipeline & whitenoise
WHITENOISE_ROOT = os.path.join(BASE_DIR, '{{cookiecutter.project_name}}', 'static_served_at_root')
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.uglifyjs.UglifyJSCompressor'
PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yuglify.YuglifyCompressor'
PIPELINE_DISABLE_WRAPPER = True


AUTH_USER_MODEL = 'accounts.User'

# configs
from .pipeline_configs import *

try:
    from local_settings import *
except Exception:
    pass

# default db settings
DATABASES={}
DATABASES['default'] =  dj_database_url.config()

