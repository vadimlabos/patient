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
    echo=False,              # Keep off unless troubleshooting
    pool_pre_ping=True,      # Reconnect dropped connections automatically
    pool_size=25,            # Tune this based on your DB and traffic
    max_overflow=10,         # Allow up to 30 concurrent connections
    pool_timeout=30,         # Seconds to wait before giving up on a connection
    pool_recycle=180,       # Recycle connections after 3 min to avoid stale ones
    future=True
)

# Sync session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=True,
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
