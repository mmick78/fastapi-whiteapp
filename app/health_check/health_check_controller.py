from fastapi import APIRouter

from app.health_check.health_check_dto import HealthCheckDto

router = APIRouter()


@router.get('/', response_model=HealthCheckDto)
async def get_health_status():
    return {'message': 'Up'}
