import os
from dotenv import load_dotenv
import json

def get_json_start_parameters():
    start_json_file = open(os.environ.get('MILLENIUM_JSON_URI'))
    start_parameters = json.load(start_json_file)
    start_json_file.close()
    return start_parameters

class BaseConfig(object):
    load_dotenv()
    DEBUG = os.environ.get('DEBUG_MOD')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.environ.get('SQLITE_FILE')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # used for encryption and session management
    SECRET_KEY = os.environ.get('SECRET_KEY')
    CORS_ORIGINS = os.getenv('CORS_ORIGINS')
    #load millennium-falcon.json on start
    START_PARAMETERS = get_json_start_parameters()
