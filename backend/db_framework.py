from abc import ABC, abstractmethod


"""
Database layout:

Table: Problems
name | difficulty | description | hint | score | answer

Table: Groups
name | members | password

Table: Scores
group_id | group (relationship) | problem_id | problem (relationship) | submitted_answer | submitted_code | score | hint_used
"""


class CodejamDB(ABC):
    """
    Defines the database interface in order to allow modularity
    """

    @abstractmethod
    def is_correct_login(self, username: str, password: str) -> bool:
        """
        Verifies that the given login is correct

        :param username: The user's login name
        :param password: The user's password
        :return: True if the given username and password match a record in the database
        """
        pass

    @abstractmethod
    def get_group_scores(self, group_id: str):
        """
        Gets the group's entire score list

        :param group_id: Group's unique identifier
        """
        pass

    @abstractmethod
    def get_group_score(self, group_id: str, problem_id: str):
        """
        Gets the group's score entity

        :param group_id: The group's ID
        :param problem_id: The problem's ID
        """
        pass

    @abstractmethod
    def create_group(self, group_name: str, members: list, password: str):
        """
        Creates the group in the database, including adding score records

        :param group_name: The group's name
        :param members: The group's members (list of names)
        :param password: The group's password
        """
        pass
