import os
import openai
from flask import Flask, request, jsonify

app = Flask(__name__)

# Set your API key from an environment variable
openai.api_key = os.environ.get('OPENAI_API_KEY')

@app.route("/")
def index():
    return "Hello, World!"

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt', '')
    try:
        # Using the ChatCompletion API with gpt-3.5-turbo
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )
        generated_text = response.choices[0].message.content.strip()
        return jsonify({'result': generated_text}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
