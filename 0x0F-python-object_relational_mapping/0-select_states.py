#!/usr/bin/python3
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace these values with your MySQL connection details
DB_USER = 'root'
DB_PASSWORD = 'root'
DB_HOST = 'localhost'
DB_PORT = '3306'
DB_NAME = 'my_db'

# Create a SQLAlchemy engine
engine = create_engine(f'mysql+mysqldb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}', pool_pre_ping=True)


# Declare a base for declarative class definitions
Base = declarative_base()

# Define your State class
class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, Sequence('state_id_seq'), primary_key=True)
    name = Column(String(256), nullable=False)

# Create the table
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Perform the query
for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))

# Close the session
session.close()

