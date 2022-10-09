from .base import *
from decouple import config

# Override base.py settings here

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
<<<<<<< HEAD
DEBUG = False
=======
DEBUG = True
>>>>>>> origin/master


EMAIL_HOST_NAME = 'amberliu0808@foxmail.com'
# EMAIL_HOST_NAME = '1540117707@qq.com'
<<<<<<< HEAD
EMAIL_HOST_PASSWORD = 'jrdfjxuajeijjbhh'
=======
EMAIL_HOST_PASSWORD = 'jrdfjxuajeijjbhh'
>>>>>>> origin/master
