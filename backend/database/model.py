from typing import List
from pydantic import BaseModel


class GroupBase(BaseModel):
    name: str
    members: List[str]

    @property
    def group_id(self) -> str:
        return self.name.upper()


class DetailedGroup(GroupBase):
    """ Meant for the admin dashboard """
    hidden: bool = False
    admin: bool = False


class OutGroup(GroupBase):
    """ Meant for responses to normal users """
    pass


class InGroup(DetailedGroup):
    """ Meant for inserting groups to the DB """
    password: str


class DBGroup(DetailedGroup):
    """ Fully detailed group as stored in the DB """
    password: bytes


class Problem(BaseModel):
    name: str
    difficulty: int
    description: str
    points: float
    answer: str
    hint: str = None
    problem_id: str = None


class ScoreBase(BaseModel):
    group_id: str
    problem_id: str
    current_points: float = 0
    hint_used: bool = False


class DBScore(ScoreBase):
    """ Fully detailed score as stored in the DB"""
    submitted_answer: str = None
    submitted_code: str = None
    score_id: str = None


GroupList = List[DBGroup]
ProblemList = List[Problem]
ScoreList = List[DBScore]
