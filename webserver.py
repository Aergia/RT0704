import json
from flask import Flask, request
import os
import requests

path = os.path.dirname(__file__)
app = Flask(__name__)

def createUserFile(username):
    file = openUserfile(username)
    json.dump([],file)
    closeUserFile(file)

def deleteUserFile(username):
    if(os.path.exists(os.path.dirname(__file__)+"/user-data/"+username+".json")):
        os.remove(os.path.dirname(__file__)+"/user-data/"+username+".json")

def openUserfile(username):
    path = os.path.dirname(__file__)+"/user-data/"+username+".json"
    file = open(path, 'w+')
    return file

def closeUserFile(file):
    file.close()

@app.route('/add', methods= ['POST'])
def add():
    name = str(request.get_data())[7:]
    name = str(name[:int(len(name)-1)])
    dicto = {}
    dicto+=name
    req = requests.post('http://localhost:8000/add', json=dicto)

    
    return '', 204

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8001)