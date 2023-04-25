import dj_database_url

from .base_settings import *

from wallet.settings.local.mailhog_settings import *

INSTALLED_APPS += [
    "debug_toolbar",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware"
]

INTERNAL_IPS = [
    "127.0.0.1",
]

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
STATIC_ROOT = BASE_DIR / 'static_root'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DATABASES["default"] = dj_database_url.parse(
    f"sqlite:////{BASE_DIR.joinpath(BASE_DIR.name)}.db", conn_max_age=600,
)
