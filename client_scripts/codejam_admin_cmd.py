from cmd import Cmd
from csv import DictReader
import os
import string
import random

from client_scripts.load_db import client, Problem, InGroup


CSV_TITLE = "title"
CSV_PROBLEM = "problem"
CSV_SOLUTION = "solution"
CSV_DIFFICULTY = "difficulty"
CSV_POINTS = "points"
CSV_HINT = "hint"
CSV_PROBLEM_FIELDNAMES = [CSV_TITLE, CSV_PROBLEM, CSV_SOLUTION, CSV_DIFFICULTY, CSV_POINTS, CSV_HINT]

CSV_TIMESTAMP = "Timestamp"
CSV_TEAM_NAME = "Name of Team"
CSV_MEMBERS = "Name of all team members separated by a comma \",\""
CSV_GROUP_FIELDNAMES = [CSV_TIMESTAMP, CSV_TEAM_NAME, CSV_MEMBERS]

PASSWORD_LENGTH = 8


def generate_password() -> str:
    return ''.join(random.sample(string.ascii_uppercase + string.ascii_lowercase + string.digits, PASSWORD_LENGTH))


class CodejamAdminCmd(Cmd):
    """
    Database-Managing scripts for quick CRUD operations
    """

    def __confirm(self, message):
        value = input(f"{message} [N/y]: ")
        confirmed = value.upper() == 'Y'
        if not confirmed:
            print("Cancelled.")
        return confirmed

    def do_load_problems_from_csv(self, csv_path: str):
        """
        Loads a set of problems from a **properly formatted** csv file

        :param csv_path: The path of the csv file to load
        """
        if not os.path.exists(csv_path):
            print("File does not exist.")
            return

        with open(csv_path) as csv_file:
            reader = DictReader(csv_file, fieldnames=CSV_PROBLEM_FIELDNAMES)
            next(reader, None)
            try:
                problems = [Problem(name=row[CSV_TITLE],
                                    difficulty=int(row[CSV_DIFFICULTY]),
                                    description=row[CSV_PROBLEM],
                                    points=float(row[CSV_POINTS]),
                                    answer=row[CSV_SOLUTION],
                                    hint=row[CSV_HINT] if row[CSV_HINT] else None) for row in reader]
                [client.add_problem(problem) for problem in problems]
            except (ValueError, TypeError) as e:
                print(f"Failed to load CSV, please check the format.\nException: {str(e)}")

    def do_add_problem(self, arg):
        """
        Adds a single problem to the database
        """
        title = input("Enter the problem's title: ")
        description = input("Enter the problem's description: ")
        try:
            difficulty = int(input("Enter the problem's difficulty: "))
            points = float(input("Enter the problem's points: "))
        except ValueError:
            print("Not a valid integer / float")
            return
        answer = input("Enter the correct answer: ")
        hint = input("Enter the problem's hint or leave blank: ")
        if hint in ("", "\n"):
            hint = None

        client.add_problem(Problem(name=title,
                                   description=description,
                                   difficulty=difficulty,
                                   points=points,
                                   answer=answer,
                                   hint=hint))
        print("Added successfully")

    def do_delete_all_problems(self, arg):
        """
        Deletes all of the problems in the database
        """
        if self.__confirm("Are you sure you want to delete the entire problem collection?"):
            problems = client.get_all_problems()
            [client.delete_problem(problem.name) for problem in problems]
            print(f"Deleted {len(problems)} problems.")
            return

    def do_delete_problem(self, problem_name: str):
        """
        Deletes a single problem

        :param problem_name: The name of the problem to delete
        """
        if self.__confirm(f'Are you sure you want to delete "{problem_name}"'):
            client.delete_problem(problem_name)
            print("Deleted.")
            return

    def do_add_group(self, arg):
        """
        Adds a group to the database
        """
        name = input("Enter the group's name: ")
        members = input("Enter the group's members separated by a comma: ").split(',')
        password = input("Enter the group's password: ")
        client.add_group(InGroup(name=name, members=members, password=password))

    def do_load_groups_from_csv(self, csv_path: str):
        """
        Loads a set of groups from a **properly formatted** csv file

        :param csv_path: The path of the csv file to load
        """
        if not os.path.exists(csv_path):
            print("File does not exist.")
            return

        with open(csv_path) as csv_file:
            reader = DictReader(csv_file, fieldnames=CSV_GROUP_FIELDNAMES)
            next(reader, None)
            try:
                groups = [InGroup(name=row[CSV_TEAM_NAME],
                                  members=row[CSV_MEMBERS].split(","),
                                  password=generate_password()) for row in reader]
                [client.add_group(group) for group in groups]
                print(f"Groups created, please save their passwords:")
                [print(f"{group.name} -> {group.password}") for group in groups]
            except (ValueError, TypeError) as e:
                print(f"Failed to load CSV, please check the format.\nException: {str(e)}")

    def do_delete_group(self, group_name: str):
        """
        Deletes the given group from the database

        :param group_name: The name of the group to delete
        """
        if self.__confirm(f'Are you sure you want to delete the group "{group_name}"?'):
            client.delete_group(group_name)
            print("Group deleted.")
            return

    def do_reset_group_score(self, group_name):
        """
        Resets a group's score back to 0 in case they cheated / any other reason

        :param group_name: The name of the group to reset a score for
        """
        problem_name = input("Enter the name of the problem to reset: ")

        if self.__confirm(f"Are you sure you want to reset {group_name}'s score for \"{problem_name}\"?"):
            score = client.get_group_score(group_name, problem_name)
            score.current_points = 0
            client.edit_score(group_name, problem_name, score)
            print("Score reset to 0.")
            return

    def do_exit(self, arg):
        """
        Exit the interface
        """
        return True
