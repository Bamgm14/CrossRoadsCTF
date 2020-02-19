import os
import multiprocessing as m
import time as t
import sys
threads=[]
settupinfo={'ip':'127.0.0.1','cport':8000,'bport':31337}
def Check(lst):
    for x in lst:
        if x.lower().endswith('.py'):
            return '"python3 '+x+'"'
        if x.lower().endswith('.exe'):
            return x
def StartServer():
    print('Start')
    lst=[]
    for x in settings.split('\n'):
        try:
            lst.append(x.format(settupinfo['ip']))
        except:
            lst.append(x)
    with open("CrossRoads\\minictf\\settings.py",'w') as f:
        f.write('\n'.join(lst))
    os.system('cd CrossRoads && python3 manage.py runserver '+str(settupinfo['ip'])+':'+str(settupinfo['cport']))
def StartBackGround(x):
    print('Start')
    os.system('cd Background\\'+os.listdir(os.getcwd()+r'\Background')[x]+' && ncat -lvk '+str(settupinfo['ip'])+' '+str(settupinfo['bport']+x)+' -e '+str(Check(os.listdir(os.getcwd()+r'\\Background\\'+os.listdir(os.getcwd()+r'\Background')[x]))))
def Start():
    threads.append(('Server',m.Process(target=StartServer)))
    for x in range(len(os.listdir(os.getcwd()+r'\Background'))):
        threads.append(('Back'+str(x+1),m.Process(target=StartBackGround,args=(x,))))
    for x in threads:
        print(x[0]+' Starting Up')
        x[1].start()
if __name__ == "__main__":
    print("CTFManager:The Manager For This CTF")
    if "--help" in sys.argv:
        print("""
        python3 CTFManager.py --ip=<ip address> --cport=<website port> --bport=<background port range>
        Options:
        --ip/-i [IP Address Going To Be Used]
        --cport/-c [Website Connection Port]
        --bport/-b [Background Port Range, by adding ports to background programs]
        """)
        sys.exit(0)
    for x in sys.argv:
        if '--ip' in x or '-i' in x:
            settupinfo['ip']=x.split('=')[1]
        elif '-b' in x or '--bport' in x:
            settupinfo['bport']=x.split('=')[1]
        elif '-c' in x or '--cport' in x:
            settupinfo['cport']=x.split('=')[1]
    Start()
settings='''
"""
Django settings for minictf project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1' #Keep it secret.. set env on herokuapp with name 'KEY'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['{}']


# Application definition

INSTALLED_APPS = [
    'Web.apps.WebConfig',
    'MainPage.apps.MainpageConfig',
    'home.apps.HomeConfig',
    'accounts.apps.AccountsConfig',
    'challenges.apps.ChallengesConfig',
    'teams.apps.TeamsConfig',
    'scoreboard.apps.ScoreboardConfig',
    'forums.apps.ForumsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'minictf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            (os.path.join(BASE_DIR, 'templates'))
        ],
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

WSGI_APPLICATION = 'minictf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

LOGIN_REDIRECT_URL = '/challenges/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'challenges/uploads/')

MEDIA_URL = '/uploads/'
'''