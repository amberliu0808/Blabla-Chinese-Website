from .base import *
from decouple import config

# Override base.py settings here

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

EMAIL_HOST_NAME = 'amberliu0808@foxmail.com'
# EMAIL_HOST_NAME = '1540117707@qq.com'
EMAIL_HOST_PASSWORD = 'jrdfjxuajeijjbhh'
EMAIL_HOST_PASSWORD = 'jrdfjxuajeijjbhh'
