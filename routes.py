from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

# Initialize Flask app and allow CORS
app = Flask(__name__)
CORS(app)

# Set your OpenAI key (You can also use environment variables securely)
openai.api_key = os.getenv("OPENAI_API_KEY") or "your-openai-key-here"

# Helper function to call OpenAI GPT-4o
def ask_gpt(prompt, model="gpt-4o", temperature=0.7):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"OpenAI API Error: {str(e)}"

# /storm — Generates 10 sharp angles on a theme
@app.route('/storm', methods=['POST'])
def storm():
    data = request.get_json()
    theme = data.get("theme", "")
    if not theme:
        return jsonify({"error": "Missing 'theme' in request"}), 400

    prompt = f"Give me 10 bold, creative, and insightful angles to explore the theme: '{theme}'"
    output = ask_gpt(prompt)
    return jsonify({"output": output})

# /map — Converts 1-line idea into MVP structure
@app.route('/map', methods=['POST'])
def map_idea():
    data = request.get_json()
    idea = data.get("idea", "")
    if not idea:
        return jsonify({"error": "Missing 'idea' in request"}), 400

    prompt = f"Break down the idea: '{idea}' into a basic MVP product roadmap. Include components, tools, and first 3 build steps."
    output = ask_gpt(prompt)
    return jsonify({"output": output})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
