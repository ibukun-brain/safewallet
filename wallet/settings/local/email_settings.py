from wallet.utils.env_variable import get_env_variable

# Sending email configuration
EMAIL_HOST_USER = get_env_variable(
    "EMAIL_HOST_USER", "contact@safewallet.com"
)

EMAIL_HOST_PASSWORD = get_env_variable("EMAIL_HOST_PASSWORD", "")

EMAIL_PORT = get_env_variable("EMAIL_PORT", 587)

EMAIL_HOST = get_env_variable("EMAIL_HOST", "smtp.gmail.com")

EMAIL_USE_SSL = True

# EMAIL_USE_TLS = True production only

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

SERVER_EMAIL = EMAIL_HOST_USER

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

ADMINS = [get_env_variable('ADMIN1'), get_env_variable('ADMIN2')]
