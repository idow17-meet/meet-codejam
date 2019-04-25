"""
Defines translations between mongo's documents and the project's dataclasses
"""

import backend.database.model as model
import mongo.consts as const


##
# Documents to dataclasses:
##


def document_to_score(document: dict) -> model.Score:
    """
    Creates a score instance from a document

    :param document: The document to create an instance from
    :return: The matching score instance
    """
    return model.Score(
        group_id=str(document[const.SCORE_GROUP_ID]),
        problem_id=str(document[const.SCORE_PROBLEM_ID]),
        current_points=document.get(const.SCORE_CURRENT_POINTS, 0),
        submitted_answer=document.get(const.SCORE_SUBMITTED_ANSWER, None),
        submitted_code=document.get(const.SCORE_SUBMITTED_CODE, None),
        hint_used=document.get(const.SCORE_HINT_USED, False),
        score_id=str(document.get(const.ID_KEY))
    )


def document_to_group(document: dict) -> model.Group:
    """
    Creates a group instance from a document

    :param document: The document to create an instance from
    :return: The matching group instance
    """
    return model.Group(
        name=document[const.GROUP_NAME],
        members=document[const.GROUP_MEMBERS],
        password=document[const.GROUP_PASSWORD],
        hidden=document[const.GROUP_HIDDEN],
        admin=document[const.GROUP_ADMIN],
        group_id=document[const.ID_KEY]
    )


def document_to_problem(document: dict) -> model.Problem:
    """
    Creates a problem instance from a document

    :param document: The document to create an instance from
    :return: The matching problem instance
    """
    return model.Problem(
        name=document[const.PROBLEM_NAME],
        difficulty=document[const.PROBLEM_DIFFICULTY],
        description=document[const.PROBLEM_DESCRIPTION],
        points=document[const.PROBLEM_POINTS],
        answer=document[const.PROBLEM_ANSWER],
        hint=document[const.PROBLEM_HINT],
        problem_id=document[const.ID_KEY]
    )

##
# Dataclasses to documents:
##

