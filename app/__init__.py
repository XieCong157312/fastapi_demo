from fastapi import FastAPI, Request, Depends, HTTPException, APIRouter,Header
from fastapi.middleware.cors import CORSMiddleware
from app.Utils import get_query_token
from .Item import views


__all__ = ["app", "Request", "Depends", "HTTPException", "APIRouter","Header"]

app = FastAPI(dependencies=[Depends(get_query_token)])


app.include_router(views.router)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
