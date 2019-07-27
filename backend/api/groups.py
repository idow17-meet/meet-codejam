from fastapi import APIRouter, Depends
from typing import List, Dict

from .database import get_db
from .auth import get_current_user
from backend.database.model import DBGroup, OutGroup


groups = APIRouter()


@groups.get('/', response_model=Dict[str, List[OutGroup]])
def get_all_groups(current_user: DBGroup = Depends(get_current_user)):
    db_session = get_db()
    all_groups = db_session.get_all_groups() if current_user.admin else filter(lambda group: group.admin, db_session.get_all_groups())
    return {'groups': db_session.get_all_groups()}


@groups.get('/{group_name}', response_model=OutGroup)
def get_group(group_name: str, current_user: DBGroup = Depends(get_current_user)):
    db_session = get_db()
    return db_session.get_group(group_name)
