import pytest
from app.db_helper import DatabaseHelper

DB_SETTINGS = {
    'dbname': 'student_db',
    'user': 'shop_marry',
    'password': '123',
    'host': 'localhost',
    'port': 5432
}

db_helper = DatabaseHelper(DB_SETTINGS)


@pytest.fixture(scope="module")
def setup_database():
    db_helper.create_database('student_db')
    db_helper.connect_to_db()
    db_helper.create_table('courses')
    db_helper.create_table('students')
    db_helper.create_table('enrollments')

    yield db_helper

    db_helper.close()


def test_courses(setup_database):
    course_id = setup_database.insert_course("Python Programming")
    assert course_id is not None, "Course not inserted"

    setup_database.update_course(course_id, "Advanced Python Programming")

    course = setup_database.select_course_by_name("Advanced Python Programming")
    assert course is not None, "Could not find course after update."
    assert course[1] == "Advanced Python Programming", "The course name does not match."

    setup_database.delete_course("Advanced Python Programming")
    deleted_course = setup_database.select_course_by_name("Advanced Python Programming")
    assert deleted_course is None, "The course was not deleted."


def test_students(setup_database):
    student_id = setup_database.insert_student("John Doe")
    assert student_id is not None, "Student was not inserted."

    setup_database.update_student(student_id, "John Smith")

    student = setup_database.select_student_by_name("John Smith")
    assert student is not None, "Unable to find student after update."
    assert student[1] == "John Smith", "Student name does not match."

    setup_database.delete_student("John Smith")
    deleted_student = setup_database.select_student_by_name("John Smith")
    assert deleted_student is None, "The student was not removed."


def test_enrollments(setup_database):
    course_id = setup_database.insert_course("Java Programming")
    student_id = setup_database.insert_student("Tim Smith")

    setup_database.enroll_student(student_id, course_id)
    enrollments = setup_database.get_enrollments_by_student(student_id)
    assert len(enrollments) > 0, "Student not enrolled in course."
    assert enrollments[0][1] == student_id, "Student ID does not match record."

    setup_database.delete_enrollment(student_id, course_id)
    updated_enrollments = setup_database.get_enrollments_by_student(student_id)
    assert len(updated_enrollments) == 0, "The student was not removed from enrollments."


if __name__ == "__main__":
    pytest.main()
