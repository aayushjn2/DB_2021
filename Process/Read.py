import threading
import json
import threading
from DB_2021.Process.utility import KeyAuthenticity, TTLAuthenticity


class ReadOperation(threading.Thread):
    def __init__(self, key, path, fileName):
        threading.Thread.__init__(self)
        self.key = key
        self.ttl = ttl
        self.path = path
        self.fileName = fileName

    def run(self):
        # key check
        key_instance = KeyAuthenticity(self.key)
        # key_size_flag = key_instance.checkSize()
        key_type_flag = key_instance.checkKeyType()
        key_existence_flag = key_instance.checkKeyExistence()
        # if not key_size_flag:
        #     print("Enter a valid sized key")
        #     return
        if not key_type_flag:
            print("Enter a valid type of key. Please follow proper format")
            return
        if not key_existence_flag:
            print(" key doesnot exists in DB")
            return
        data = getData(key, self.path, self.fileName)
        # TTL check
        ttl_instance = TTLAuthenticity(data.ttl)
        ttl_status_flag = ttl_instance.checkTTL()
        if(ttl_status_flag == False):
            print("Key has been destroyed and hence key is not in DB")
            return
        else:
            print(data.value)
            return
        # if correct key and ttl then return value object now


def getData(key, path, fileName):
    data = None
    with open(path + '/' + fileName) as f:
        data = json.load(f)
    if(key in data):
        return data[key]
    else:
        return "error"
