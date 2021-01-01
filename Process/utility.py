import json
import time
import sys
import os

# update data into DB


class UpdateData():
    def __init__(self, path, fileName, data):
        self.path = path
        self.fileName = fileName
        self.data = data

    def update(self):
        with open(self.path + '/' + self.fileName, "w") as outfile:
            json.dump(self.data, outfile)

# check constraints for file


class FileAuthenticity():
    def __init__(self, path, fileName):
        self.path = path
        self.fileName = fileName

    def fileSize(self):
        size = os.path.getsize(self.path+'/'+self.fileName)  # in bytes
        return size

# check key format and existence in DB


class KeyAuthenticity():
    def __init__(self, key):
        self.key = key

    def checkKeyType(self):
        if type(key) == str and key.isalpha():
            return True
        else:
            return False

    def checkSize(self):
        keySize = self.getKeySize()  # considering key as str datatype
        if keySize == 32:
            return True
        else:
            return False

    def getKeySize(self):
        return len(self.key)

    def checkKeyExistence(self):
        data = None
        with open('path_to_file/DataStore.json') as f:
            data = json.load(f)
        if (key in data):
            return True
        else:
            return False

# check proper format of value for a given key


class ValueAuthenticity():
    def __init__(self, value):
        self.value = value

    # check value type
    def checkValueType(self):
        if isinstance(self.value, dict):
            return True
        else:
            return False

    # check Value size
    def checkValueSize(self):
        valueSize = self.getObjectSize()
        if(valueSize <= "16KB"):
            return True
        else:
            return False

    def getObejectSize(self):
        size = None
        return size

# check TTL property for a key


class TTLAuthenticity():
    def __init__(self, ttl):
        self.ttl = ttl

    def checkTTL(self):
        if(self.ttl - time.time() >= 0):
            return True
        else:
            return False
