#!/bin/bash

# Make the file executable: chmod +x run_tests.sh
# Start the run: ./run_tests.sh

# Clearing previous results
rm -rf allure-results/*
rm -rf allure-report/*

# Start tests
pytest --alluredir=allure-results

# Generate the report
allure generate allure-results -o allure-report --clean

# Open the report (in background) and wait for a few seconds
allure open allure-report &
ALLURE_PID=$!

# Wait for a few seconds to ensure the report is opened
sleep 10

# Stop the Allure server
echo "Stopping Allure server..."
kill $ALLURE_PID
