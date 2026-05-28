from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():

    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Name Validation
    if not name[0].isupper():
        return "First letter of Name must be Capital"

    # Simple Email Validation
    if '@' not in email or '.com' not in email:
        return "Invalid Email Address"

    # Message Validation
    if len(message.strip()) == 0:
        return "Message cannot be empty"

    return render_template('success.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
