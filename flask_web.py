from flask import Flask
from flask import render_template
from flask import abort, redirect
from flask import url_for

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


# 多个路由可以指定同一处理函数

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


# 错误处理
@app.errorhandler(404)
def bad_request(error):
    return render_template('bad_request.html'), 400


# 动态url
@app.route("/login/<username>")
def show_welcome(username):
    return 'Hi %s' % username


# url里面接受int类型
@app.route('/add/<int:number>')
def add(number):
    return "%d" % (number + 1)


# url后面有无/的区别
@app.route('/student')
def students():
    return "students"


@app.route('/school/')
def school():
    return "school"


@app.route('/get_method',methods=['get'])
def get_method():
    return 'use get method'


@app.route('/get_url')
def get_url():
    return url_for(get_method)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9001)
