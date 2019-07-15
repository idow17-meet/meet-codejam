from fastapi import APIRouter, Depends, HTTPException, Body
from starlette.responses import Response
from starlette.status import HTTP_404_NOT_FOUND
from typing import List
import logging

from backend.database.model import DBGroup, OutScore, DBScore
from .database import get_db, CodejamDB
from .auth import get_current_user


scores = APIRouter()


def create_out_score(db_session: CodejamDB, score: DBScore) -> OutScore:
    """
    Converts a Database score to an OutScore (binds the problem instance and removes hint if necessary)

    :param db_session: The current database session to query with
    :param score: The score as queried from the database
    :return: A new OutScore instance with a binded problem
    """
    problem = db_session.get_problem(score.problem_id)
    if not problem:
        raise ValueError(f"Problem not found for score: {score}")

    out_score = OutScore(**score.dict(), problem=problem)
    if not score.hint_used:
        out_score.problem.hint = None
    return out_score


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
    for score in group_scores:
        try:
            output_scores.append(create_out_score(db_session, score))
        except ValueError as e:
            logging.error(str(e))

    output_scores.sort(key=lambda score: score.problem.difficulty)
    return output_scores


@scores.get('/{group_name}/{problem_name}', response_model=OutScore)
def get_group_score(group_name: str, problem_name: str, current_user: DBGroup = Depends(get_current_user)):
    db_session = get_db()
    score = db_session.get_group_score(group_name, problem_name)

    if not score:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="Score not found")

    try:
        return create_out_score(db_session, score)
    except ValueError as e:
        logging.error(str(e))
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="Problem not found for score instance")


@scores.post('/{problem_name}')
def submit_answer(problem_name: str,
                  answer: str = Body(...),
                  code: str = Body(...),
                  current_user: DBGroup = Depends(get_current_user)):
    db_session = get_db()
    correct_answer = db_session.submit_answer(current_user.name, problem_name, answer, code)
    return {"correct": correct_answer}


@scores.patch('/{problem_name}/hint')
def use_hint(problem_name: str, response: Response, current_user: DBGroup = Depends(get_current_user)):
    db_session = get_db()
    hint = db_session.use_hint(current_user.name, problem_name)
    if not hint:
        response.status_code = HTTP_404_NOT_FOUND
    return {"hint": hint}
