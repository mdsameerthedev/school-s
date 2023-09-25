from flask import Flask

app = Flask(__name__)

@app.route('/js/<name>')
def show():
    return '<h1> Utensil Star {name}<\h1>'.format(name=<name>)

app.run()
