from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<user>')
def index(user):
    return render_template('file2.html',name = user)

if __name__ == '__main__':
    app.run(debug = True)