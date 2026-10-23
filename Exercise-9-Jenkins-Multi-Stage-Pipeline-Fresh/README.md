# Exercise 9 - Jenkins Multi-Stage Pipeline

## Overview
This project demonstrates how to organize application validation into multiple stages using a Jenkins Declarative Pipeline.

## Objective
To understand how Jenkins executes build and test tasks in a defined sequence.

## Technologies
- Jenkins
- Python
- pytest
- Bash
- Docker

## Project Files
- `app.py` - Sample Python application.
- `test_app.py` - Automated application test.
- `requirements.txt` - Python testing dependency.
- `Jenkinsfile` - Defines the multi-stage pipeline.
- `README.md` - Project documentation.

## Pipeline Stages
1. Checkout - Prepares the source code.
2. Build - Checks the Python environment and runs the application.
3. Test - Installs dependencies and runs automated tests.
4. Deploy - Demonstrates the final validation stage.

## Execution
Configure a Jenkins Pipeline job using the pipeline script or the `Jenkinsfile`. Run the job and inspect Console Output to verify each stage.

## Expected Result
The application should print its status, the automated test should pass, and the Jenkins build should finish successfully.

## Learning Outcome
Learn to define and execute a structured, multi-stage CI pipeline in Jenkins.
