
from flask import Flask, request, jsonify
from agent_core import generate_ideas, map_idea

app = Flask(__name__)

@app.route('/storm', methods=['POST'])
def storm():
    theme = request.json.get('theme', '')
    return jsonify(generate_ideas(theme))

@app.route('/map', methods=['POST'])
def map_():
    idea = request.json.get('idea', '')
    return jsonify(map_idea(idea))

if __name__ == '__main__':
    app.run(debug=True)
