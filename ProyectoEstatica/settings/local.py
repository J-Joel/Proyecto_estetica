from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','.vercel.app','localhost'] # Para servidor en la nube static

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # Para servidor en la nube static

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
