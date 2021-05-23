import pytest
from fastapi.testclient import TestClient

from app.utils.session import SessionLocal
from app.beer_params.beer_params_dto import BeerParamInsertionDTO
from main import app as _app


@pytest.fixture(scope='module')
def app() -> TestClient:
    """Module wide test 'fastapi' application """
    app = TestClient(_app)
    return app


def get_db() -> SessionLocal:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.rollback()
        db.close()


@pytest.fixture(scope='class')
def db_session():
    return next(get_db())


@pytest.fixture(scope='function')
def beer_name() -> str:
    return 'test_stout'


@pytest.fixture(scope='function')
def list_attributes_to_check() -> list:
    return ['name', 'percentage_alcohol', 'color', 'type']


@pytest.fixture(scope='function')
def beer_insertion() -> BeerParamInsertionDTO:
    return BeerParamInsertionDTO(**{'name': 'test_test', 'percentage_alcohol': 0, 'color': 'unknown', 'type': 'NA'})


@pytest.fixture(scope='function')
def fail_beer_insertion() -> BeerParamInsertionDTO:
    return BeerParamInsertionDTO(**{'name': 'test_stout', 'percentage_alcohol': 0, 'color': 'unknown', 'type': 'NA'})
