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
    def __init__(self, path, fileName, key, ttl, value):
        self.path = path
        self.fileName = fileName
        self.key = key
        self.ttl = ttl
        self.value = value

    def getfileSize(self):
        fileSize = os.path.getsize(self.path+'/'+self.fileName)  # in bytes
        return fileSize

    def checkFileSize(self):
        keySize = KeyAuthenticity(
            self.key, self.path, self.fileName).getKeySize()
        ValueSize = ValueAuthenticity(self.value).getValueSize()
        fileSize = self.getfileSize()

        if(keySize + ValueSize + fileSize <= 8*1024*1024*1024):
            return True
        else:
            return False

# check key format and existence in DB


class KeyAuthenticity():
    def __init__(self, key, path, fileName):
        self.key = key
        self.fileName = fileName
        self.path = path

    def checkKeyType(self):
        if type(key) == str and key.isalpha():
            return True
        else:
            return False

    def checkKeySize(self):
        keySize = self.getKeySize()  # considering key as str datatype
        if keySize == 32:
            return True
        else:
            return False

    def getKeySize(self):
        return sys.getsizeof(str(self.key)) - sys.getsizeof('')

    def checkKeyExistence(self):
        data = None
        with open(self.path + '/' + self.fileName) as f:
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
        valueSize = self.getValueSize()
        if(valueSize <= 8*16*1024):
            return True
        else:
            return False

    def getValueSize(self):
        return sys.getsizeof(str(self.value)) - sys.getsizeof('')

# check TTL property for a key


class TTLAuthenticity():
    def __init__(self, ttl):
        self.ttl = ttl

    def checkTTL(self):
        if(self.ttl - time.time() >= 0):
            return True
        else:
            return False
