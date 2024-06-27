from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return ('This is home boy')

@app.route('/<name>')
def hello_world(name):
    return ('Hello %s' %name)

if __name__ == '__main__':
    app.run(debug = True)

