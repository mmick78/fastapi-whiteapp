import os


def create_db_models(env: str) -> None:
    if str(env.upper()) in ['PRODUCTION', 'PROD', 'PRD']:
        os.environ['APP_ENV'] = 'production'
    elif str(env.upper) in ['development', 'DEV']:
        os.environ['APP_ENV'] = 'development'

    from app.utils.session import engine, Base
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    create_db_models(env='dev')
