import pytest
from sqlalchemy.exc import IntegrityError
from models import Student


class TestStudents:
    """Тесты для работы со студентами"""

    def test_create_student(self, db_session):
        """Тест на добавление студента"""
        student = Student(
            name="John Doe",
            email="john@example.com"
        )
        db_session.add(student)
        db_session.commit()

        saved_student = db_session.query(Student).filter_by(
            email="john@example.com"
        ).first()
        assert saved_student is not None
        assert saved_student.name == "John Doe"
        assert saved_student.email == "john@example.com"

        db_session.delete(saved_student)
        db_session.commit()

    def test_update_student(self, db_session, sample_student):
        """Тест на изменение студента"""
        sample_student.name = "Updated Name"
        db_session.commit()

        updated = db_session.query(Student).filter_by(
            id=sample_student.id
        ).first()
        assert updated.name == "Updated Name"

    def test_delete_student(self, db_session):
        """Тест на удаление студента"""
        student = Student(
            name="To Delete",
            email="delete@example.com"
        )
        db_session.add(student)
        db_session.commit()

        student_id = student.id

        db_session.delete(student)
        db_session.commit()

        deleted = db_session.query(Student).filter_by(
            id=student_id
        ).first()
        assert deleted is None

    def test_unique_email_constraint(self, db_session, sample_student):
        """Негативный тест: попытка добавить студента
        с существующим email"""
        duplicate = Student(
            name="Another",
            email=sample_student.email
        )

        with pytest.raises(IntegrityError):
            db_session.add(duplicate)
            db_session.commit()
        db_session.rollback()

    def test_read_student(self, db_session, sample_student):
        """Тест на чтение студента"""
        found = db_session.query(Student).filter_by(
            id=sample_student.id
        ).first()
        assert found is not None
        assert found.name == sample_student.name
        assert found.email == sample_student.email
