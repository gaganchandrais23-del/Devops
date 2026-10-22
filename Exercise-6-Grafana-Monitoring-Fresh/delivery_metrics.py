from flask import Flask, jsonify
from prometheus_client import Counter, Gauge, generate_latest, CONTENT_TYPE_LATEST
from prometheus_client import CollectorRegistry
from flask import Response
import random
import threading
import time

app = Flask(__name__)

registry = CollectorRegistry()

DELIVERIES = Counter(
    "quickcommerce_deliveries_total",
    "Total number of completed quick-commerce deliveries",
    registry=registry
)

ACTIVE_ORDERS = Gauge(
    "quickcommerce_active_orders",
    "Number of currently active delivery orders",
    registry=registry
)

DELIVERY_TIME = Gauge(
    "quickcommerce_delivery_time_seconds",
    "Simulated average delivery time in seconds",
    registry=registry
)

FAILED_DELIVERIES = Counter(
    "quickcommerce_failed_deliveries_total",
    "Total number of failed deliveries",
    registry=registry
)

state = {
    "completed": 0,
    "failed": 0,
    "active": 10
}

def simulate_deliveries():
    while True:
        time.sleep(5)

        if random.random() < 0.85:
            DELIVERIES.inc()
            state["completed"] += 1
        else:
            FAILED_DELIVERIES.inc()
            state["failed"] += 1

        state["active"] = random.randint(5, 30)
        ACTIVE_ORDERS.set(state["active"])
        DELIVERY_TIME.set(random.randint(300, 1200))

@app.route("/")
def home():
    return jsonify({
        "application": "Quick Commerce Monitoring",
        "status": "running",
        "metrics_endpoint": "/metrics"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/deliveries")
def deliveries():
    return jsonify(state)

@app.route("/metrics")
def metrics():
    return Response(
        generate_latest(registry),
        mimetype=CONTENT_TYPE_LATEST
    )

ACTIVE_ORDERS.set(state["active"])
DELIVERY_TIME.set(600)

threading.Thread(target=simulate_deliveries, daemon=True).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
