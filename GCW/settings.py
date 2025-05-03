import os
from django.core.management.utils import get_random_secret_key

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Эта настройка отключена в шаблоне, чтобы все проекты обязательно указывали свой индивидуальный SECRET_KEY.
# Генерация делается в консоли Python при помощи команд:

# Далее полученное значение подставляется в соответствующую переменную

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_random_secret_key()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['goose-cycle.ru', 'www.goose-cycle.ru']

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '487307331145-ck95tdae6qiu1lqemj3r8qkeed22mf4j.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

LOGIN_URL = '/auth/login/google-oauth2/'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
SOCIAL_AUTH_URL_NAMESPACE = 'social'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    # "main.apps.MainConfig",
    'rest_framework',
    'training',
    'import_export',
    'social_django',

]

DEFAULT_AUTO_FIELD='django.db.models.AutoField'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'GCW.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            "main/templates",
            "training/templates",
        ],
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

WSGI_APPLICATION = 'GCW.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'u3120090_default',
        'USER': 'u3120090_default',
        'PASSWORD': 'xaMMUtn9Q4MGf57d',
        'HOST': 'localhost',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'ru'
# LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = 'static/'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]

MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# AUTH_USER_MODEL = 'main.User'  # Если вы хотите

# Проверка тех, кто ленится указать корректный SECRET_KEY
if SECRET_KEY == 'Insert secret key here and uncomment this variable':
    raise RuntimeError('Сначала укажите SECRET_KEY. Подробности - в settings.py')


#DEFAULT_AUTO_FIELD='django.db.models.AutoField'

FIXTURES_DIRS = [
    '/main/database'
]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },

    "handlers": {
        "debug_file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "logs/debug.log",
            "formatter": "simple",
        },
        "info_file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "logs/info.log",
            "formatter": "simple",
        },
        "warning_file": {
            "level": "WARNING",
            "class": "logging.FileHandler",
            "filename": "logs/warning.log",
            "formatter": "verbose",
        },
        "error_file": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": "logs/error.log",
            "formatter": "verbose",
        },
        "critical_file": {
            "level": "CRITICAL",
            "class": "logging.FileHandler",
            "filename": "logs/critical.log",
            "formatter": "verbose",
        },
    },

    "loggers": {
        "": {
            "handlers": ["debug_file", "info_file", "warning_file", "error_file", "critical_file", ],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}
