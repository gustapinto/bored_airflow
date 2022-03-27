from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base


engine = create_engine(getenv('CONNECTION_STRING'))
Base = declarative_base()
