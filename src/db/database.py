from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.config.settings import get_general_settings

# Build the full connection string
DATABASE_URL = (
    get_general_settings().db_connection_string +
    get_general_settings().db_driver  # This should already start with '?driver=...'
)

# Create synchronous SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    echo=False,         # set True for debugging
    pool_pre_ping=True, # auto-reconnect dropped connections
    pool_size=10,       # adjust based on load
    max_overflow=20,    # additional connections beyond pool_size
    future=True
)

# Sync session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Declarative base
Base = declarative_base()


# Dependency to be used with FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
