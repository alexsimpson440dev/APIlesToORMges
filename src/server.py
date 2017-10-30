from flask import Flask, render_template, request, session, redirect
from src.dbManager import DBManager

#sets app routes and app secret key
app = Flask(__name__, '/static', static_folder='../static', template_folder='../templates')
app.secret_key = 'DSM stands for diamond star motors'

#calls db manager class
MANAGER = DBManager()

#gets index route
@app.route('/')
@app.route('/index')
@app.route('/index.html', methods=['get'])
def index():
    return render_template('index.html')
#gets signup route, if post, then it will send the form information to the database
@app.route('/signup', methods=['get', 'post'])
@app.route('/signup.html', methods=['get'])
def sign_up():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email_address = request.form.get('email_address')
        password = request.form.get('password')
        try:
            MANAGER.add_user(first_name, last_name, email_address, password)
            sign_in(email_address)
        except RuntimeError as e:
            print('Run Time Error: ', e)
            return redirect('signup.html')

        return render_template('index.html')

    #executes on a request 'GET' method
    else:
        return render_template('signup.html')

@app.route('/search', methods=['get', 'post'])
@app.route('/search.html', methods=['get'])
def search():
    return render_template('search.html')
#signs user in (work in progress)
def sign_in(email_address):
    session['email'] = email_address

#calls app to run and then assigns a port and debug to True
if __name__ == '__main__':
    app.run(port=9999, debug=True)