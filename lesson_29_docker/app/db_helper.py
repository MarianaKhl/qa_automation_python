import os
import psycopg2
from dotenv import load_dotenv
import logging
from urllib.parse import urlparse

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://shop_marry:123@localhost/students_db')

class DatabaseHelper:
    def __init__(self, db_settings=None):
        self.db_settings = db_settings or self._parse_db_url(DATABASE_URL)
        self.connection = None
        self.cursor = None

    def _parse_db_url(self, db_url):
        parsed_url = urlparse(db_url)
        return {
            'dbname': parsed_url.path[1:],
            'user': parsed_url.username,
            'password': parsed_url.password,
            'host': parsed_url.hostname,
            'port': parsed_url.port or 5432,
        }

    def connect_to_db(self):
        try:
            self.connection = psycopg2.connect(**self.db_settings)
            self.cursor = self.connection.cursor()
            print("Connected to the database.")
        except Exception as e:
            print(f"Error connecting to the database: {e}")

    def create_database(self, db_name):
        admin_db_settings = {**self.db_settings, 'dbname': 'postgres'}
        try:
            admin_connection = psycopg2.connect(**admin_db_settings)
            admin_connection.autocommit = True
            admin_cursor = admin_connection.cursor()

            admin_cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{db_name}';")
            if admin_cursor.fetchone() is None:
                print(f"Database {db_name} does not exist. Creating...")
                admin_cursor.execute(f"CREATE DATABASE {db_name};")
                print(f"Database {db_name} created.")
            admin_cursor.close()
            admin_connection.close()
        except Exception as e:
            print(f"Error creating database: {e}")

    def create_table(self, table_name):
        if self.connection is None or self.cursor is None:
            self.connect_to_db()

        create_statements = {
            "courses": '''
                CREATE TABLE IF NOT EXISTS courses (
                    id SERIAL PRIMARY KEY,
                    course_name VARCHAR(255) NOT NULL
                );
            ''',
            "students": '''
                CREATE TABLE IF NOT EXISTS students (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL
                );
            ''',
            "enrollments": '''
                CREATE TABLE IF NOT EXISTS enrollments (
                    id SERIAL PRIMARY KEY,
                    student_id INT REFERENCES students(id),
                    course_id INT REFERENCES courses(id)
                );
            '''
        }
        if table_name in create_statements:
            self.cursor.execute(create_statements[table_name])
            self.connection.commit()
            print(f"Table {table_name} created.")

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Database connection closed.")

    def check_table_exists(self, table_name):
        self.cursor.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = '{table_name}');")
        exists = self.cursor.fetchone()[0]
        return exists

    def get_table_columns(self, table_name):
        self.cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}';")
        columns = self.cursor.fetchall()
        return columns

    def insert_course(self, course_name):
        self.cursor.execute("INSERT INTO courses (course_name) VALUES (%s) RETURNING id;", (course_name,))
        course_id = self.cursor.fetchone()[0]
        self.connection.commit()
        logging.info(f"Inserted course with ID: {course_id}")
        return course_id

    def update_course(self, course_id, new_name):
        self.cursor.execute("UPDATE courses SET course_name = %s WHERE id = %s;", (new_name, course_id))
        self.connection.commit()
        logging.info(f"Updated course ID {course_id} to {new_name}.")

    def select_course_by_name(self, course_name):
        self.cursor.execute("SELECT * FROM courses WHERE course_name = %s;", (course_name,))
        return self.cursor.fetchone()

    def delete_course(self, course_name):
        self.cursor.execute("DELETE FROM courses WHERE course_name = %s;", (course_name,))
        self.connection.commit()
        logging.info(f"Deleted course: {course_name}")

    def insert_student(self, student_name):
        self.cursor.execute("INSERT INTO students (name) VALUES (%s) RETURNING id;", (student_name,))
        student_id = self.cursor.fetchone()[0]
        self.connection.commit()
        logging.info(f"Inserted student with ID: {student_id}")
        return student_id

    def update_student(self, student_id, new_name):
        self.cursor.execute("UPDATE students SET name = %s WHERE id = %s;", (new_name, student_id))
        self.connection.commit()
        logging.info(f"Updated student ID {student_id} to {new_name}.")

    def select_student_by_name(self, student_name):
        self.cursor.execute("SELECT * FROM students WHERE name = %s;", (student_name,))
        return self.cursor.fetchone()

    def delete_student(self, student_name):
        self.cursor.execute("DELETE FROM students WHERE name = %s;", (student_name,))
        self.connection.commit()
        logging.info(f"Deleted student: {student_name}")

    def enroll_student(self, student_id, course_id):
        self.cursor.execute("INSERT INTO enrollments (student_id, course_id) VALUES (%s, %s);", (student_id, course_id))
        self.connection.commit()
        logging.info(f"Enrolled student ID {student_id} in course ID {course_id}.")

    def delete_enrollment(self, student_id, course_id):
        self.cursor.execute("DELETE FROM enrollments WHERE student_id = %s AND course_id = %s;", (student_id, course_id))
        self.connection.commit()
        logging.info(f"Deleted enrollment for student ID {student_id} and course ID {course_id}.")

    def get_enrollments_by_student(self, student_id):
        self.cursor.execute("SELECT * FROM enrollments WHERE student_id = %s;", (student_id,))
        return self.cursor.fetchall()
