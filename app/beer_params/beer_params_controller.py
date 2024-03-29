from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.beer_params.beer_params_dto import BeerParamDTo, BeerParamInsertionDTO, BeerParamUpdateDTO
from app.beer_params.beer_params_service import get_beer_parameters, get_beer_param_per_name, update_beer_param, add_beer_param, delete_beer_param
from app.utils.db import get_db

router = APIRouter()


@router.get('/', response_model=List[BeerParamDTo])
def get_beer_params(db: Session = Depends(get_db)):
    """
        All the beers available in the Db
    """
    return get_beer_parameters(db_session=db)


@router.get('/{beer_name}', response_model=BeerParamDTo)
def get_beer_params(beer_name: str, db: Session = Depends(get_db)):
    """
        Get specific beer per name available in the Db
    """
    return get_beer_param_per_name(db_session=db, beer_name=beer_name)


@router.post('', response_model=str)
def add_beer_params(beer_param: BeerParamInsertionDTO, db: Session = Depends(get_db)):
    """
        Add a beer in the Db
    """
    return add_beer_param(db_session=db, beer_parameter=beer_param, is_test=False)


@router.patch('/', response_model=BeerParamUpdateDTO)
def update_beer_params(beer_param: BeerParamUpdateDTO, db: Session = Depends(get_db)):
    """
        Update a  specific beer per name available in the Db
    """
    return update_beer_param(db_session=db, beer_parameter=beer_param, is_test=False)


@router.delete('/{beer_name}', response_model=str)
def delete_beer_params(beer_name: str, db: Session = Depends(get_db)):
    """
        Delete a specific beer per name available in the Db
    """
    return delete_beer_param(db_session=db, beer_name=beer_name, is_test=False)
