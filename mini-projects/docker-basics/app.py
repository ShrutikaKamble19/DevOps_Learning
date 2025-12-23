from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>🚀 DevOps Learning: Docker Mini-Project</h1><p>Flask app running in Docker!</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
EOF

