# Exercise 6 - Grafana Real-Time Monitoring of Quick Commerce App

## Objective
Build a Docker-based monitoring system for a simulated quick-commerce application using Python, Prometheus, and Grafana. The application generates delivery metrics, Prometheus collects them, and Grafana visualizes them through a real-time dashboard.

## Technologies Used
- Python
- Flask
- Prometheus
- Grafana
- Docker
- Docker Compose
- Jenkins Pipeline

## Project Structure

Exercise-6-Grafana-Monitoring-Fresh/
├── Dockerfile
├── Jenkinsfile
├── README.md
├── alert_rules.yml
├── compose.yaml
├── delivery_metrics.py
├── prometheus.yml
├── requirements.txt
└── grafana/
    ├── dashboards/
    │   └── quick-commerce.json
    └── provisioning/
        ├── dashboards/
        │   └── dashboard.yml
        └── datasources/
            └── prometheus.yml


## Application Features
- Simulates quick-commerce delivery activity.
- Exposes application health and Prometheus metrics endpoints.
- Collects delivery metrics using Prometheus.
- Displays monitoring metrics through Grafana dashboards.
- Defines alert rules for application availability and delivery conditions.
- Includes a Jenkins pipeline for code validation and Docker image building.

## Metrics Monitored
| Metric | Description |
|---|---|
| `quickcommerce_deliveries_total` | Total completed deliveries |
| `quickcommerce_active_orders` | Number of active orders |
| `quickcommerce_delivery_time_seconds` | Simulated delivery time in seconds |
| `quickcommerce_failed_deliveries_total` | Total failed deliveries |

## Docker Setup

### 1. Build the application

docker compose build


### 2. Start the services

docker compose up -d


### 3. Check container status

docker compose ps


### 4. View logs

docker compose logs


## Application Endpoints
| Service | URL |
|---|---|
| Quick Commerce Application | http://localhost:8001/ |
| Application Health Check | http://localhost:8001/health |
| Prometheus Metrics | http://localhost:8001/metrics |
| Prometheus Dashboard | http://localhost:9091 |
| Prometheus Targets | http://localhost:9091/targets |
| Grafana Dashboard | http://localhost:3001 |

## Grafana Login
The initial credentials configured in Docker Compose are:

- **Username:** `admin`
- **Password:** `admin`

Change the default password when prompted or before using the setup beyond local testing.

## Grafana Dashboard
The dashboard is named **Quick Commerce Real-Time Monitoring** and contains four panels:

1. Total Completed Deliveries
2. Active Orders
3. Delivery Time (Seconds)
4. Failed Deliveries

The dashboard refreshes automatically every five seconds.

## Prometheus Alert Rules
The project includes alert rules for:
- `QuickCommerceAppDown` — detects when the application cannot be scraped.
- `HighDeliveryTime` — detects simulated delivery time above 900 seconds.
- `HighActiveOrders` — detects active orders above 25.

## Jenkins Pipeline
The `Jenkinsfile` defines these stages:

1. Checkout
2. Validate Python
3. Validate Configuration Files
4. Build Docker Image

The pipeline requires a configured Jenkins agent with Python 3, PyYAML, and Docker access. Pipeline execution must be verified separately in that environment.

## Validation and Results
- The application endpoint returned application information.
- The health endpoint returned a healthy status.
- The metrics endpoint exposed delivery metrics.
- Prometheus successfully collected delivery metrics.
- The Grafana dashboard displayed all four metric panels.

The metrics are simulated for demonstration purposes and do not represent real customer or delivery-service data.

## Stop the Services

docker compose down


This stops and removes the Compose containers while preserving the named Grafana data volume.

## Conclusion
This exercise demonstrates how Docker, Prometheus, and Grafana can be integrated to monitor a simulated quick-commerce application. It also introduces configuration validation and Docker image building through a Jenkins pipeline.
