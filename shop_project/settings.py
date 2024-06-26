"""
Django settings for shop_project project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
# import pytesseract
from pathlib import Path
import os
import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ys#u2o80@kf$zmkhb58ni)4_+tn#=pb6l!a44^=hn!#%%rtpt6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


#ALLOWED_HOSTS = ['127.0.0.1','*','shop-new-backened.herokuapp.com','shopbackened.onrender.com','shopbackened.up.railway.app']
ALLOWED_HOSTS = ['*']
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shopAccountKdm',
    'shopAccountTpm',
    'houseAccount',
    'rest_framework',
    'corsheaders'
]
CORS_ORIGIN_ALLOW_ALL =True




# TesseractPath = r'C:\Users\shahul.m\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'  
# TesseractPath = r'C:\Users\shahul.m\Documents\shop_backened_enhancement\shop_project\Tesseract-OCR\tesseract.exe'


# TesseractPath =  os.path.join(BASE_DIR,'shop_project','Tesseract-OCR','tesseract.exe')
# pytesseract.pytesseract.tesseract_cmd = TesseractPath


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shop_project.urls'

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

WSGI_APPLICATION = 'shop_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME':  'dcr3u1l9qjphtm',
#         'USER':'ohbvalvqeimebw',
#         'PASSWORD': 'd16c96410eb672c25e265ab4976b47f9cd25209623e67dcc81b82648435f186b',
#         'HOST': 'ec2-44-199-9-102.compute-1.amazonaws.com',
#         'PORT':'5432'
#     }
# }

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME':  'railway',
    #     'USER':'postgres',
    #     'PASSWORD': 'mZptZjt6selI2VRwZl8k',
    #     'HOST': 'containers-us-west-66.railway.app',
    #     'PORT':'6694'
    # }
 'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':  'railway',
        'USER':'postgres',
        'PASSWORD': 'FDg13Dc5gbgcggGF4AFC6gdBd4FGf4dC',
        'HOST': 'viaduct.proxy.rlwy.net',
        'PORT':'21583'
    }


}
# DATABASES["default"] = dj_database_url.parse("postgres://xerox_shop_user:9AMgRC93vJcwMfE4tOf1WSjxyNQyYqqt@dpg-cplilpdds78s73ekuoag-a.oregon-postgres.render.com/xerox_shop")
DATABASES["default"] = dj_database_url.parse("postgres://postgres.kzzurfojmqokxutadtrh:shahulhameed7@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres")
# username: shahul
# password : shahul7 
# for admin credentials

# username: shahul
# password : shahulhameed7  
# for supabase free postgres db
# https://supabase.com/dashboard/project/kzzurfojmqokxutadtrh/storage/buckets

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
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')


STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
