"""
Django settings for foodlocation project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g&!9gniaw!uipsw7o)5h6r#nmc(g83m=bfll&+)$jvp=8@20u)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'menufood.apps.MenufoodConfig',
    'ckeditor',
    'ckeditor_uploader',
    'rest_framework',
    'oauth2_provider',
    'drf_yasg',
    'corsheaders',
    'cloudinary',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'foodlocation.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'foodlocation.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

import pymysql

pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'foodlocaiondb',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': ''  # mặc định localhost
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# chỉ định nơi upload
CKEDITOR_UPLOAD_PATH = "ckeditor/menufood/"

# xác định nơi upload ảnh
MEDIA_ROOT = '%s/menufood/static/' % BASE_DIR

# chứng thực và phân quyền
AUTH_USER_MODEL = 'menufood.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',

    'PAGE_SIZE': 20,  # phân trang
}

CORS_ALLOW_ALL_ORIGINS = True

# (<<NTTN>>)
# CLIENT_ID = 'PX1L78DG7sjxUgndorfk2LTH8ye0jOWbcpRON1lI'
# CLIENT_SECRET = 'e2X37hXDnWDK1i2sNjCocfUqiDD6siUZKbB52xVjZ9yc2jYKE3PTtNvUNvPPukBGbKda5Iq9mU9L5aWiLZ0mkYpEprjJNkL6bkqnO3Rz4LxCrYDdgyE4Hpef1CL6P6IV'

#(<<DTKN>>)
CLIENT_ID = 'l8k5r5rRgKwsdHkBQIQjBbSdaL93odS3Uat6dtUk'
CLIENT_SECRET = 'QIIXY3ZH9NqaUgl63V3MHe1YvjzdfgDXsW7tmiV799J2r9P0a78AwGgyxprpp0yx4LT0VPuuwpMBT7LyJ45aRQvjtxPWCP9xwORXabIxNYEwvpQZPkwrUOYUphWB9MTe'


# config send email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'foodlocationapp@gmail.com' # Thay bằng email của bạn
EMAIL_HOST_PASSWORD = 'auwhudaioiziwhff' # Thay bằng password của bạn

# config cloudinary
cloudinary.config(
  cloud_name='tr-ng-h-m-tp-hcm',
  api_key="129162374872392",
  api_secret="Tpb6bk0-oTQf7B1o6wcwJU68c1Q"
)


