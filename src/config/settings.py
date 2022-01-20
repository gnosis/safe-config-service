"""
Django settings for safe_client_config_service project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from distutils.util import strtobool
from pathlib import Path

import django_stubs_ext

django_stubs_ext.monkeypatch()

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", None)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(strtobool(os.getenv("DEBUG", "false")))

# https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-ALLOWED_HOSTS
allowed_hosts = os.getenv("DJANGO_ALLOWED_HOSTS", ".localhost,127.0.0.1,[::1]")
ALLOWED_HOSTS = [allowed_host.strip() for allowed_host in allowed_hosts.split(",")]

# Application definition

REST_FRAMEWORK = {
    # https://www.django-rest-framework.org/api-guide/renderers/
    "DEFAULT_RENDERER_CLASSES": [
        "djangorestframework_camel_case.render.CamelCaseJSONRenderer",
    ],
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.NamespaceVersioning",
}

INSTALLED_APPS = [
    "corsheaders",
    "about.apps.AboutAppConfig",
    "chains.apps.AppsConfig",
    "safe_apps.apps.AppsConfig",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "drf_yasg",
    "django_otp",
    "django_otp.plugins.otp_totp",
    "django_otp.plugins.otp_static",
]

MIDDLEWARE = [
    "config.middleware.LoggingMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django_otp.middleware.OTPMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

DJANGO_OTP_ADMIN = strtobool(os.getenv("DJANGO_OTP_ADMIN", "true"))
if DJANGO_OTP_ADMIN:
    # Use OTP admin
    INSTALLED_APPS.append("config.admin.OTPAdminConfig")
else:
    # Use Default admin
    INSTALLED_APPS.append("django.contrib.admin")

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    },
    "safe-apps": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    },
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "short": {"format": "%(asctime)s %(message)s"},
        "verbose": {
            "format": "%(asctime)s [%(levelname)s] [%(processName)s] %(message)s"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "console_short": {
            "class": "logging.StreamHandler",
            "formatter": "short",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": os.getenv("ROOT_LOG_LEVEL", "INFO"),
    },
    "loggers": {
        "LoggingMiddleware": {
            "handlers": ["console_short"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

ROOT_URLCONF = "config.urls"
FORCE_SCRIPT_NAME = os.getenv("FORCE_SCRIPT_NAME", default=None)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_NAME", "postgres"),
        "USER": os.getenv("POSTGRES_USER", "postgres"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", "postgres"),
        "HOST": os.getenv("POSTGRES_HOST", "db"),
        "PORT": os.getenv("POSTGRES_PORT", "5432"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = "staticfiles"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SWAGGER_SETTINGS = {
    "DEFAULT_INFO": "config.swagger_info.SAFE_CONFIG_SERVICE_SWAGGER_INFO"
}

CORS_ALLOW_ALL_ORIGINS = True
CORS_URLS_REGEX = r"^/api/.*$"

CGW_URL = os.environ.get("CGW_URL")
CGW_FLUSH_TOKEN = os.environ.get("CGW_FLUSH_TOKEN")

# By default, Django stores files locally, using the MEDIA_ROOT and MEDIA_URL settings.
# (using the default the default FileSystemStorage)
# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = f"{BASE_DIR}/media/"
# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = "/media/"

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
AWS_S3_CUSTOM_DOMAIN = os.getenv("AWS_S3_CUSTOM_DOMAIN")
# By default files with the same name will overwrite each other. Set this to False to have extra characters appended.
AWS_S3_FILE_OVERWRITE = True
# Setting AWS_QUERYSTRING_AUTH to False to remove query parameter authentication from generated URLs.
# This can be useful if your S3 buckets are public.
AWS_QUERYSTRING_AUTH = False
DEFAULT_FILE_STORAGE = os.getenv(
    "DEFAULT_FILE_STORAGE", "storages.backends.s3boto3.S3Boto3Storage"
)

# SECURITY
# https://docs.djangoproject.com/en/4.0/ref/settings/#csrf-trusted-origins
allowed_csrf_origins = os.getenv("CSRF_TRUSTED_ORIGINS", "http://127.0.0.1")
CSRF_TRUSTED_ORIGINS = [
    allowed_csrf_origins.strip()
    for allowed_csrf_origins in allowed_csrf_origins.split(",")
]
