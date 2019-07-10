from fastapi import APIRouter, Depends, HTTPException
from starlette.status import HTTP_404_NOT_FOUND
from typing import List
import logging

from backend.database.model import DBGroup, OutScore
from .database import get_db
from .auth import get_current_user


scores = APIRouter()


@scores.get('/', response_model=List[OutScore], response_model_exclude={'group_id'})
def get_current_group_scores(current_user: DBGroup = Depends(get_current_user)):
    return get_group_scores(current_user.name)


@scores.get('/{group_name}', response_model=List[OutScore], response_model_exclude={'group_id'})
def get_group_scores(group_name: str, current_user: DBGroup = Depends(get_current_user)):
    db_session = get_db()
    group_scores = db_session.get_group_scores(group_name)
    if not group_scores:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="No scores found for the given group name")
    output_scores = []
    for problem in db_session.get_all_problems():
        try:
            score = [score for score in group_scores if score.problem_id == problem.problem_id][0]
            output_scores.append(OutScore(**score.dict(), problem=problem))
        except IndexError:
            logging.error(f"Score not found for problem id: {problem.problem_id}")

    output_scores.sort(key=lambda score: score.problem.difficulty)
    return output_scores


@scores.get('/{group_name}/{problem_name}', response_model=OutScore)
def get_group_score(group_name: str, problem_name: str, current_user: DBGroup = Depends(get_current_user)):
    db_session = get_db()
    score = db_session.get_group_score(group_name, problem_name)

    if not score:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="Score not found")
    problem = db_session.get_problem(problem_name)
    new_score = OutScore(**score.dict(), problem=problem)
    return new_score
