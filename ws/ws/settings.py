# Django settings for ws project.
import os
import logging

DEBUG = True

# Sms center settings
SERVICE_URL = 'http://localhost/'
SERVICE_USERNAME = 'username'
SERVICE_PASSWORD = 'password'
SERVICE_ID = 'free'

# Logging settings
LOG_FILE = 'sms_log' # you can add dir+filename like /var/log/sms/sms_log
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(filename=LOG_FILE,level=logging.INFO)

# Database settings
DATABASE_HOST = '127.0.0.1'
DATABASE_PORT = 27017
DATABASE_USE = ''
DATABASE_PASS = ''
DATABASE_NAME = 'smskeygen'

# Soap settings
SOAP_NAME = 'smskeygen'
SOAP_TNS = 'http://local.host'
SOAP_LOCATION = 'http://127.0.0.1:8000/api/'

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = '^0er&7nna17+@+v1-e$t!j$y=yr1+ue+kleifumu_89@8&+l%o'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ws.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'ws.wsgi.application'

# Web service settings for connecting to SMS center
# connect : for connecting to web service
# step(int) : for connecting to services. some SMS centers have login service before sending
# and some others just have calling service name with username and password. So you can do it:
# "step1:" { "service":"sendmsg","argv" : (SERVICE_USERNAME,SERVICE_PASSWORD,{message},{mobile}) }
# Any things depends on the API of SMS centers. So please read cerfully DEV doc of SMS center!
# You can add more steps or remove other steps. One step in nessesery for running!
WEB_SERVICE = {
    "connect": {
        "url" : SERVICE_URL,
        "argv" : (SERVICE_USERNAME,SERVICE_PASSWORD), # order is too important!
    },
    "step1": {
        "service" : "Login",
        "argv" : (SERVICE_USERNAME,SERVICE_PASSWORD), # order is too important!
    },
    "step2": {
        "service" : "SendMessage",
        "argv" : (SERVICE_USERNAME,SERVICE_PASSWORD,'{message}','{mobile}',SERVICE_ID),  # order is too important! {} are just for message and mobile!!!
    },
}