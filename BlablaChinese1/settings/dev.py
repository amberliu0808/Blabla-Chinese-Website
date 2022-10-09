from .base import *
from decouple import config

# Override base.py settings here
# SECURITY WARNING: keep the secret key used in production secret!

# SECRET_KEY = config('SECRET_KEY')
SECRET_KEY = '+55v-#kn=c7#v!=3oh_wlf_k8qszgp-2qfi8zr5)z!vmn&1q8w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
