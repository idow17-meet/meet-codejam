"""
Defines translations between mongo's documents and the project's dataclasses
"""

from bson.objectid import ObjectId
import backend.database.model as model
import backend.database.mongo.consts as const


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


def document_to_group(document: dict) -> model.DBGroup:
    """
    Creates a group instance from a document

    :param document: The document to create an instance from
    :return: The matching group instance
    """
    return model.DBGroup(
        name=document[const.GROUP_NAME],
        members=document[const.GROUP_MEMBERS],
        password=document[const.GROUP_PASSWORD],
        hidden=document[const.GROUP_HIDDEN],
        admin=document[const.GROUP_ADMIN],
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


def score_to_document(score: model.Score) -> dict:
    """
    Converts a score instance to a mongo document
    :param score: The score instance to convert
    :return: A mongo document (dictionary)
    """
    document = {
        const.SCORE_GROUP_ID: score.group_id,
        const.SCORE_PROBLEM_ID: score.problem_id,
        const.SCORE_CURRENT_POINTS: score.current_points,
        const.SCORE_SUBMITTED_ANSWER: score.submitted_answer,
        const.SCORE_SUBMITTED_CODE: score.submitted_code,
        const.SCORE_HINT_USED: score.hint_used,
    }

    if score.score_id:
        document.update({const.ID_KEY: ObjectId(score.score_id)})
    return document


def group_to_document(group: model.DBGroup) -> dict:
    """
    Converts a group instance to a mongo document
    :param group: The group instance to convert
    :return: A mongo document (dictionary)
    """
    document = {
        const.GROUP_NAME: group.name,
        const.GROUP_MEMBERS: group.members,
        const.GROUP_PASSWORD: group.password,
        const.GROUP_HIDDEN: group.hidden,
        const.GROUP_ADMIN: group.admin,
        const.ID_KEY: group.name.upper()
    }

    return document


def problem_to_document(problem: model.Problem) -> dict:
    """
    Converts a problem instance to a mongo document
    :param problem: The problem instance to convert
    :return: A mongo document (dictionary)
    """
    document = {
        const.PROBLEM_NAME: problem.name,
        const.PROBLEM_DIFFICULTY: problem.difficulty,
        const.PROBLEM_DESCRIPTION: problem.description,
        const.PROBLEM_POINTS: problem.points,
        const.PROBLEM_ANSWER: problem.answer,
        const.PROBLEM_HINT: problem.hint,
        const.ID_KEY: problem.name.upper()
    }

    return document
