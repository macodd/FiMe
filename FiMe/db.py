# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
import dj_database_url

from .env import config

DATABASE_URL = config("DATABASE_URL", default=None)

if DATABASE_URL is not None:
    DATABASES = {
        "default": dj_database_url.config(
            default=DATABASE_URL, conn_max_age=600, conn_health_checks=True
        )
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "fime_db",
            "USER": config("DB_USER", default="db-user"),
            "PASSWORD": config("DB_PASSWORD", default="db-password"),
            "HOST": "localhost",
            "PORT": "5432",
        }
    }
