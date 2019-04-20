"""
Defines the database interface in order to allow modularity
"""

from abc import ABC, abstractmethod
import backend.database.model as model


class CodejamDB(ABC):
    """
    DB Operations interface
    """

    @abstractmethod
    def add_group(self, group: model.Group):
        """
        Adds the group in the database, including adding score records. Sets the group instance's group_id

        :param group: The group to add
        """
        pass

    @abstractmethod
    def add_problem(self, problem: model.Problem):
        """
        Add a problem / question for the codejam, while creating the appropriate score instances for each group.
        Sets the problem instance's problem_id

        :param problem: The problem to add
        """
        pass

    @abstractmethod
    def add_score(self, score: model.Score):
        """
        Adds a score instance of the given problem for the given group

        :param score: The score to add
        """
        pass

    @abstractmethod
    def is_correct_login(self, username: str, password: str, *, should_hash: bool = True) -> bool:
        """
        Verifies that the given username and password are correct

        :param username: The group's display name
        :param password: The group's password
        :param should_hash: Whether or not the given password should be hashed before comparison
        :return: True if the login is correct
        """
        pass

    @abstractmethod
    def get_group_scores(self, group_id: str) -> model.ScoreList:
        """
        Gets the group's entire score list

        :param group_id: Group's unique identifier
        """
        pass

    @abstractmethod
    def get_group_score(self, group_id: str, problem_id: str) -> model.Score:
        """
        Gets the group's score entity

        :param group_id: The group's ID
        :param problem_id: The problem's ID
        """
        pass
