import os
import psycopg2
import pytest
from dotenv import load_dotenv

load_dotenv()

DB_SETTINGS = {
    'dbname': os.getenv('DB_NAME', 'students_db'),
    'user': os.getenv('DB_USER', 'shop_marry'),
    'password': os.getenv('DB_PASSWORD', '123'),
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', 5432),
}

def get_db_connection():
    return psycopg2.connect(**DB_SETTINGS)

@pytest.fixture(scope="module")
def setup_database():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        age INT
    );
    ''')
    conn.commit()

    cursor.execute("INSERT INTO students (name, age) VALUES ('John Doe', 21), ('Jane Doe', 22);")
    conn.commit()

    yield cursor

    cursor.execute('DROP TABLE IF EXISTS students;')
    conn.commit()

    cursor.close()
    conn.close()

def test_table_exists(setup_database):
    setup_database.execute("SELECT to_regclass('public.students');")
    result = setup_database.fetchone()
    assert result[0] == 'students', "Таблиця 'students' не існує"

def test_data_in_table(setup_database):
    setup_database.execute("SELECT COUNT(*) FROM students;")
    result = setup_database.fetchone()
    assert result[0] == 2, "Не знайдено очікуваних записів у таблиці students"
