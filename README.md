# Python REST API Server

This project is a (very) basic python app using flask.  The hello.py file splats your classic 'hello world' onto the DOM at '/', uses a rendered template that is mildly styled and accesses the static .css file at '/hello', and requests made to '/login' are parsed out to access the body of the requests or params / args, depending on the method.

The config.py and connect.py files use psycopg2 to contact a database.  The information for db setup can be found in the database.sql file; it's a slice of the db from my solo project.  This can be accessed by running 'python3 connect.py' in console.

Most of the action here shows on the python/flask server console.  Requests to /login and the database don't do anything on client side, all just in the server console.

I found these resources especially helpful when working on this -
https://flask.palletsprojects.com/en/1.1.x/
https://www.learnpython.org/en/Welcome
https://pypi.org/project/psycopg2/

Although my main takeaway was that I need to remember that I'm running python3 and pip3, so I can't just run 'python connect.py' or 'pip install etc' in the command line...
