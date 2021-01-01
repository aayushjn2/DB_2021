import json
from Process.Create import CreateOperation
from Process.Read import ReadOperation
from Process.Delete import DeleteOperation
import os
import sys
class InitializeDB():
    def __init__(self):
        print("Enter path to file")
        self.path = input()
        print("Enter DB name")
        self.fileName = input()
        # if file does not exist create db
        # else open existing one
        print("Enter operation you want to perform on DB.")
        print("To insert data command -> insert")
        print("To read data command -> read")
        print("To delete data command -> insert")
        operation = input()
        if(operation == 'insert'):
            print("Enter Key, value, ttl")
            key = input()
            value = input()
            ttl = input()
            instance = CreateOperation(
                key, value, ttl, self.path, self.fileName)
        elif(operation == 'read'):
            print("Please enter key to read corresponding data.")
            key = input()
            instance = ReadOperation(key, self.path, self.fileName)
        elif(operation == 'delete'):
            print("Please Enter to delete key")
            key = input()
            instance = DeleteOperation(key, self.path, self.fileName)
