from flask import Flask, request, jsonify
from flask_cors import CORS
from performance_analysis import analyze_code

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    code_snippet = data.get("code", "")
    if not code_snippet:
        return jsonify({"error": "No code provided"}), 400
    
    result = analyze_code(code_snippet)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
