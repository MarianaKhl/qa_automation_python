from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import random

# PostgreSQL connection options
DATABASE_URL = "postgresql://shop_marry:shop_3@localhost/students_db"

# database initialization
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# relationship table of students and courses (many-to-many)
enrollment_table = Table(
    'enrollments', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    courses = relationship("Course", secondary=enrollment_table, back_populates="students")


class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    course_name = Column(String, nullable=False)
    students = relationship("Student", secondary=enrollment_table, back_populates="courses")

# initialization of the table structure
Base.metadata.create_all(engine)


if session.query(Course).count() == 0:
    course_names = ['Math', 'Physics', 'Chemistry', 'Biology', 'Computer Science']
    courses = [Course(course_name=name) for name in course_names]
    session.add_all(courses)
    session.commit()

# adding students to the database if they do not already exist
if session.query(Student).count() == 0:
    for i in range(1, 21):                    # add 20 students with unique names
        student = Student(name=f"Student {i}")
        student.courses = random.sample(courses, k=random.randint(1, 3))
        session.add(student)
    session.commit()

print("Courses available in the database:")
for course in session.query(Course).all():
    print(f"Course ID: {course.id}, Name: {course.course_name}")

print("\nStudents available in the database:")
for student in session.query(Student).all():
    print(f"Student ID: {student.id}, Name: {student.name}")


# the function of adding a new student to the course
def add_student(name, course_name):
    existing_student = session.query(Student).filter(Student.name == name).first()
    if existing_student is None:
        new_student = Student(name=name)
        course = session.query(Course).filter(Course.course_name == course_name).first()
        if course is None:
            print(f"Course '{course_name}' not found.")
            return
        new_student.courses.append(course)
        session.add(new_student)
        try:
            session.commit()
            print(f"Added {name} to {course.course_name}")
        except Exception as e:
            session.rollback()
            print("Error committing to the database:", e)
    else:
        print(f"Student '{name}' already exists in the database.")


# a function to retrieve students registered for a specific course
def get_students_by_course(course_name):
    course = session.query(Course).filter(Course.course_name == course_name).first()
    if course is None:
        print(f"Course '{course_name}' not found.")
        return []
    students = [student.name for student in course.students]
    return students


# a function to retrieve the courses for which a particular student is registered
def get_courses_by_student(student_name):
    student = session.query(Student).filter(Student.name == student_name).first()
    if student is None:
        print(f"Student '{student_name}' not found.")
        return []
    courses = [course.course_name for course in student.courses]
    return courses


# function for updating the name of the student
def update_student_name(student_id, new_name):
    student = session.query(Student).filter(Student.id == student_id).first()
    if student:
        student.name = new_name
        try:
            session.commit()
            print(f"Updated student ID {student_id} name to {new_name}")
        except Exception as e:
            session.rollback()
            print("Error committing to the database:", e)
    else:
        print(f"Student with ID {student_id} not found.")


def update_student_course(student_name, old_course_name, new_course_name):
    # find a student by name
    student = session.query(Student).filter(Student.name == student_name).first()
    # find the old course and the new course by name
    old_course = session.query(Course).filter(Course.course_name == old_course_name).first()
    new_course = session.query(Course).filter(Course.course_name == new_course_name).first()

    if not student:
        print(f"Student '{student_name}' not found.")
        return
    if not old_course:
        print(f"Old course '{old_course_name}' not found.")
        return
    if not new_course:
        print(f"New course '{new_course_name}' not found.")
        return

    # check whether the student is registered for the old course
    if old_course in student.courses:
        # exchange rate
        student.courses.remove(old_course)
        student.courses.append(new_course)
        try:
            session.commit()
            print(f"Updated course for {student_name}: replaced '{old_course_name}' with '{new_course_name}'")
        except Exception as e:
            session.rollback()
            print("Error committing to the database:", e)
    else:
        print(f"Student '{student_name}' is not enrolled in the course '{old_course_name}'.")


# function to delete a student
def delete_student(student_id):
    student = session.query(Student).filter(Student.id == student_id).first()
    if student:
        session.delete(student)
        try:
            session.commit()
            print(f"Deleted student ID {student_id}")
        except Exception as e:
            session.rollback()
            print("Error committing to the database:", e)
    else:
        print(f"Student with ID {student_id} not found.")


add_student("Student 11", "Physics")
print("Students in Physics:", get_students_by_course("Physics"))
print("Courses of Student 7:", get_courses_by_student("Student 2"))
update_student_name(895, "Student 7")
update_student_name(882, "Student 20")
update_student_course("Student 2", "Physics", "Biology")
#delete_student(2)
session.commit()

