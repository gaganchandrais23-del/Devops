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
```text
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
```

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
```bash
docker compose build
```

### 2. Start the services
```bash
docker compose up -d
```

### 3. Check container status
```bash
docker compose ps
```

### 4. View logs
```bash
docker compose logs
```

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
The
