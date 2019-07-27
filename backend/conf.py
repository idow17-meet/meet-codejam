"""
Might be worth implementing a JSON configuration
"""

# Environment Variables
ENV_DATABASE_URI = "CODEJAM_DB_URI"
ENV_SECRET_KEY = "CODEJAM_SECRET_KEY"
ENV_PASSWORD_SALT = "CODEJAM_PASSWORD_SALT"


# Cookie 'expire' field in days
COOKIE_EXPIRATION_DEFAULT = {"days": 365 * 2}  # Two years
JWT_ALGORITHM = "HS256"
