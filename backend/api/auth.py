from fastapi import APIRouter, Cookie, Body, HTTPException, Depends
from starlette.responses import Response
from starlette.status import HTTP_401_UNAUTHORIZED
import jwt
from jwt.exceptions import PyJWTError
from datetime import datetime, timedelta
import os
import logging

from backend.conf import COOKIE_EXPIRATION_DEFAULT, ENV_SECRET_KEY, JWT_ALGORITHM
from backend.database.model import DBGroup, OutGroup
from .database import get_db


SECRET_KEY = os.environ.get(ENV_SECRET_KEY, None)
if not SECRET_KEY:
    logging.error(f"Missing authentication secret key '{ENV_SECRET_KEY}' as environment variable.")
    exit(1)

auth = APIRouter()


def create_token_cookie(*, data: dict, expires_delta: timedelta = timedelta(**COOKIE_EXPIRATION_DEFAULT)):
    """
    Creates a JWT string in order to be sent back as a session cookie
    :param data: The data to encode, typically the group's name / id
    :param expires_delta: Token's expiration date
    :return:
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=JWT_ALGORITHM)
    return encoded_jwt.decode(encoding='ascii')


async def get_current_user(session: str = Cookie(None)) -> DBGroup:
    """
    Gets current group object via the user's JWT cookie
    :param session: User's "session" cookie
    :return:
    """
    credentials_exception = HTTPException(
        status_code=HTTP_401_UNAUTHORIZED,
        detail="Invalid credential cookie",
    )

    if not session:
        raise credentials_exception
    try:
        payload = jwt.decode(session, SECRET_KEY, algorithms=[JWT_ALGORITHM])
        group_name: str = payload.get('sub')
        if group_name is None:
            raise credentials_exception

    except PyJWTError:
        raise credentials_exception
    db_session = get_db()
    group = db_session.get_group(group_name)
    if group is None:
        raise credentials_exception
    return group


@auth.post('/login')
async def login(*, username: str = Body(...), password: str = Body(...), response: Response):
    db_session = get_db()
    authenticated = db_session.is_correct_login(username, password)
    if authenticated:
        token = create_token_cookie(data={'sub': username})
        response.set_cookie(key='session', value=token)
    return {'success': authenticated}


@auth.post('/logout')
async def logout(response: Response):
    response.delete_cookie(key='session')
    return {'success': True}
