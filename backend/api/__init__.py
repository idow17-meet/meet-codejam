from fastapi import APIRouter
from .auth import auth
from .scores import scores
from .groups import groups

api = APIRouter()
api.include_router(auth, prefix='/auth', tags=['auth'])
api.include_router(scores, prefix='/scores', tags=['scores'])
api.include_router(groups, prefix='/groups', tags=['groups'])
