from flask import Flask, render_template

app = Flask(__name__, '/static', static_folder='../static', template_folder='../templates')

@app.route('/')
@app.route('/index')
@app.route('/index.html', methods=['get'])
def index():
    return render_template('index.html')
@app.route('/signup', methods=['get', 'post'])
@app.route('/signup.html', methods=['get'])
def sign_up():
    return render_template('signup.html')

app.run(port=9999, debug=True)