from pathlib import Path
import os
import sys

BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY = 'django-insecure-sc%u%h2dap2jwnm2y9-#2*@cr54j1)9-2wh306x(j!+_ra-4#o'
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-sc%u%h2dap2jwnm2y9-#2*@cr54j1)9-2wh306x(j!+_ra-4#o",
)

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    # Local apps
    "asct",
    "users",
    "docs",
    "notes",
    "ai",
    # Third-party apps
    "debug_toolbar",
    "django.contrib.sites",
    # Celery apps
    "django_celery_beat",
    "django_celery_results",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

DEBUG_TOOLBAR_CONFIG = {
    # Set a high z-index to ensure the toolbar appears above other elements.
    "RESULTS_CACHE_SIZE": 100,
    "SHOW_TOOLBAR_CALLBACK": lambda request: True,
}

INTERNAL_IPS = [
    "127.0.0.1",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "aism_v1",
        "USER": "postgres",
        "PASSWORD": "1111",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Seoul"
USE_I18N = True
USE_TZ = True

# Encoding
FILE_CHARSET = "utf-8"
DEFAULT_CHARSET = "utf-8"

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

LOGIN_REDIRECT_URL = "main-index"
LOGOUT_REDIRECT_URL = "main-index"
# allauth 관련
ACCOUNT_SIGNUP_FIELDS = ["email*", "username*", "password1*", "password2*"]
ACCOUNT_LOGIN_METHODS = {"username", "email"}
# ACCOUNT_AUTHENTICATION_METHOD = 'username_email' # 로그인 시 아이디/이메일 모두 허용
ACCOUNT_EMAIL_VERIFICATION = "optional"  # 이메일 인증 설정 (mandatory, optional, none)

LOGIN_URL = "login"
# LOGIN_URL = 'users:login'

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "ml.python.ai@gmail.com"
EMAIL_HOST_PASSWORD = "dtty tgfa lxzm bhue"

CART_ID = "cart_in_session"

# Celery Configuration
CELERY_BROKER_URL = "redis://localhost:6379/0"
CELERY_RESULT_BACKEND = "django-db"
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = TIME_ZONE
# DB 기반 스케줄러 사용 (django-celery-beat)
# 이 설정을 추가하면 위쪽의 CELERY_BEAT_SCHEDULE 딕셔너리는 무시되고 DB의 내용을 따릅니다.
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"

# 로깅 설정
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

if "SERVICE_TYPE" in os.environ:
    SERVICE_TYPE = os.environ["SERVICE_TYPE"]
elif len(sys.argv) > 0 and "celery" in sys.argv[0].lower():
    if "worker" in sys.argv:
        SERVICE_TYPE = "worker"
    elif "beat" in sys.argv:
        SERVICE_TYPE = "beat"
    else:
        SERVICE_TYPE = "celery"
else:
    SERVICE_TYPE = "web"

# 운영체제에 따른 로깅 핸들러 설정 분기
# Windows: 개발 편의를 위해 Django가 직접 회전 (TimedRotatingFileHandler)
# Linux: Gunicorn 멀티 프로세스 환경에서의 충돌 방지를 위해 외부 logrotate 사용 (WatchedFileHandler)
if os.name == "nt":
    LOG_HANDLER_CLASS = "logging.FileHandler"
    # Windows 환경에서 파일 잠금(WinError 32) 방지를 위해 Log Rotation 중지
    LOG_HANDLER_KWARGS = {}
else:
    LOG_HANDLER_CLASS = "logging.handlers.WatchedFileHandler"
    LOG_HANDLER_KWARGS = {}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[{asctime}] {levelname} [{name}:{lineno}] {message}",
            "style": "{",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "file": {
            "level": "INFO",
            "class": LOG_HANDLER_CLASS,
            "filename": str(LOG_DIR / f"asct_system_{SERVICE_TYPE}.log"),
            "encoding": "utf-8",
            **LOG_HANDLER_KWARGS,
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file", "console"],
            "level": "INFO",
            "propagate": True,
        },
        # 'asct' 앱에 대한 로거 설정
        "asct": {
            "handlers": ["file", "console"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}
