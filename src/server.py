from flask import Flask, render_template

app = Flask(__name__, static_folder='../static', template_folder='../templates')

@app.route('/')
@app.route('/index.html')
@app.route('/index.html', methods=['get'])
def index():
    return render_template('index.html')

app.run(port=9999, debug=True)