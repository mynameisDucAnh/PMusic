import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY =os.environ.get("KEY")
SQLALCHEMY_DATABASE_UR = os.wnviron.get("DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False