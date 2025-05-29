from pathlib import Path
from datetime import timedelta
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ind3+s%fy7!u4ig4jvdsu+*m#)7a+&h7-m2dv#@6c900_v%cy6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "http://localhost:3000",  # Ajouter l'origine de votre front-end
    "localhost",              # Assurez-vous que localhost est autorisé
    "127.0.0.1",             # Si vous utilisez 127.0.0.1 pour accéder à Django
]

# CORS settings
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Frontend Next.js
]

CORS_ALLOW_HEADERS = [
    'content-type',
    'authorization',  # Si vous envoyez un token d'authentification
    'x-csrftoken',    # Si vous utilisez des tokens CSRF
]

CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'DELETE',
    'OPTIONS',
    'PATCH',
]

# Si vous voulez désactiver complètement CORS pour le développement
# CORS_ALLOW_ALL_ORIGINS = True  # Permet à toutes les origines de faire des requêtes

# JWT settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=2),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
}

# Application definition
INSTALLED_APPS = [
    'jazzmin',                
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'charges_app',
    'documents_app',
    'corsheaders', 
    'properties_app',
    'auth_app',
    'residences_app',
    'interventions',
]

# CORS Middleware configuration
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Doit être ajouté en premier
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # À ne pas supprimer
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project_codetime_django.urls'

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

WSGI_APPLICATION = 'project_codetime_django.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'syndicnadb',       # Replace with your database name
        'USER': 'postgres',     # Replace with your database username
        'PASSWORD': 'youssefpg',    # Replace with your database password
        'HOST': 'localhost',         # Use '127.0.0.1' if needed
        'PORT': '5432',              # Default PostgreSQL port
    }
}

# Password validation
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

# Utilisation du modèle utilisateur personnalisé
AUTH_USER_MODEL = 'auth_app.CustomUser'

# Configuration REST Framework pour l'authentification JWT
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# Configurations pour les fichiers médias
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Tunis'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Or your SMTP server
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'testsyndic7@gmail.com'
EMAIL_HOST_PASSWORD = 'ykcilosikeesfade'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


JAZZMIN_SETTINGS = {
    "site_title": "Syndic Admin",
    "site_header": "Syndic Dashboard",
    "site_brand": "Syndicna",
    "welcome_sign": "Welcome to the Syndic Admin Panel",
    "site_logo": "images/logo_Syndicna.png",        # logo in the navbar
    "login_logo": "images/logo_Syndicna.png",  
    "site_logo_classes": "img-circle",  # Optional: round style

    "user_avatar": None,  # Set to None if you don’t have user profile pics

    # Dark mode settings
    "theme": "darkly",  # 👈 Available dark themes: darkly, cyborg, slate, etc.

    # Optional extras
    "show_sidebar": True,
    "navigation_expanded": True,

    "icons": {
        # Auth / Users
        "auth_app.CustomUser": "fas fa-user-shield",
        "auth_app.UserLoginHistory": "fas fa-history",         # User login histories
        "auth_app.UserLoginPrediction": "fas fa-chart-line",   # User login predictions

        # Charges_App
        "Charges_App.ChargePrediction": "fas fa-chart-bar",    # Charge predictions
        "Charges_App.Charge": "fas fa-file-invoice-dollar",
        "Charges_App.PropertyCharge": "fas fa-home",           # Property charges

        # Documents_App
        "Documents_App.Document": "fas fa-file-alt",            # Documents
        "Documents_App.Invoice": "fas fa-file-invoice",         # Invoices

        # Interventions
        "interventions.Intervention": "fas fa-tools",          # Interventions (existing)

        # Properties_App
        "Properties_App.Property": "fas fa-building",           # Properties

        # Residences_App
        "Residences_App.Residence": "fas fa-city",              # Residences
    },


    "custom_css": "css/admin_custom.css",
}


