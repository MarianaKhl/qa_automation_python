#!/bin/bash


rm -rf allure-results/*
rm -rf allure-report/*

pytest --alluredir=allure-results

allure generate allure-results -o allure-report --clean

allure open allure-report

exit 0

