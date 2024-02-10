from flask import Flask, request

app = Flask(__name__)
counter = 0

@app.route('/', methods=['GET', 'POST'])
def handle_requests():
    global counter

    if request.method == 'POST':
        # Increment the counter on each POST request
        counter += 1
        return f'Counter value: {counter}'
    else:
        # Return the current counter value on GET request
        return f'Current counter value: {counter}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
