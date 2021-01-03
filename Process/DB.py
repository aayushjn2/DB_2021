import json
from Process.Create import CreateOperation
from Process.Read import ReadOperation
from Process.Delete import DeleteOperation
import os
import sys


class DB():
    def __init__(self, path=None, fileName=None):
        self.path = path
        self.fileName = fileName

    def openDB(self, path, fileName):
        self.path = path
        self.fileName = fileName
        pathExistence = self.verifyPathFile()
        if not pathExistence:
            with open(os.path.join(self.path, self.fileName), 'w') as fp:
                pass
        return

    def changeDB(self, path, fileName):
        self.path = path
        self.fileName = fileName
        pathExistence = self.verifyPathFile()
        if not pathExistence:
            with open(os.path.join(self.path, self.fileName), 'w') as fp:
                pass
        print("DB change to "+self.fileName)
        return

    def deleteDB(self, path, fileName):
        self.path = path
        self.fileName = fileName
        pathExistence = self.verifyPathFile()
        if pathExistence:
            os.remove(self.path + '/' + self.fileName)
            print("DB change to "+self.fileName)
        else:
            print("Specified DB doestnot exists")
        return

    def exitDB(self):
        self.path = None
        self.fileName = None
        return

    def insertData(self, key, value, ttl=sys.float_info.max):
        print("insert Data")
        if self.path == None or self.fileName == None:
            print("Please select DB first")
        else:
            CreateOperation(key, value, ttl, self.path, self.fileName)
        return

    def readData(self, key):
        print("read data")
        if self.path == None or self.fileName == None:
            print("Please select DB first")
        else:
            ReadOperation(key, self.path, self.fileName)
        return

    def deleteData(self, key):
        print("Delete Data")
        if self.path == None or self.fileName == None:
            print("Please select DB first")
        else:
            DeleteOperation(key, self.path, self.fileName)
        return

    def verifyPathFile(self):
        check = os.path.isfile(self.path + '/' + self.fileName)
        return check
