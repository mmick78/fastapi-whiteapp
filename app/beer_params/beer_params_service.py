from typing import List

from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.beer_params.beer_params_dto import BeerParamDTo, BeerParamInsertionDTO, BeerParamUpdateDTO
from app.beer_params.beer_params_models import BeerParamsModel
from app.core.logger import get_uvicorn_logger


def get_beer_parameters(db_session: Session) -> List[BeerParamDTo]:
    return db_session.query(BeerParamsModel).all()


def get_beer_param_per_name(db_session: Session, beer_name: str) -> BeerParamDTo:
    try:
        beer_param = db_session.query(BeerParamsModel).filter_by(name=beer_name).first()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f'Issue while retrieving parameter from db: {beer_name}. Sql Error: {e}')
    if not beer_param:
        raise HTTPException(status_code=400, detail=f'This beer parameter was not found: {beer_name}. Please verify the name before trying again!')
    return beer_param


def add_beer_param(db_session: Session, beer_parameter: BeerParamInsertionDTO, is_test: bool = False) -> str:
    try:
        beer_param = BeerParamsModel(**beer_parameter.dict())
        db_session.add(beer_param)
        if is_test:
            db_session.flush()
        else:
            db_session.commit()
        return 'Beer Parameter inserted with success !'
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f'Issue while inserting parameter in db: {beer_parameter}. Sql Error: {e}')


def update_beer_param(db_session: Session, beer_parameter: BeerParamUpdateDTO, is_test: bool = False) -> BeerParamDTo:
    try:
        # Get item from db first to see if it exists
        db_item = get_beer_param_per_name(db_session=db_session, beer_name=beer_parameter.name)

        # Keep only the fields provided
        dict_updated_data = beer_parameter.dict(exclude_unset=True)

        # Create an audit message of the fields updated and update them
        log_message = ''
        for key, value in dict_updated_data.items():
            if value != getattr(db_item, key):
                log_message += f'{key} Previous Value: {getattr(db_item, key)} / New Value: {value} \n'
                setattr(db_item, key, value)

        # Commit the changes if not testing mode
        if not is_test:
            db_session.commit()

        if log_message:
            get_uvicorn_logger().debug(log_message)

        return db_item
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f'Issue while updating parameter in db: {beer_parameter}. Sql Error: {e}')


def delete_beer_param(beer_name, db_session: Session, is_test: bool = False) -> str:
    try:
        item_to_be_deleted = get_beer_param_per_name(db_session=db_session, beer_name=beer_name)
        db_session.delete(item_to_be_deleted)
        if not is_test:
            db_session.commit()
        return 'Beer deleted with success !'
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f'Issue while deleting beer name in db: {beer_name}. Sql Error: {e}')
