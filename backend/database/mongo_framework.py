from pymongo import MongoClient
from hashlib import sha512
from bson.objectid import ObjectId
import re

import model
from framework import CodejamDB
import mongo_consts as const


class MongoCodejamDB(CodejamDB):
    """
    Codejam database operations using MongoDB
    """

    def __init__(self, database_uri: str):
        """
        :param database_uri: The database's connection URI
        """
        self.__client = MongoClient(database_uri)
        self.__db = self.__client[const.DATABASE_NAME]
        self.__problems = self.__db[const.PROBLEM_COLLECTION]
        self.__groups = self.__db[const.GROUP_COLLECTION]
        self.__scores = self.__db[const.SCORE_COLLECTION]

        # TODO: When deploying, replace this with an environment variable
        self.__password_salt = 'b32197fwqgfFWEIO014jfx-a?'

    @staticmethod
    def __document_to_score(document: dict) -> model.Score:
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

    def __hash_password(self, password: str) -> str:
        """
        Hashes the password using sha512
        :param password:
        :return:
        """
        return sha512(password.encode() + self.__password_salt.encode()).hexdigest()

    def add_group(self, group: model.Group):
        """
        Adds the group in the database, including adding score records. Sets the group instance's group_id

        :param group: The group to add
        """
        if self.__groups.count_documents({const.GROUP_NAME: group.name}) > 0:
            raise ValueError("Group with given name already exists")

        new_group = {
            const.GROUP_NAME: group.name,
            const.GROUP_MEMBERS: group.members,
            const.GROUP_PASSWORD: self.__hash_password(group.password),
            const.GROUP_HIDDEN: group.hidden,
            const.GROUP_ADMIN: group.admin
        }

        # Insert and store the returned mongo-created ID in the dataclass
        result = self.__groups.insert_one(new_group)
        group.group_id = str(result.inserted_id)  # str is required to transform from ObjectId to str

        # Add all score instances for this group
        # Note: Consider generating scores and adding in bulk
        for problem in self.__problems.find():
            problem_id = str(problem[const.ID_KEY])
            self.add_score(model.Score(group.group_id, problem_id))

    def add_problem(self, problem: model.Problem):
        """
        Add a problem / question for the codejam, while creating the appropriate score instances for each group.
        Sets the problem instance's problem_id

        :param problem: The problem to add
        """
        new_problem = {
            const.PROBLEM_NAME: problem.name,
            const.PROBLEM_DIFFICULTY: problem.difficulty,
            const.PROBLEM_DESCRIPTION: problem.description,
            const.PROBLEM_POINTS: problem.points,
            const.PROBLEM_ANSWER: problem.answer
        }

        result = self.__problems.insert_one(new_problem)
        problem.problem_id = str(result.inserted_id)

        # Add score instances for all groups
        for group in self.__groups.find():
            group_id = str(group[const.ID_KEY])
            self.add_score(model.Score(group_id, problem.problem_id))

    def add_score(self, score: model.Score):
        """
        Adds a score instance of the given problem for the given group

        :param score: The score to add
        """
        new_score = {
            const.SCORE_GROUP_ID: ObjectId(score.group_id),
            const.SCORE_PROBLEM_ID: ObjectId(score.problem_id),
            const.SCORE_SUBMITTED_ANSWER: score.submitted_answer,
            const.SCORE_SUBMITTED_CODE: score.submitted_code,
            const.SCORE_CURRENT_POINTS: score.current_points,
            const.SCORE_HINT_USED: score.hint_used
        }

        result = self.__scores.insert_one(new_score)
        score.score_id = str(result.inserted_id)

    def is_correct_login(self, username: str, password: str, *, should_hash: bool = True) -> bool:
        """
        Verifies that the given username and password match a group document

        :param username: The group's display name
        :param password: The group's password
        :param should_hash: Whether or not the given password should be hashed before comparison
        :return: True if the login is correct
        """
        if should_hash:
            password = self.__hash_password(password)

        return self.__groups.count_documents({
            const.GROUP_NAME: re.compile(username, re.IGNORECASE),
            const.GROUP_PASSWORD: password
        }) > 0

    def get_group_scores(self, group_id: str) -> model.ScoreList:
        """
        Gets the group's entire score list

        :param group_id: Group's unique identifier
        """
        score_documents = self.__scores.find({const.SCORE_GROUP_ID: ObjectId(group_id)})
        return [self.__document_to_score(document) for document in score_documents]

    def get_group_score(self, group_id: str, problem_id: str) -> model.Score:
        """
        Get the group's score for the given problem
        :param group_id: The group's ID
        :param problem_id: The problem's ID
        :return: The group's score
        """
        score = self.__scores.find_one({const.SCORE_GROUP_ID: group_id, const.SCORE_PROBLEM_ID: problem_id})
        return self.__document_to_score(score)
