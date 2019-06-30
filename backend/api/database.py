from functools import lru_cache
import os

from backend.conf import ENV_DATABASE_URI
from backend.database.codejam_db import CodejamDB
from backend.database.mongo.mongo_codejam_db import MongoCodejamDB


DB_URI = os.environ.get(ENV_DATABASE_URI, 'localhost')
DB_TYPES = {'mongo': MongoCodejamDB}


@lru_cache()  # Cached since this only needs to run once
def get_db_type() -> type(CodejamDB):
    """
    Implemented in order to allow usage of different databases in the future according to the given URI.
    As of now, always returns the MongoDB type.
    :return: A **type** of a DB Client class to use
    """
    return DB_TYPES['mongo']


def get_db() -> CodejamDB:
    """
    Database client getter
    :return: An instance of the database client
    """
    db_type = get_db_type()
    return db_type(DB_URI)

