"""
Created by sudo-ranjith at 19/04/20

Scenario: # we are going to CRUD operation.
"""

from flask import Flask, jsonify
import pymongo
from datetime import datetime

app = Flask(__name__)

# mongodb connections
# mongo connection URI
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# database name
mydb = myclient["pythonist"]
# collection name
mycol = mydb["customers"]


@app.route('/home')
@app.route('/')
def home():
    return "welcome home"


@app.route('/create', methods=['POST'])
def create():
    data = {"name": "sanjeev", "address": "Palladam", "excecuted_at": datetime.now()}
    x = mycol.insert_one(data)
    return jsonify({"message": "data inserted successfully", "excecuted_at": datetime.now()})


# read API
@app.route('/read', methods=['GET'])
def akjsnfalusfnasifn():
    # here we need to write find query
    results = mycol.find()
    # created a list
    data = []

    for x in results:
        # inserting data into the list
        print(x, type(x))
        del x["_id"]
        data.append(x)
    return jsonify({"data": data})


# update
@app.route('/update', methods=['PUT'])
def update():
    # find
    payload = {"name": "sanjeev"}
    find_resp = mycol.find(payload)
    if find_resp:
        data = {"name": "Sanjeev Ravi", "address": "Palladam", "excecuted_at": datetime.now()}
        x = mycol.update_one(payload, {"$set": data})
        return jsonify({"message": "data updated successfully", "excecuted_at": datetime.now()})
    else:
        return jsonify({"message": "please check the value you entered for update"})


# delete
@app.route('/delete', methods=['DELETE'])
def delete():
    data = {"name": "John"}
    mycol.delete_one(data)
    return jsonify({"message": "data deleted successfully", "excecuted_at": datetime.now()})


if __name__ == "__main__":
    app.run(debug=True)
