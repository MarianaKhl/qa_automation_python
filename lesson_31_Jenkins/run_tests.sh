#!/bin/bash

# make file executable = chmod +x run_tests.sh
# start run = ./run_tests.sh

# clearing previous results
rm -rf allure-results/*
rm -rf allure-report/*

# start tests
pytest --alluredir=allure-results

# generation report
allure generate allure-results -o allure-report --clean

# open report
allure open allure-report

exit 0

