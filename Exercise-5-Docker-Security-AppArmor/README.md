# Exercise 5 - Docker Security with AppArmor

## Objective
Run a Flask application in Docker and prepare an AppArmor profile to demonstrate container security concepts.

## Technologies
- Docker
- Python
- Flask
- AppArmor
- Ubuntu on WSL

## Project Files
- app.py - Flask application.
- Dockerfile - Docker image configuration.
- requirements.txt - Python dependencies.
- my-apparmor-profile - Draft AppArmor security policy.
- apply_apparmor.py - Checks AppArmor availability and profile loading.
- test_restricted_actions.py - Tests API endpoints.
- README.md - Project documentation.

## Build and Run
Build the image:
docker build -t flask-apparmor .

Run the container:
docker run -d --name flask-apparmor -p 5002:5000 flask-apparmor

Test the API:
curl http://localhost:5002/
curl http://localhost:5002/about
curl http://localhost:5002/restricted-test

Run endpoint tests:
python3 test_restricted_actions.py

Check AppArmor availability:
python3 apply_apparmor.py

## Results
- Docker image built successfully.
- Flask application started successfully.
- The home and about endpoints returned HTTP 200.
- The restricted-test endpoint returned HTTP 200 and allowed the write.
- The AppArmor helper detected that enforcement was unavailable in this WSL environment.

## Security Limitation
The AppArmor kernel parameter reported N, and the AppArmor filesystem was not mounted. Docker reported seccomp and cgroup namespace security options, but not AppArmor.

The custom AppArmor profile has not been loaded or enforced in this environment. It must be validated on a compatible Linux host with AppArmor enabled before claiming that restricted actions are blocked.

The endpoint tests demonstrate application functionality, not AppArmor enforcement.
