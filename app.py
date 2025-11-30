from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api')
def api():
    return jsonify({"message": "Hello from backend"}), 200

@app.route("/health")
def health():
    return "OK", 200

@app.route("/ready")
def ready():
    return "READY", 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
