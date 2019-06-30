from fastapi import APIRouter
from .auth import auth

api = APIRouter()
api.include_router(auth, prefix='/auth', tags=['auth'])
