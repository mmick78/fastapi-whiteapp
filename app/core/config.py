import os
import getpass


class BaseConfig(object):
    ENV = 'DEV'

    # API
    API_PATH_VERSION = '/api/v1'
    PROJECT_NAME = 'WHITE_APP_FAST_API'
    PROJECT_VERSION = '1.0'
    LOGGER_PATH = f'{os.path.dirname(os.path.abspath(__file__))}\\Logs\\white_app.log'

    # DB Configuration
    DB_NAME = 'test'

    def __init__(self):
        # DB Connection SQLAlchemy
        self.SQLALCHEMY_DATABASE_URL = f"sqlite:///./{self.DB_NAME}.db"


class DevelopmentConfig(BaseConfig):
    def __init__(self):
        super().__init__()


class ProductionConfig(BaseConfig):
    ENV = 'PROD'

    LOGGER_PATH = f'{os.path.dirname(os.path.abspath(__file__))}\\Logs\\white_app.log'  # Change it to a prod parameter

    # DB Configuration
    DB_NAME = 'prod'

    def __init__(self):
        super().__init__()


config_name = dict(
    development=DevelopmentConfig(),
    production=ProductionConfig()
)

Config = config_name[os.environ.get('APP_ENV', 'development')]  # Default Env to dev if not specified as we don't want to run in prod by default

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {'fmt': '%(levelprefix)s %(message)s', 'use_colors': None},
        'access': {'format': f'[%(levelname)s]-[%(asctime)s]-[{getpass.getuser()}]-[%(name)s]-%(message)s', 'use_colors': True}
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'access',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'access',
            'when': 'midnight',
            'interval': 1,
            'filename': Config.LOGGER_PATH,
            'backupCount': 3
        }
    },
    'loggers': {
        'uvicorn': {'handlers': ['console'], 'level': 'DEBUG'},
        'uvicorn.error': {'level': 'DEBUG', 'handlers': ['file'], 'propagate': True},
        'uvicorn.access': {'handlers': ['file'], 'level': 'DEBUG', 'propagate': False},
    }
}
