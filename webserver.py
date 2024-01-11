import json
import os



def createUserFile(username):
    file = openUserfile(username)

    json.dump([],file)

def openUserfile(username):
    path = os.path.dirname(__file__)+"/user-data/"+username+".json"
    file = open(path, 'w+')
    return file

def closeUserFile(file):
    file.close()

createUserFile("lapin")