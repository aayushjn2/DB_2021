from DB_2021.Process.utility import KeyAuthenticity, ValueAuthenticity, TTLAuthenticity, FileAuthenticity, UpdateData
import time
import json


class CreateOperation():
    def __init__(self, key, value, ttl, path, fileName):
        self.key = key
        self.value = value
        self.ttl = ttl
        self.path = path
        self.fileName = fileName
        self.checkFileSize()

    def checkFileSize(self):
        file_instance = FileAuthenticity(self.path, self.fileName)
        fileSize = file_instance.fileSize()  # in bytes
        if(fileSize <= 1024*1024*1024*8):
            self.checkKeyValueTTL()
        else:
            print("File size is greater than 1GB")
            return

    def checkKeyValueTTL(self):
        # key check
        key_instance = KeyAuthenticity(self.key)
        # key_size_flag = key_instance.checkSize()
        # key_type_flag = key_instance.checkKeyType()
        key_existence_flag = key_instance.checkKeyExistence()
        # if not key_size_flag:
        #     print("Enter a valid sized key")
        #     return
        # if not key_type_flag:
        #     print("Enter a valid type of key. Please follow proper format")
        #     return
        if not key_existence_flag:
            print(" key doesnot exists in DB")
            return
        # TTL check
        ttl_instance = TTLAuthenticity(self.ttl)
        ttl_status_flag = ttl_instance.checkTTL()
        if(ttl_status_flag == False):
            print("Key has been destroyed and hence key is not in DB")
            return
        # Value check
        value_instance = ValueAuthenticity(self.value)
        value_type = value_instance.checkValueType()
        # value_size_flag = value_instance.checkValueSize()
        if not value_type:
            print("check value format")
            return
        # if not value_size_flag:
        #     print("Value size exceeds")
        #     return
        self.writeData()
        print("Data entered")

    def writeData(self):
        data = None
        with open(self.path + '/' + self.fileName) as f:
            data = json.load(f)
        data[self.key] = {'value': self.value, 'ttl': self.ttl}
        UpdateData(self.path, self.fileName, data)
