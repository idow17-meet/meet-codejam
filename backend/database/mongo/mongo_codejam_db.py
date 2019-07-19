"""
Defines the MongoDB client wrapper for codejam operations.

Important note about the _id fields in each collection:

In the scores collection it is kept as is (generated by mongo) and therefore must be wrapped in
'ObjectId' when querying.

In the groups and problems collections however, the _id key is inserted at creation as an uppercase
version of the group / problem's name (since the name is unique, and this makes operations easier)
"""
from typing import List, Dict

from pymongo import MongoClient
from hashlib import sha512

import backend.database.model as model
from backend.database.codejam_db import CodejamDB
import backend.database.mongo.consts as const
import backend.database.mongo.translations as trans


class MongoCodejamDB(CodejamDB):
    """
    Codejam database operations using MongoDB
    """

    # TODO: Make this adjustable
    HINT_USED_PERCENTAGE = 0.5

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

    def __hash_password(self, password: str) -> bytes:
        return sha512(password.encode() + self.__password_salt.encode()).digest()

    def add_group(self, group: model.InGroup):
        if self.__groups.count_documents({const.ID_KEY: group.name.upper()}) > 0:
            raise ValueError("Group with given name already exists")

        group_dict = group.dict()
        group_dict[const.GROUP_PASSWORD] = self.__hash_password(group_dict[const.GROUP_PASSWORD])
        db_group = model.DBGroup(**group_dict)
        new_group = trans.group_to_document(db_group)

        # Insert and store the returned mongo-created ID in the dataclass
        self.__groups.insert_one(new_group)

        # Add all score instances for this group
        # Note: Consider generating scores and adding in bulk
        for problem in self.__problems.find():
            problem_id = str(problem[const.ID_KEY])
            self.add_score(model.DBScore(group_id=group.group_id, problem_id=problem_id))

    def get_group(self, group_name: str) -> model.DBGroup:
        document = self.__groups.find_one({const.ID_KEY: group_name.upper()})
        if document:
            return trans.document_to_group(document)

    def get_all_groups(self) -> model.GroupList:
        return [trans.document_to_group(document) for document in self.__groups.find()]

    def edit_group(self, group_name: str, updated_group: model.DBGroup):
        updated_document = trans.group_to_document(updated_group)

        self.__groups.remove({const.ID_KEY: group_name.upper()})
        self.__groups.insert_one(updated_document)
        if updated_group.name != group_name:
            self.__scores.update_many({const.SCORE_GROUP_ID: group_name.upper()},
                                      {"$set": {const.SCORE_GROUP_ID: updated_group.name.upper()}})

    def delete_group(self, group_name: str):
        self.__groups.remove({const.ID_KEY: group_name.upper()})
        self.__scores.remove({const.SCORE_GROUP_ID: group_name.upper()})

    def add_problem(self, problem: model.Problem):
        if self.__problems.count_documents({const.ID_KEY: problem.name.upper()}) > 0:
            raise ValueError("Problem with given name already exists")

        new_problem = trans.problem_to_document(problem)
        result = self.__problems.insert_one(new_problem)
        problem.problem_id = result.inserted_id

        # Add score instances for all groups
        for group in self.__groups.find():
            group_id = group[const.ID_KEY]
            self.add_score(model.DBScore(group_id=group_id, problem_id=problem.problem_id))

    def get_problem(self, problem_name: str) -> model.Problem:
        document = self.__problems.find_one({const.ID_KEY: problem_name.upper()})
        if document:
            return trans.document_to_problem(document)

    def get_all_problems(self) -> model.ProblemList:
        return [trans.document_to_problem(document) for document in self.__problems.find()]

    def edit_problem(self, problem_name: str, updated_problem: model.Problem):
        updated_document = trans.problem_to_document(updated_problem)

        self.__problems.remove({const.ID_KEY: problem_name.upper()})
        self.__problems.insert_one(updated_document)
        if updated_problem.name != problem_name:
            self.__scores.update_many({const.SCORE_PROBLEM_ID: problem_name.upper()},
                                      {"$set": {const.SCORE_PROBLEM_ID: updated_problem.name.upper()}})

    def delete_problem(self, problem_name: str):
        self.__problems.remove({const.ID_KEY: problem_name.upper()})
        self.__scores.remove({const.SCORE_PROBLEM_ID: problem_name.upper()})

    def add_score(self, score: model.DBScore):
        new_score = trans.score_to_document(score)
        result = self.__scores.insert_one(new_score)
        score.score_id = str(result.inserted_id)

    def get_group_score(self, group_name: str, problem_name: str) -> model.DBScore:
        score = self.__scores.find_one({const.SCORE_GROUP_ID: group_name.upper(),
                                        const.SCORE_PROBLEM_ID: problem_name.upper()})
        if score:
            return trans.document_to_score(score)

    def get_group_scores(self, group_name: str) -> model.ScoreList:
        score_documents = self.__scores.find({const.SCORE_GROUP_ID: group_name.upper()})
        return [trans.document_to_score(document) for document in score_documents]

    def get_all_scores(self, solved_only: bool = False, excluded_groups: List[str] = None, problem_name: str = None) \
            -> Dict[str, model.ScoreList]:
        if not excluded_groups:
            excluded_groups = []
        excluded_groups = [group_name.upper() for group_name in excluded_groups]

        query = {const.SCORE_GROUP_ID: {"$nin": excluded_groups}}

        if problem_name:
            query.update({const.SCORE_PROBLEM_ID: problem_name.upper()})

        if solved_only:
            query.update({const.SCORE_CURRENT_POINTS: {"$gt": 0}})

        group = {const.ID_KEY: f'${const.SCORE_GROUP_ID}',
                 const.SCORES_AGGREGATION: {"$push": "$$ROOT"}}

        results = [result for result in self.__scores.aggregate([{"$match": query}, {"$group": group}])]
        raw_mapping = {aggregation[const.ID_KEY]: aggregation[const.SCORES_AGGREGATION] for aggregation in results}
        return {group_id: [trans.document_to_score(raw_score) for raw_score in raw_mapping[group_id]]
                for group_id in raw_mapping}

    def edit_score(self, group_name: str, problem_name: str, updated_score: model.DBScore):
        updated_document = trans.score_to_document(updated_score)

        self.__scores.replace_one({const.SCORE_GROUP_ID: group_name.upper(),
                                   const.SCORE_PROBLEM_ID: problem_name.upper()},
                                  updated_document)

    def submit_answer(self, group_name: str, problem_name: str, answer: str, code: str) -> bool:
        problem = trans.document_to_problem(self.__problems.find_one({const.ID_KEY: problem_name.upper()}))
        score = trans.document_to_score(self.__scores.find_one({const.SCORE_GROUP_ID: group_name.upper(),
                                                                const.SCORE_PROBLEM_ID: problem_name.upper()}))
        correct_answer = problem.answer == answer
        points = problem.points if correct_answer else 0
        if score.hint_used:
            points *= self.HINT_USED_PERCENTAGE

        # TODO: Change scores to support submission list instead of most recent
        score.current_points = points
        score.submitted_answer = answer
        score.submitted_code = code

        self.__scores.replace_one({const.SCORE_GROUP_ID: group_name.upper(),
                                  const.SCORE_PROBLEM_ID: problem_name.upper()},
                                  trans.score_to_document(score))
        return correct_answer

    def use_hint(self, group_name: str, problem_name: str) -> str:
        hint = self.__problems.find_one({const.ID_KEY: problem_name.upper()},
                                        {const.PROBLEM_HINT: True})[const.PROBLEM_HINT]

        if hint:
            self.__scores.update_one({const.SCORE_GROUP_ID: group_name.upper(),
                                      const.SCORE_PROBLEM_ID: problem_name.upper()},
                                     {"$set": {const.SCORE_HINT_USED: True}})
        return hint

    def is_correct_login(self, username: str, password: str, *, should_hash: bool = True) -> bool:
        if should_hash:
            password = self.__hash_password(password)

        return self.__groups.count_documents({
            const.ID_KEY: username.upper(),
            const.GROUP_PASSWORD: password
        }) > 0
