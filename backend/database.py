from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# --------------------------------------------------------
# DATABASE URL - use the 'db' service name inside Docker
# Format: postgresql://username:password@service_name/db_name
# --------------------------------------------------------
SQLALCHEMY_DATABASE_URL = "postgresql://tradex_user:tradex_pass@db:5432/tradex_db"

# Create the engine (the connection to the DB)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a SessionLocal class (each request uses a separate session)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our models (tables) will inherit from this
Base = declarative_base()

# Dependency to get the database session in other files
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
