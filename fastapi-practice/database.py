from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#create_engine use for create a connection to the database
#sessionmake - it is a factory that creates database "sessions"
#declarative_base - used for define the table as python class

# SQLite was designed assuming one connection = one thread, for safety. It physically checks: "which thread opened this connection?" and refuses to let any other thread use it. This isn't a performance setting — it's a rule enforced by the SQLite C library itself.
# Without check_same_thread: False, SQLite would throw this error the moment Thread 1 or Thread 2 tries to use that connection:


# It tells SQLite: "Skip that thread-ownership check — trust SQLAlchemy to manage access safely instead." SQLAlchemy's connection pooling handles the actual safety (making sure two threads don't corrupt the same connection simultaneously), so disabling SQLite's own check is safe in this specific FastAPI + SQLAlchemy setup.

# sqlite3.ProgrammingError: SQLite objects created in a thread can only 
# be used in that same thread.

SQLALCHEMY_DATABASE_URL = "sqlite:///./items.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
