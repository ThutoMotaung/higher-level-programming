#!/usr/bin/python3
"""
Task 13: deletes all State objects with a name containing the letter a from
the database hbtn_0e_6_usa. You must use the module SQLAlchemy
"""

import sys
import MySQLdb
from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

if __name__ == "__main__":

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                            mysql_username, mysql_password, mysql_dbname, pool_pre_ping=True))

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).filter(
        State.name.ilike("%a%")).delete(synchronize_session='fetch')
    session.commit()

    session.close()