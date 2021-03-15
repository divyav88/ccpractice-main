
# entities\databaseSessionManager.py
import json
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

workingDirectory = os.getcwd()
configFile = os.path.join(workingDirectory, 'config.json')



with open(configFile, 'r') as jsonConfig:
    config = json.load(jsonConfig)

DATABASE_CONNECTION = config['database_connection_string']
engine = create_engine(DATABASE_CONNECTION, echo=True)

# create a Session
Session = sessionmaker(bind=engine)

class SessionManager(object):
    def __init__(self):
        self.session = Session()