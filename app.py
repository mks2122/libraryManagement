from flask import Flask, render_template, request, redirect, url_for
import sqlite3

global user_found
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
    
    if not user_found:
        message = "Invalid username or password"
        return render_template('log.html', message=message)
    # return redirect('/')
    return render_template("index.html", button_visibility=True)


@app.route('/inOut.html')
def inOut():
    return render_template('./inOut.html')
@app.route('/bookdetails.html')
def bookdetails():
    con=sqlite3.connect('library.db')
    cursor=con.cursor()
    cursor.execute("SELECT * FROM books")
    
    results = cursor.fetchall()
    con.close()
    # print(results)

    return render_template('./bookdetails.html',data=results[1:])
@app.route('/details.html')
def details():
    # if user_found:
        con=sqlite3.connect('library.db')
        cursor=con.cursor()
        cursor.execute("SELECT * FROM currentDetails")
        
        results = cursor.fetchall()
        con.close()
        print(results)

        return render_template('./details.html',data=results)
    # else:
    #     return redirect('/log.html')

# con.close()
if __name__ == '__main__':
    app.run(debug=True)
