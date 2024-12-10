#!/bin/bash

# Set base directory
BASE_DIR=$(dirname "$0")

# Log start of the process
echo "Starting test execution and report generation..."

# Clearing previous results
echo "Clearing previous test results..."
rm -rf "${BASE_DIR}/allure-results/*"
rm -rf "${BASE_DIR}/allure-report/*"

# Run tests
echo "Running tests with pytest..."
pytest --alluredir="${BASE_DIR}/allure-results"

# Check if Allure results exist
if [ ! -d "${BASE_DIR}/allure-results" ] || [ -z "$(ls -A ${BASE_DIR}/allure-results)" ]; then
  echo "ERROR: No Allure results found. Tests may have failed or produced no output."
  exit 1
fi

# Generate Allure report
echo "Generating Allure report..."
allure generate "${BASE_DIR}/allure-results" -o "${BASE_DIR}/allure-report" --clean

# Log completion
echo "Allure report generated successfully in ${BASE_DIR}/allure-report."

# Exit script
exit 0
