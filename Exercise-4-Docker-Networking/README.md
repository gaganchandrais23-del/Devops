# Exercise 4 - Docker Networking

## Objective
Create a custom Docker bridge network and run a Flask REST API, MySQL, and Redis containers on the same network.

## Technologies
- Docker
- Docker Bridge Networking
- Python
- Flask
- MySQL
- Redis

## Files
- `app.py` - Flask REST API implementation
- `Dockerfile` - Instructions to build the Flask API image
- `requirements.txt` - Python dependencies
- `README.md` - Exercise documentation

## Implementation

### 1. Create the Docker network
```bash
docker network create --driver bridge my-bridge-net
```

### 2. Build the Flask API image
```bash
docker build -t flask-api .
```

### 3. Start MySQL and Redis
```bash
docker run -d --name mysql --network my-bridge-net -e MYSQL_ROOT_PASSWORD=LabPassword123 mysql:latest
docker run -d --name redis --network my-bridge-net redis:latest
```

### 4. Start the Flask API
```bash
docker run -d --name flask --network my-bridge-net -p 5001:5001 flask-api
```

### 5. Test the API
```bash
curl http://localhost:5001/about
```

Expected response:
```json
{
  "name": "Simple REST API",
  "version": "1.0",
  "description": "This is a simple REST API built with Flask."
}
```

### 6. Verify network connectivity
The Flask container successfully resolved both MySQL and Redis container names and connected to their service ports.

- MySQL: port 3306
- Redis: port 6379

## Results
- The Flask API returned the expected JSON response.
- MySQL and Redis were reachable from the Flask container.
- All three containers used the custom Docker bridge network.

## Cleanup
When the exercise is no longer needed, stop and remove the exercise containers:
```bash
docker stop flask mysql redis
docker rm flask mysql redis
docker network rm my-bridge-net
```

**Note:** Run cleanup commands only after finishing the exercise.
