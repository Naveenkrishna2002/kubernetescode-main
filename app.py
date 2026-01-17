from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Please subscribe, like, and comment on this video, TY!!!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
