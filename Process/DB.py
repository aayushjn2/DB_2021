import json
from DB_2021.Process.Create import CreateOperation
from DB_2021.Process.Read import ReadOperation
from DB_2021.Process.Delete import DeleteOperation
import os
import sys
class DB():
    def __init__(self, path=None, fileName=None):
        self.path = path
        self.fileName = fileName

    def openDB(self, path, fileName):
        self.path = path
        self.fileName = fileName
        print("DB opened")
        return

    def changeDB(self, path, fileName):
        print("Change DB")
        self.path = path
        self.fileName = fileName
        return

    def exitDB(self):
        print("exit DB")
        self.path = None
        self.fileName = None
        return

    def insertData(self, key, value, ttl=sys.float_info.max):
        print("insert Data")
        CreateOperation(key, value, ttl, self.path, self.fileName)
        return

    def readData(self, key):
        print("read data")
        ReadOperation(key, self.path, self.fileName)
        return

    def deleteData(self, key):
        print("Delete Data")
        DeleteOperation(key, self.path, self.fileName)
        return
