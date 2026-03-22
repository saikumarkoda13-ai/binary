"""
Django settings for BinaryConfig project.
"""

import os
from pathlib import Path

# =========================
# BASE DIRECTORY
# =========================

BASE_DIR = Path(__file__).resolve().parent.parent


# =========================
# SECURITY
# =========================

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-secret-key')

DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = []
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# =========================
# INSTALLED APPS
# =========================

INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Custom Apps
    'users',
    'admins',
]


# =========================
# MIDDLEWARE
# =========================

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


# =========================
# URLS
# =========================

ROOT_URLCONF = 'BinaryConfig.urls'


# =========================
# TEMPLATES
# =========================

TEMPLATES = [
{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',

    # ✅ correct template path
    'DIRS': [BASE_DIR / 'assets' / 'templates'],

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


# =========================
# WSGI
# =========================

WSGI_APPLICATION = 'BinaryConfig.wsgi.application'


# =========================
# DATABASE
# =========================

DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite3',
}
}


# =========================
# PASSWORD VALIDATION
# =========================

AUTH_PASSWORD_VALIDATORS = [

{'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
{'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
{'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
{'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},

]


# =========================
# LANGUAGE
# =========================

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True
USE_TZ = True


# =========================
# STATIC FILES
# =========================

STATIC_URL = '/static/'

# ✅ MAIN STATIC FOLDER (IMPORTANT)
STATICFILES_DIRS = [
    BASE_DIR / 'assets' / 'static'
]

# ✅ production ki use avutundi (ippudu ignore cheyyachu)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# ✅ WhiteNoise configuration
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# =========================
# MEDIA FILES
# =========================

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# =========================
# DEFAULT PRIMARY KEY
# =========================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'