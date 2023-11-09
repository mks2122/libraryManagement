from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="./template", static_folder="./static")

users = [
    {'username': 'user1', 'password': 'password1'},
    {'username': 'user2', 'password': 'password2'}
]

@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/log.html')
def loginPage():
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
        return redirect(url_for('index'))
    else:
        message = "Invalid username or password"
        return render_template('log.html', message=message)

@app.route('/inOut.html')
def inOut():
    return render_template('./inOut.html')


if __name__ == '__main__':
    app.run(debug=True)
