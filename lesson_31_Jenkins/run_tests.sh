#!/bin/bash

BASE_DIR=$(cd "$(dirname "$0")"; pwd)
ALLURE_RESULTS_DIR="$BASE_DIR/allure-results"
ALLURE_REPORT_DIR="$BASE_DIR/allure-report"

echo "Base directory: $BASE_DIR"

mkdir -p "$ALLURE_RESULTS_DIR"
mkdir -p "$ALLURE_REPORT_DIR"

echo "Clearing previous results..."
rm -rf "$ALLURE_RESULTS_DIR/*"
rm -rf "$ALLURE_REPORT_DIR/*"

echo "Running tests with pytest..."
pytest --alluredir="$ALLURE_RESULTS_DIR"
if [ $? -ne 0 ]; then
    echo "ERROR: Tests failed. Check the output for more details."
    exit 1
fi

echo "Generating Allure report..."
allure generate "$ALLURE_RESULTS_DIR" -o "$ALLURE_REPORT_DIR" --clean
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to generate Allure report."
    exit 1
fi

echo "Allure report successfully generated in $ALLURE_REPORT_DIR."

JENKINS_OUTPUT_DIR="$WORKSPACE/allure-report"
echo "Copying Allure report to Jenkins workspace: $JENKINS_OUTPUT_DIR"
mkdir -p "$JENKINS_OUTPUT_DIR"
cp -r "$ALLURE_REPORT_DIR/"* "$JENKINS_OUTPUT_DIR/"

echo "Test execution and report generation completed successfully."
exit 0

