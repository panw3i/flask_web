from flask import Flask
from flask import render_template
from flask import abort, redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/pan')
def pan():
    return redirect('/check')


@app.route('/check')
def f_check():
    abort(404)


# doing somting here

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.errorhandler(404)
def bad_request(error):
    return render_template('bad_request.html'), 400


@app.route("/login/<username>")
def show_welcome(username):
    return 'Hi %s' % username


@app.route('/add/<int:number>')
def add(number):
    return "%d" % (number + 1)


@app.route('/student')
def students():
    return "students"


@app.route('/school/')
def school():
    return "school"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9001)
