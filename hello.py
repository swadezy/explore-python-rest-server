from flask import Flask, request, render_template, url_for
app = Flask(__name__)    

# splats a basic string to the DOM when navigating to localhost:5000
@app.route('/')
def hello_world():
    return 'Hello, World!'

# on routing to either /hello or /hello/<name>, renders hello.html and passes the name 'param' (?) to that html file
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

# here's our routes
# yes i'm aware the login route likely wouldn't accept all these routes but ay it's for testing gimme a break
@app.route('/login', methods=['GET', 'POST', 'PUT', 'DELETE'])
def login():
    error = None
    if request.method == 'GET':
        print('getted')
        return 'getted'

    # uses request.form to access the body of a post request
    elif request.method == 'POST':
        print("username from body is %s, password from body is %s" %
              (request.form['username'], request.form['password']))
        return 'posted'

    # uses request.args to access the params of a put or delete request
    elif request.method == 'PUT':
        print("user id to update from params is %s" % request.args['id'])
        return 'putted'
    elif request.method == 'DELETE':
        print("user id to delete from params is %s" % request.args['id'])
        return 'deleted'
    else:
        print('none of the above')
        return 'none of the above'
