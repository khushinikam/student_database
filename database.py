import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()


user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
name = os.getenv("DB_NAME")


Database_url = os.getenv("DB_URL")
engine = create_engine(Database_url)

try: 
   
    connection = engine.connect()
    connection.close()
    print("Connection succesful")


except Exception as e:
    print("connection failed")


sessionLocal = sessionmaker(
    bind = engine
)

BaseClass = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally: 
        db.close()
