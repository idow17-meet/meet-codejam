from fastapi import APIRouter
from .auth import auth
from .scores import scores

api = APIRouter()
api.include_router(auth, prefix='/auth', tags=['auth'])
api.include_router(scores, prefix='/scores', tags=['scores'])
