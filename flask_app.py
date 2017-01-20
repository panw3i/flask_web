from flask import Flask,render_template
from modles import User

app = Flask(__name__)


@app.route('/')
def hello_world():
    content = "hello world!!!!"
    return render_template("index.html", content=content)


@app.route('/user')
def user_index():
    user = User(1, "pan")
    return render_template("user_index.html",user=user)


@app.route('/userlist')
def user_list():
    users = []
    for i in range(10):
        user = User(i,"pan")
        users.append(user)

    return render_template("user_list.html",users=users)

if __name__ == '__main__':
    app.run()