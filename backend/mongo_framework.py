from pymongo import MongoClient
from hashlib import sha512
from backend.db_framework import CodejamDB
import backend.mongo_consts as const


class MongoCodejamDB(CodejamDB):
    """
    Codejam database operations using MongoDB
    """

    def __init__(self, database_uri: str):
        """
        :param database_uri: The database's connection URI
        """

        self.client = MongoClient(database_uri)
        self.db = self.client[const.DATABASE_NAME]
        self.problems = self.db[const.PROBLEM_COLLECTION]
        self.groups = self.db[const.GROUP_COLLECTION]
        self.scores = self.db[const.SCORE_COLLECTION]

        # Replace this with an environment variable
        self.__password_salt = 'b32197fwqgfFWEIO014jfx-a?'

    def __hash_password(self, password: str) -> str:
        """
        Hashes the password using sha512
        :param password:
        :return:
        """
        return sha512(password.encode() + self.__password_salt.encode()).hexdigest()

    def is_correct_login(self, username: str, password: str) -> bool:
        pass

    def get_group_scores(self, group_id: str):
        pass

    def get_group_score(self, group_id: str, problem_id: str):
        pass

    def create_group(self, group_name: str, members: list, password: str):
        """
        Creates the group in the database, including adding score records

        :param group_name: The group's name
        :param members: The group's members (list of names)
        :param password: The group's password
        """

        new_group = {
            const.GROUP_NAME: group_name,
            const.GROUP_MEMBERS: members,
            const.GROUP_PASSWORD: self.__hash_password(password)
        }

        self.groups.insert_one(new_group)
