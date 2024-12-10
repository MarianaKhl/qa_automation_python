#!/bin/bash

# Set base directory
BASE_DIR=$(dirname "$0")

# Log start of the process
echo "Starting test execution..."

# Clearing previous results
echo "Clearing previous test results..."
rm -rf "${BASE_DIR}/allure-results/*"

# Run tests
echo "Running tests with pytest..."
pytest --alluredir="${BASE_DIR}/allure-results"

# Check if tests passed successfully
if [ $? -ne 0 ]; then
  echo "ERROR: Tests failed. Please check the output for more details."
  exit 1
fi

# Log completion
echo "Tests completed successfully."

# Exit script
exit 0
