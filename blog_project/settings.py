import os
from django.utils.translation import gettext_lazy as _ 



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '6+_(6czw@+gbm$5q@j6u#ubk^)19o&0+3wi!2u(%x^^y^!d(j#'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1','worthygram.com','www.worthygram.com','100.25.170.202']




INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',

    
    # My_apps.
    'blog',
    'users.apps.UsersConfig',
    'footer',

    # Third_party_apps.
    'widget_tweaks',
    'django_social_share',
    'pwa',
    'storages',
    'embed_video',
    'rosetta',  # NEW
    'parler',  # NEW

]

DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location':  os.path.join(BASE_DIR, 'backup')}
DJANGORESIZED_DEFAULT_FORCE_FORMAT = 'WEBP'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', # new
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blog_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'blog_project.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql_psycopg2',
'NAME': 'worthygram',
'USER' : 'worthygram_official',
# 'USER' : 'postgres',
'PASSWORD' : 'Palash@90',
'HOST' : 'localhost',
'PORT' : '',
}
}



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

PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'blog/static/blog/js', 'serviceworker.js')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AWS_ACCESS_KEY_ID = 'AKIARH5WEAWIQRIKGRML'
AWS_S3_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'worthygram'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=31536000'}
AWS_QUERYSTRING_AUTH = 'False'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

SITE_ID = 1

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


LANGUAGES = (
    ('en', _('English')),
    ('hi', _('Hindi')),
)

PARLER_LANGUAGES = {
    1: (
        {'code': 'en',}, # English
        {'code': 'hi',}, # Hindi
    ),
    'default': {
        'fallbacks': ['en'],
        'hide_untranslated': False,
    }
}

LOCALE_PATHS = [
    # BASE_DIR / 'locale/',
    os.path.join(BASE_DIR,'/locale/')
]


# EMAIL CONFIGURATION (for contact form)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'worthygram@gmail.com'
EMAIL_HOST_PASSWORD = 'cbzcebvtwyqahjti'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


LOGIN_REDIRECT_URL = 'blog:home'
LOGIN_URL = 'login'

ADMIN_SITE_HEADER = "BUDDIES"

TIME_ZONE =  'Asia/Kolkata'


PWA_APP_NAME = 'Worthygram'
PWA_APP_DESCRIPTION = "Turn your reel happiness into real happiness, try Worthygram"
PWA_APP_THEME_COLOR = '#0A0302'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ID = '/'

PWA_APP_ICONS = [
	{
		'src': '/static/blog/img/logo.png',
		'sizes': '160x160',
        "type": "image/png",
	}
]
PWA_APP_ICONS_APPLE = [
	{
		'src': '/static/blog/img/logo.png',
		'sizes': '160x160',
        "type": "image/png",

	}
]
PWA_APP_SPLASH_SCREEN = [
	{
		'src': '/static/blog/img/logo.png',
        'sizes': '512x512',
        "type": "image/png",
		'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
	}
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'





