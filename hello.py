from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    print('Hello, World!')
    return 'Hello, World!'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/login', methods=['GET', 'POST', 'PUT', 'DELETE'])
# yes i'm aware the login route likely wouldn't accept all these routes
def login():
    error = None
    if request.method == 'GET':
        print('getted')
        return 'getted'
    elif request.method == 'POST':
        print("username from body is %s, password from body is %s" %
              (request.form['username'], request.form['password']))
        return 'posted'
    elif request.method == 'PUT':
        print("user id to update from params is %s" % request.args['id'])
        return 'putted'
    elif request.method == 'DELETE':
        print("user id to delete from params is %s" % request.args['id'])
        return 'deleted'
    else:
        print('none of the above')
        return 'none of the above'
