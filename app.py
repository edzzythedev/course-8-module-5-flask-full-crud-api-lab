from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# Helper function to find event by ID
def find_event_by_id(event_id):
    for event in events:
        if event.id == event_id:
            return event
    return None

# TODO: Task 1 - Define the Problem
# Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    # TODO: Task 2 - Design and Develop the Code
    # Get JSON data from request
    data = request.get_json()
    
    # TODO: Task 3 - Implement the Loop and Process Each Element
    # Validate that title exists in the JSON
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400
    
    if "title" not in data:
        return jsonify({"error": "Missing required field: title"}), 400
    
    # Create new event with next ID
    new_id = len(events) + 1
    new_event = Event(new_id, data["title"])
    events.append(new_event)
    
    # TODO: Task 4 - Return and Handle Results
    # Return 201 Created status with the new event
    return jsonify(new_event.to_dict()), 201

# TODO: Task 1 - Define the Problem
# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    # TODO: Task 2 - Design and Develop the Code
    # Find the event by ID
    event = find_event_by_id(event_id)
    
    # TODO: Task 3 - Implement the Loop and Process Each Element
    # Check if event exists
    if not event:
        return jsonify({"error": f"Event with id {event_id} not found"}), 404
    
    # Get JSON data from request
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400
    
    # Update title if provided
    if "title" in data:
        event.title = data["title"]
    
    # TODO: Task 4 - Return and Handle Results
    # Return updated event
    return jsonify(event.to_dict()), 200

# TODO: Task 1 - Define the Problem
# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    # TODO: Task 2 - Design and Develop the Code
    # Find the event by ID
    event = find_event_by_id(event_id)
    
    # TODO: Task 3 - Implement the Loop and Process Each Element
    # Check if event exists
    if not event:
        return jsonify({"error": f"Event with id {event_id} not found"}), 404
    
    # Remove event from list
    events.remove(event)
    
    # TODO: Task 4 - Return and Handle Results
    # Return 204 No Content for successful deletion
    return "", 204

# Bonus: GET all events (for testing)
@app.route("/events", methods=["GET"])
def get_events():
    return jsonify([event.to_dict() for event in events]), 200

# Bonus: Welcome route
@app.route("/")
def welcome():
    return jsonify({
        "message": "Welcome to the Events API",
        "endpoints": {
            "GET /": "Welcome message",
            "GET /events": "Get all events",
            "POST /events": "Create a new event",
            "PATCH /events/<id>": "Update an event",
            "DELETE /events/<id>": "Delete an event"
        }
    })

if __name__ == "__main__":
    app.run(debug=True)