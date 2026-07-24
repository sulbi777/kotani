import os
import json
from flask import Flask, request, jsonify
from confluent_kafka import Producer

app = Flask(__name__)
KAFKA_BROKER = os.getenv('KAFKA_BROKER', 'localhost:9092')

# Bypass kafka error if testing locally without broker
try:
    producer = Producer({'bootstrap.servers': KAFKA_BROKER})
except Exception:
    producer = None

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "service": "kotani-backend", "python_version": "3.12"}), 200

@app.route('/api/v1/logistics/perishable-logic', methods=['POST'])
def calculate_route():
    data = request.json
    temperature = data.get('current_temperature', 0)
    
    if temperature > 8.0:
        route_decision = "DYNAMIC_REROUTE_TO_NEAREST_RETAIL"
        food_loss_risk = "HIGH"
    else:
        route_decision = "CONTINUE_TO_PRIMARY_DESTINATION"
        food_loss_risk = "LOW"

    event_payload = json.dumps({
        "truck_id": data.get("truck_id"),
        "decision": route_decision,
        "risk": food_loss_risk
    })
    
    if producer:
        producer.produce('logistics-events', value=event_payload.encode('utf-8'))
        producer.flush()

    return jsonify({"route_action": route_decision, "risk": food_loss_risk}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
