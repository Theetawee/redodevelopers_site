from pathlib import Path
import os
from django.contrib.messages import constants as messages

"""
from django.core.management.utils import get_random_secret_key

print( get_random_secret_key())
"""


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'main',
    "debug_toolbar",
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'accounts'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'base.urls'
SITE_ID=1
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'base.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


if DEBUG == True:
    
    STATIC_URL = 'static/'
    MEDIA_URL='media/'

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    }
    
    STATICFILES_DIRS=[
        os.path.join(BASE_DIR,'static'),
        os.path.join(BASE_DIR,'media')
    ]
    STATIC_ROOT=os.path.join(BASE_DIR,'static_cdn')
    
    MEDIA_ROOT=os.path.join(BASE_DIR,'media_cdn')

    INTERNAL_IPS = [
        "127.0.0.1",
    ]
    
    ACCOUNT_DEFAULT_HTTP_PROTOCOL ='http'
else:
    #ALLOWED_HOSTS = [''] update allowed hosts for production
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    }
    

    # CLOUDINARY_STORAGE={
    #     'CLOUD_NAME': 'dnb8rethz',
    #     'API_KEY': os.environ.get('API_KEY'),
    #     'API_SECRET': os.environ.get('API_SECRET')
    # }
    
    # DEFAULT_FILE_STORAGE='cloudinary_storage.storage.MediaCloudinaryStorage'


    ACCOUNT_DEFAULT_HTTP_PROTOCOL ='https'
    STATIC_URL='https://theetawee.github.io/company_staticfiles/'
    
    
    


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('EMAIL')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')
EMAIL_USE_TLS = True

MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': os.environ.get('GOOGLE_ID'),
            'secret': os.environ.get('GOOGLE_SECRET'),
            'key': ''
        }
    }
}


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True,
    }
}

ACCOUNT_MAX_EMAIL_ADDRESSES= 2
ACCOUNT_EMAIL_VERIFICATION ='mandatory'  #none mandatory #optional
ACCOUNT_EMAIL_REQUIRED =True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS =1
ACCOUNT_LOGOUT_REDIRECT_URL ='account_login'
LOGIN_REDIRECT_URL='home'
ACCOUNT_AUTHENTICATION_METHOD='username_email'
ACCOUNT_USERNAME_MIN_LENGTH =4
ACCOUNT_SIGNUP_REDIRECT_URL='home'
ACCOUNT_EMAIL_SUBJECT_PREFIX ='Redo Developers.'
