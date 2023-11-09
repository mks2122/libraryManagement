from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="./", static_folder="./static")

users = [
    {'username': 'user1', 'password': 'password1'},
    {'username': 'user2', 'password': 'password2'}
]

@app.route('/')
def index():
    return render_template('./log.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    message = ""
    user_found = False
    
    for user in users:
        if user['username'] == username and user['password'] == password:
            user_found = True
            break

    if user_found:
        message = "Login successful"
    else:
        message = "Invalid username or password"

    return render_template('log.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)
