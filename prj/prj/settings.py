from pathlib import Path
from pathlib import os

from dotenv import load_dotenv, find_dotenv

find_dotenv('.env')
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-zf&66f3pa76f#9v$_-yqbuhrk$k^30!wahm$^-q)2$gljrleez'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

# AUTHENTICATION_BACKENDS = [
#
#     'django.contrib.auth.backends.ModelBackend',
#
#     'allauth.account.auth_backends.AuthenticationBackend',
# ]

INSTALLED_APPS = [
    'modeltranslation',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.flatpages',
    'django.contrib.sites',
    'newsapp.apps.NewsappConfig',
    'django_filters',
    'sign',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.google',

    'django_apscheduler',

]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.locale.LocaleMiddleware',
    
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',

    'newsapp.middlewares.TimezoneMiddleware',
]

ROOT_URLCONF = 'prj.urls'

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [(BASE_DIR / 'templates')],
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

WSGI_APPLICATION = 'prj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'PASSWORD': '12345',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     },
# }


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ru'

LANGUAGES = [
# список кортежей
    ('en-us', 'English'),
    ('ru', 'Русский'),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# STATICFILES_DIRS = [
#     BASE_DIR / "static"
# ]
### было так 14-го
#LOGIN_URL = 'sign/login/'
#LOGIN_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/'
###

LOGIN_URL = '/accounts/login/'


ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

ACCOUNT_FORMS = {'signup': 'sign.models.BasicSignupForm'}


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

##Дописвли от Кати
SITE_URL = 'http://127.0.0.1:8000'
##
####Дописали от меня
EMAIL_HOST = 'smtp.yandex.ru'  # адрес сервера Яндекс-почты для всех один и тот же
EMAIL_PORT = 465  # порт smtp сервера тоже одинаковый
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')  # ваше имя пользователя, всё то что идёт до собаки
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_SSL = True  # Яндекс использует ssl, почитайте в доп., но включать его здесь обязательно
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')  # здесь указываем уже свою ПОЛНУЮ почту, с которой будут отправляться письма

STATIC_URL = 'static/'
####


# формат даты, которую будет воспринимать шудулер
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
# если задача не выполняется за 25 секунд, то она автоматически снимается,
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

#
# LOGGING = {
#     'version' : 1,
#     'disable_existing_logger': False, # внутренний дебагер джанго
#
#     'loggers': {
#         'django': {
#             'handlers': ['debug', 'warning', 'error_critical', 'general'],
#             'level': 'DEBUG',
#         },
#
#         'django.request': {
#             'handlers': ['error_file', 'mail_admins'],
#             'level': 'INFO',
#         },
#
#         'django.server': {
#             'handlers': ['error_file', 'mail_admins'],
#             'level': 'INFO',
#         },
#         'django.template': {
#             'handlers': ['error_file'],
#             'level': 'INFO',
#         },
#         'django.db.backends': {
#             'handlers': ['error_file'],
#             'level': 'INFO',
#         },
#
#         'django.security': {
#             'handlers': ['security'],
#             'level': 'INFO',
#         },
#
#
#     },
#     'handlers': {
#         'debug': {
#             'level': 'DEBUG',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'formatter_debug',
#         },
#
#         'warning': {
#             'level': 'WARNING',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'formatter_warn_mail',
#         },
#
#         'error_critical': {
#             'level': 'ERROR',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'formatter_error_critical',
#         },
#
#         'general': {
#             'level': 'INFO',
#             'filters': ['require_debug_false'],
#             'class': 'logging.FileHandler',
#             'filename': 'general.log',
#             'formatter': 'formatter_general',
#         },
#
#         'error_file': {
#             'level': 'ERROR',
#             'class': 'logging.FileHandler',
#             'filename': 'errors.log',
#             'formatter': 'formatter_error_file',
#
#         },
#
#         'security': {
#             'level': 'INFO',
#             'class': 'logging.FileHandler',
#             'filename': 'security.log',
#             'formatter': 'formatter_security',
#
#         },
#
#         'mail_admins': {
#             'level': 'ERROR',
#             'filters': ['require_debug_false'],
#             'class': 'django.utils.log.AdminEmailHandler',
#             'formatter': 'formatter_warn_mail',
#
#
#         },
#     },
#
#
#     'formatters': {
#
#         'formatter_debug': {
#             'format': '{asctime} {levelname} {message} ',
#             'datetime': '%Y.%m.%d. %H:%M:%S',
#             'style': '{',
#         },
#
#         'formatter_warn_mail': {
#             'format': '{asctime} {levelname} {message} {pathname}',
#             'datetime': '%Y.%m.%d. %H:%M:%S',
#             'style': '{',
#         },
#
#         'formatter_error_critical': {
#             'format': '{asctime} {levelname} {message} {exc_info}',
#             'datetime': '%Y.%m.%d. %H:%M:%S',
#             'style': '{',
#         },
#
#         'formatter_general': {
#             'format': '{asctime} {levelname} {module} {message} ',
#             'datetime': '%Y.%m.%d. %H:%M:%S',
#             'style': '{',
#         },
#
#         'formatter_error_file': {
#             'format': '{asctime} {levelname} {message} {pathname} {exc_info}',
#             'datetime': '%Y.%m.%d. %H:%M:%S',
#             'style': '{',
#         },
#
#         'formatter_security': {
#             'format': '{asctime} {levelname} {module} {message}',
#             'datetime': '%Y.%m.%d. %H:%M:%S',
#             'style': '{',
#         },
#
#     },
#     'filters':{
#         'require_debug_false': { # - имя фильтра
#             '()': 'django.utils.log.RequireDebugFalse',
#         },
#
#         'require_debug_true': {  # - имя фильтра
#             '()': 'django.utils.log.RequireDebugTrue',
#
#         },
#
#     },
# }
#
#


