# things we done
# create a project directory - done
# creating virtual env - done
# install python libraries - done
# write first flask application

# importing libraries
from flask import Flask, render_template
# created a object of flask
app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('madhu.html')

# local machine -> mongo db -> read -> api => fetch =>
# ml task -> json file -> insert data -> any collection
# database
# json file

@app.route('/index')
def index():
    return " welcome pythonist team, to index"


@app.route('/welcome')
def welcom():
    return " welcome pythonist team"


@app.route('/madhu')
def madhu():
    return " welcome pythonist team, it is a welcome page"


@app.route('/ranjith')
def ranjith():
    return " welcome pythonist team, ranjith"


if __name__ == "__main__":
    app.run(debug=True, port='8000', host='0.0.0.0')

# flask running methods - 2
# python filename.py
# set flask app and flask run
