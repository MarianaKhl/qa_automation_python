#!/bin/bash

# make file executable = chmod +x run_tests.sh
# start run = ./run_tests.sh

# Activate virtual environment
source venv/bin/activate

# clearing previous results
echo "Clearing previous test results..."
rm -rf allure-results/*
rm -rf allure-report/*

# start tests
echo "Running tests..."
pytest --alluredir=allure-results

# generation report
echo "Generating Allure report..."
allure generate allure-results -o allure-report --clean

# open report
echo "Opening Allure report..."
allure open allure-report
