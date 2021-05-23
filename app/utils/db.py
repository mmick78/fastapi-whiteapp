from app.utils.session import SessionLocal


# Dependency (see fastapi documentation), if using python version below 3.7 it requires async-generator and async-exist-stack to allow async dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
