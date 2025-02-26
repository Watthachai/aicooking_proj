import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_default_secret_key'  # Use environment variable or a default
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Database configuration using environment variables
    DB_HOST = os.environ.get('DB_HOST', 'db')  # Default to 'db' (Docker Compose service name)
    DB_USER = os.environ.get('DB_USER', 'kmitl_project_user')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', 'kmitl_project') # IMPORTANT: change the default!
    DB_NAME = os.environ.get('DB_NAME', 'kmitl_project_db')

    # Construct the SQLAlchemy database URI
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    )