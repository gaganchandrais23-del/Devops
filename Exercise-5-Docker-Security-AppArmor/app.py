from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Docker AppArmor Security Demo",
        "status": "running"
    })

@app.route("/about")
def about():
    return jsonify({
        "name": "AppArmor Security Demo",
        "purpose": "Demonstrate container security testing"
    })

@app.route("/restricted-test")
def restricted_test():
    test_file = "/restricted-test.txt"

    try:
        with open(test_file, "w") as file:
            file.write("Security test")
        return jsonify({
            "result": "write allowed",
            "note": "AppArmor enforcement must be verified separately"
        }), 200
    except PermissionError:
        return jsonify({
            "result": "write denied",
            "note": "The write was denied; the cause must be verified"
        }), 403
    except OSError as error:
        return jsonify({
            "result": "write failed",
            "error": str(error)
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
