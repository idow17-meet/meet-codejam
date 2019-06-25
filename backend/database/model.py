from typing import List
from pydantic import BaseModel


class GroupBase(BaseModel):
    name: str
    members: List[str]

    @property
    def group_id(self) -> str:
        return self.name.upper()


class DetailedGroup(GroupBase):
    hidden: bool = False
    admin: bool = False


class OutGroup(GroupBase):
    pass


class InGroup(DetailedGroup):
    password: str


class DBGroup(DetailedGroup):
    password: bytes


class Problem(BaseModel):
    name: str
    difficulty: int
    description: str
    points: float
    answer: str
    hint: str = None
    problem_id: str = None


class Score(BaseModel):
    group_id: str
    problem_id: str
    current_points: float = 0
    submitted_answer: str = None
    submitted_code: str = None
    hint_used: bool = False
    score_id: str = None


GroupList = List[DBGroup]
ProblemList = List[Problem]
ScoreList = List[Score]
