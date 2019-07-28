from fastapi import APIRouter, Depends, HTTPException
from starlette.status import HTTP_404_NOT_FOUND
from typing import List, Dict

from .database import get_db
from .auth import get_current_user
from backend.database.model import DBGroup, OutGroup


groups = APIRouter()


def is_hidden_to_user(current_user: DBGroup, group: DBGroup) -> bool:
    """
    Returns whether the given group should be hidden to the user

    :param current_user: The user attempting to view the group
    :param group: The group that is inspected
    :return: True if the group is hidden to the user
    """
    return group.hidden and current_user.group_id != group.group_id and not current_user.admin


def filter_hidden_groups(current_user: DBGroup, all_groups: List[DBGroup]):
    return [group for group in all_groups if not is_hidden_to_user(current_user, group)]


@groups.get('/', response_model=Dict[str, List[OutGroup]])
def get_all_groups(current_user: DBGroup = Depends(get_current_user)):
    db_session = get_db()
    all_groups = db_session.get_all_groups()
    if not current_user.admin:
        all_groups = filter_hidden_groups(current_user, all_groups)
    return {'groups': all_groups}


@groups.get('/{group_name}', response_model=OutGroup)
def get_group(group_name: str, current_user: DBGroup = Depends(get_current_user)):
    db_session = get_db()
    group = db_session.get_group(group_name)
    if not group or is_hidden_to_user(current_user, group):
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail="Group not found."
        )
    return group
