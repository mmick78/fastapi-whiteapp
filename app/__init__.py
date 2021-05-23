from fastapi import APIRouter

from app.health_check import health_check_controller
from app.beer_params import beer_params_controller

api_router = APIRouter()

api_router.include_router(health_check_controller.router, prefix='/health_check', tags=['health_check-controler'])
api_router.include_router(beer_params_controller.router, prefix='/beer_parameters', tags=['beer_parameters-controler'])
