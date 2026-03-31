from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)


DATABASE_URL = "postgresql://postgres:12345@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


def create_tables():
    """Создаёт таблицу students, если её нет"""
    Base.metadata.create_all(engine)


def get_session():
    """Возвращает сессию для работы с БД"""
    return SessionLocal()
