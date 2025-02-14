from flask import Flask, request, jsonify
from flask_cors import CORS
from performance_analysis import analyze_code

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    code_snippet = data.get("code", "")
    if not code_snippet:
        return jsonify({"error": "No code provided"}), 400
    
    result = analyze_code(code_snippet)
    return jsonify(result)

if __name__ == '__main__':
    from os import environ
    app.run(host="0.0.0.0", port=int(environ.get("PORT", 5000)))
