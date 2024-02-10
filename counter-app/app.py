from flask import Flask, request

app = Flask(__name__)
count = 0

@app.route('/')
def index():
    global count
    count += 1
    return f'Counter: {count}\n'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)