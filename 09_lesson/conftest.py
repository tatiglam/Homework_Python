import pytest
from models import get_session, create_tables, Student


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    """Создаёт таблицы перед тестами"""
    create_tables()
    yield
    # Очистка после тестов (опционально)
    session = get_session()
    session.query(Student).delete()
    session.commit()
    session.close()


@pytest.fixture
def db_session():
    """Фикстура для сессии БД"""
    session = get_session()
    yield session
    session.rollback()
    session.close()


@pytest.fixture
def sample_student(db_session):
    """Создаёт тестового студента и удаляет после теста"""
    student = Student(name="Test Student", email="test@example.com")
    db_session.add(student)
    db_session.commit()
    yield student
    db_session.delete(student)
    db_session.commit()
