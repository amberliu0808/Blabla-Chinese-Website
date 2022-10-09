from .base import *
from decouple import config

# Override base.py settings here
# SECURITY WARNING: keep the secret key used in production secret!

# SECRET_KEY = config('SECRET_KEY')
SECRET_KEY = '+55v-#kn=c7#v!=3oh_wlf_k8qszgp-2qfi8zr5)z!vmn&1q8w'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SECURE_HSTS_SECONDS = 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
