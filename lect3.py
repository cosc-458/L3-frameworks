import flask

app = flask.Flask(__name__)


@app.route('/') # Python decorator 
def index(): 
    return "Hello, world!"

# Uh oh - this may not work
app.run()
