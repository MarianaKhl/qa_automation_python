#!/bin/bash

echo "Creating directories for Allure results..."
mkdir -p lesson_31_Jenkins/allure-results
mkdir -p lesson_31_Jenkins/allure-report

echo "Activating virtual environment..."
source venv/bin/activate

echo "Running tests with pytest..."
set +e
pytest --alluredir=lesson_31_Jenkins/allure-results
TEST_EXIT_CODE=$?
set -e

echo "Generating Allure report..."
allure generate lesson_31_Jenkins/allure-results -o lesson_31_Jenkins/allure-report --clean

if [ $TEST_EXIT_CODE -ne 0 ]; then
    echo "Tests failed. Review the Allure report for details."
    exit $TEST_EXIT_CODE
fi

echo "All tests passed successfully."
exit 0
