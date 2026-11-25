from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Encoded '@' as '%40' in the password
url = "mysql+pymysql://root:Ritesh%402811@localhost:3306/db"

engine = create_engine(url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
