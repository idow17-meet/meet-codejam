from typing import List
from dataclasses import dataclass


@dataclass
class Group:
    name: str
    members: List[str]
    password: str
    hidden: bool = False
    admin: bool = False
    group_id: str = None


@dataclass
class Problem:
    name: str
    difficulty: int
    description: str
    points: float
    answer: str
    hint: str = None
    problem_id: str = None


@dataclass
class Score:
    group_id: str
    problem_id: str
    current_points: float = 0
    submitted_answer: str = None
    submitted_code: str = None
    hint_used: bool = False
    score_id: str = None


GroupList = List[Group]
ProblemList = List[Problem]
ScoreList = List[Score]
