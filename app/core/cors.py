""""
CORS or "Cross-Origin Resource Sharing" refers to the situations when a frontend running in a browser has JavaScript code
that communicates with a backend, and the backend is in a different "origin" than the frontend.
Origin¶
An origin is the combination of protocol (http, https), domain (myapp.com, localhost, localhost.tiangolo.com), and port (80, 443, 8080).

So, all these are different origins:

http://localhost
https://localhost
http://localhost:8080
Even if they are all in localhost, they use different protocols or ports, so, they are different "origins".
"""

from typing import List

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


def init_cors(fast_api_app: FastAPI, authorized_origins: List[str] = None) -> None:
    fast_api_app.add_middleware(
        CORSMiddleware,
        allow_origins=authorized_origins if authorized_origins else ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
