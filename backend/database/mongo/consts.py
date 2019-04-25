"""
Defines constants for the MongoDB framework, such as key names
"""

# DB and collections
DATABASE_NAME = 'meet_codejam'
PROBLEM_COLLECTION = "problems"
GROUP_COLLECTION = "groups"
SCORE_COLLECTION = "scores"

# Group collection
GROUP_NAME = 'name'
GROUP_MEMBERS = 'members'
GROUP_PASSWORD = 'password'
GROUP_HIDDEN = 'hidden'
GROUP_ADMIN = 'admin'

# Problem collection
PROBLEM_NAME = 'name'
PROBLEM_DIFFICULTY = 'difficulty'
PROBLEM_DESCRIPTION = 'description'
PROBLEM_POINTS = 'points'
PROBLEM_ANSWER = 'answer'
PROBLEM_HINT = 'hint'

# Score collection
SCORE_GROUP_ID = 'group_id'
SCORE_PROBLEM_ID = 'problem_id'
SCORE_SUBMITTED_ANSWER = 'submitted_answer'
SCORE_SUBMITTED_CODE = 'submitted_code'
SCORE_CURRENT_POINTS = 'current_points'
SCORE_HINT_USED = 'hint_used'

# General mongo
ID_KEY = '_id'
