
import os
from dotenv import load_dotenv
load_dotenv()



class BaseConfig(object):
    PROJECT = "dummy"
    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    DEBUG = True
    TESTING = False
    SECRET_KEY = os.getenv('FLASK_SECRET')


class DefaultConfig(BaseConfig):
    DEBUG = True

