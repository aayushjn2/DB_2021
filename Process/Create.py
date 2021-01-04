from Process.utility import KeyAuthenticity, ValueAuthenticity, TTLAuthenticity, FileAuthenticity, UpdateData
import time
import json


class CreateOperation():
    def __init__(self, key, value, ttl, path, fileName):
        self.key = key
        self.value = value
        self.ttl = ttl
        self.path = path
        self.fileName = fileName

    def checkKeyValueTTL(self):
        # key check
        key_instance = KeyAuthenticity(self.key, self.path, self.fileName)
        key_size_flag = key_instance.checkSize()
        key_type_flag = key_instance.checkKeyType()
        key_existence_flag = key_instance.checkKeyExistence()
        if not key_size_flag:
            print("Enter a valid sized key")
            return False
        if not key_type_flag:
            print("Enter a valid type of key. Please follow proper format")
            return False
        if not key_existence_flag:
            print(" key doesnot exists in DB")
            return False
        # TTL check
        ttl_instance = TTLAuthenticity(self.ttl)
        ttl_status_flag = ttl_instance.checkTTL()
        if(ttl_status_flag == False):
            print("Key has been destroyed and hence key is not in DB")
            return False
        # Value check
        value_instance = ValueAuthenticity(self.value)
        value_type = value_instance.checkValueType()
        value_size_flag = value_instance.checkValueSize()
        if not value_type:
            print("check value format")
            return False
        if not value_size_flag:
            print("Value size exceeds")
            return False
        return True

    def writeData(self):
        fileInstance = FileAuthenticity(
            self.path, self.fileName, self.key, self.ttl, self.value)
        if fileInstance.checkFileSize():
            if self.checkKeyValueTTL():
                data = None
                with open(self.path + '/' + self.fileName) as f:
                    data = json.load(f)
                data[self.key] = {'value': self.value, 'ttl': self.ttl}
                UpdateData(self.path, self.fileName, data)
                print("Data entered")
        else:
            print(
                "File Size will be greater than 1GB. Either delete some data or use another DB")
