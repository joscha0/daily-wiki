import os
import json


def adduser(email, lang):
    with open("email.json", "r") as jsonFile:
        data = json.load(jsonFile)
    if(email not in data):
        data[email] = {
            "confirmed": False,
            "language": lang
        }

        with open("email.json", "w") as jsonFile:
            json.dump(data, jsonFile)

        return True
    else:
        return False


def getusers():
    with open("email.json", "r") as jsonFile:
        data = json.load(jsonFile)
    return data


def validateuser(email):
    with open("email.json", "r") as jsonFile:
        data = json.load(jsonFile)
    if(email not in data):
        return False
    else:
        data[email]["confirmed"] = True
        with open("email.json", "w") as jsonFile:
            json.dump(data, jsonFile)
        return True


def deluser(email):
    with open("email.json", "r") as jsonFile:
        data = json.load(jsonFile)
    del data[email]

    print(email)
