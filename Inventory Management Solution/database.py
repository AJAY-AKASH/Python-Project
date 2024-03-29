from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Configure the PostgreSQL database connection
engine = create_engine("postgresql://postgres:20Pds819@localhost/stock?port=5432")
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

# Initialize the database
def init_db():
    import models
    Base.metadata.create_all(bind=engine)

# Call the init_db() function to create the tables

