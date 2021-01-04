from Process.utility import KeyAuthenticity, TTLAuthenticity, UpdateData
import json


class DeleteOperation():
    def __init__(self, key, path, fileName):
        self.key = key
        self.path = path
        self.fileName = fileName

    def delete(self):
        # key check
        key_instance = KeyAuthenticity(self.key, self.path, self.fileName)
        key_size_flag = key_instance.checkSize()
        key_type_flag = key_instance.checkKeyType()
        key_existence_flag = key_instance.checkKeyExistence()
        if not key_size_flag:
            print("Enter a valid sized key")
            return
        if not key_type_flag:
            print("Enter a valid type of key. Please follow proper format")
            return
        if not key_existence_flag:
            print(" key doesnot exists in DB")
            return
        # TTL check
        ttl_instance = TTLAuthenticity(self.ttl)
        ttl_status_flag = ttl_instance.checkTTL()
        if(ttl_status_flag == False):
            print("Key has been destroyed and hence key is not in DB")
            return
        self.deleteData()

    def deleteData(self):
        data = None
        with open(self.path + '/' + self.fileName) as f:
            data = json.load(f)
        del data[key]
        updateData = UpdateData(self.path, self.fileName, data)
        updateData.update()
