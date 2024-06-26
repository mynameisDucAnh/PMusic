import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecret')
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:112233@localhost/ungdungamnhac'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
