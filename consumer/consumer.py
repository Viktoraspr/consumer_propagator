from flask import Flask, request, jsonify
from consumer_config import get_config
from models import db, Event

app = Flask(__name__)
CONSUMER = get_config()

app.config['SQLALCHEMY_DATABASE_URI'] = CONSUMER.database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/event', methods=['POST'])
def get_event():
    if request.is_json:
        event = request.get_json()
        if not (isinstance(event, dict) and 'event_type' in event and 'event_payload' in event and len(event) == 2):
            return jsonify({"error": "Invalid data structure"}), 400

        database_event = Event(event_type=str(event['event_type']), event_payload=str(event['event_payload']))
        db.session.add(database_event)
        db.session.commit()

        return jsonify({"message": "Event received"}), 200
    else:
        return jsonify({"error": "Request must be JSON"}), 400

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host=CONSUMER.host, port=CONSUMER.port)