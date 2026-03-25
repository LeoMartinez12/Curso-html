# carniceria/settings.py
from pathlib import Path

# Carpeta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------
# Aplicaciones instaladas
# -----------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tienda',  # tu app
]

# -----------------------
# Middleware
# -----------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',        # obligatorio
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',      # obligatorio
    'django.contrib.messages.middleware.MessageMiddleware',         # obligatorio
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -----------------------
# URLs principales
# -----------------------
ROOT_URLCONF = 'carniceria.urls'

# -----------------------
# Templates
# -----------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'tienda' / 'templates'],  # ruta a tus HTML
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

# -----------------------
# WSGI
# -----------------------
WSGI_APPLICATION = 'carniceria.wsgi.application'

# -----------------------
# Base de datos (SQLite)
# -----------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',   # motor SQLite
        'NAME': BASE_DIR / 'db.sqlite3',          # archivo que Django crea
    }
}

# -----------------------
# Contraseñas (modo desarrollo)
# -----------------------
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

# -----------------------
# Idioma y zona horaria
# -----------------------
LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_TZ = True

# -----------------------
# Archivos estáticos
# -----------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'tienda' / 'static']  # CSS, JS, imágenes

# -----------------------
# Configuración de media (opcional)
# -----------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# -----------------------
# Clave secreta (solo desarrollo)
# -----------------------
SECRET_KEY = 'django-insecure-reemplaza-esta-clave-por-una-segura'

# -----------------------
# Modo debug (desarrollo)
# -----------------------
DEBUG = True

ALLOWED_HOSTS = []