from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Flask! Updated: 2026-01-17'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
