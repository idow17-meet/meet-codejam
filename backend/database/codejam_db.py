"""
Defines the database interface in order to allow modularity
"""

from abc import ABC, abstractmethod
from typing import Dict, List

import backend.database.model as model


class CodejamDB(ABC):
    """
    DB Operations interface
    """

    @abstractmethod
    def add_group(self, group: model.InGroup):
        """
        Adds the group in the database, including adding score records. Sets the group instance's group_id

        :param group: The group to add
        """
        pass

    @abstractmethod
    def get_group(self, group_name: str) -> model.DBGroup:
        """
        Retrieves a group using its name / ID

        :param group_name: Group's name or ID (name converted to ID)
        :return: The corresponding group
        """
        pass

    @abstractmethod
    def get_all_groups(self) -> model.GroupList:
        """
        Retrieves the entire group list

        :return: List containing all group objects in the database
        """
        pass

    @abstractmethod
    def edit_group(self, group_name: str, updated_group: model.InGroup):
        """
        Modify an existing group

        :param group_name: Group's name or ID (name converted to ID)
        :param updated_group: The modified group
        """
        pass

    @abstractmethod
    def delete_group(self, group_name: str):
        """
        Deletes a group using its name / ID

        :param group_name: Group's name or ID (name converted to ID)
        """

    @abstractmethod
    def add_problem(self, problem: model.Problem):
        """
        Add a problem / question for the codejam, while creating the appropriate score instances for each group.
        Sets the problem instance's problem_id

        :param problem: The problem to add
        """
        pass

    @abstractmethod
    def get_problem(self, problem_name: str) -> model.Problem:
        """
        Retrieves a problem using its name / ID

        :param problem_name: Problem's name or ID (name converted to ID)
        :return: The corresponding group
        """
        pass

    @abstractmethod
    def get_all_problems(self) -> model.ProblemList:
        """
        Retrieves the entire problem list

        :return: List containing all problem objects in the database
        """
        pass

    @abstractmethod
    def edit_problem(self, problem_name: str, updated_problem: model.Problem):
        """
        Modify an existing problem

        :param problem_name: Problem's name or ID (name converted to ID)
        :param updated_problem: The modified problem
        """
        pass

    @abstractmethod
    def delete_problem(self, problem_name: str):
        """
        Deletes a problem using its name / ID

        :param problem_name: Problem's name or ID (name converted to ID)
        """
        pass

    @abstractmethod
    def add_score(self, score: model.DBScore):
        """
        Adds a score instance of the given problem for the given group

        :param score: The score to add
        """
        pass

    @abstractmethod
    def get_group_scores(self, group_name: str) -> model.ScoreList:
        """
        Gets the group's entire score list

        :param group_name: Group's name or ID (name converted to ID)
        """
        pass

    @abstractmethod
    def get_group_score(self, group_name: str, problem_id: str) -> model.DBScore:
        """
        Gets the group's score entity

        :param group_name: Group's name or ID (name converted to ID)
        :param problem_id: The problem's ID
        """
        pass

    @abstractmethod
    def get_all_scores(self, solved_only: bool = False, excluded_groups: List[str] = None) \
            -> Dict[str, model.ScoreList]:
        """
        Retrieves all of the scores in the database

        :param solved_only: Whether only solved scores (points above 0) should be included, defaults to False
        :param excluded_groups: A list of group names to exclude from the query, such as the current user
        :return: A dictionary that maps group IDS to a list of their scores
        """
        pass

    # The following may not be needed:
    # Added in case manual changes are required (disqualifying an answer, etc)
    @abstractmethod
    def edit_score(self, group_name: str, problem_name: str, updated_score: model.DBScore):
        """
        Update an existing score's fields

        :param group_name: Group's name or ID (name converted to ID)
        :param problem_name: Problem's name or ID (name converted to ID)
        :param updated_score: The new score object
        """
        pass

    @abstractmethod
    def submit_answer(self, group_name: str, problem_name: str, answer: str, code: str) -> bool:
        """
        Submit an answer, update accordingly in the DB

        :param group_name: The name / ID of the group submitting
        :param problem_name: The name / ID of the problem
        :param answer: The answer the group is submitting
        :param code: The group's code for the problem, for validation
        :return: True if the answer was correct
        """
        pass

    @abstractmethod
    def use_hint(self, group_name: str, problem_name: str) -> str:
        """
        Gets the hint for the given problem while saving that the group used it

        :param group_name: The group's name / ID
        :param problem_name: The problem's name / ID
        :return: The hint for the problem
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
