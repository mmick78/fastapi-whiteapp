import os
from traceback import format_exc

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StartletteHTTPException

from app import api_router
from app.core.config import Config, LOGGING
from app.core.cors import init_cors
from app.core.logger import get_uvicorn_logger

app = FastAPI(title=Config.PROJECT_NAME, openapi_url='/swagger.json')

# Include main router, if you wish to add new routes please add them there
app.include_router(api_router, prefix=Config.API_PATH_VERSION)

# Init CORS setting to allow connection with different origins
init_cors(fast_api_app=app)


def create_app(reload: bool = False, workers: int = 1):
    app_port: int = int(os.environ.get('APP_PORT', '4200'))  # Default to 4200 if nothing is specified
    print(f'Swagger accessible at this path: http://localhost:{app_port}/docs')
    uvicorn.run("main:app", host="0.0.0.0", port=app_port, log_level="debug", log_config=LOGGING, reload=reload, workers=workers)


# Catch all exceptions (and HTTP Exceptions more specifically) to be able to log them
@app.exception_handler(Exception)
async def exception_handler(request: Request, ex: Exception) -> StartletteHTTPException:
    msg = f'Issue while calling this path: {request.url}. Error: {ex}. Full Traceback: {format_exc()}'
    get_uvicorn_logger().error(msg)
    return StartletteHTTPException(status_code=500, detail=msg)


@app.exception_handler(StartletteHTTPException)
async def http_exception_handler(request: Request, ex: StartletteHTTPException) -> JSONResponse:
    msg = f'Issue while calling this path: {request.url}. Error: {ex.detail}. Full Traceback: {format_exc()}'
    get_uvicorn_logger().error(msg)
    return JSONResponse(status_code=ex.status_code, content=str(ex.detail))


if __name__ == '__main__':
    dict_mapping_reload = {'NO': False, 'YES': True}
    is_reload = os.environ.get('RELOAD', True)
    is_reload = dict_mapping_reload.get(is_reload, is_reload)
    nb_workers = int(os.environ.get('NB_WORKERS', 1))
    create_app(reload=is_reload, workers=nb_workers)
