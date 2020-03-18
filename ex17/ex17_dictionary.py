import sys
sys.path.append("..")
from ex14.ex14_dllist import *

class Dictionary():
    def __init__(self, number_bucket=250):
        self.map = DoubleLinkedList()
        for i in range(0, number_bucket):
            self.map.push(DoubleLinkedList())


    def get_bucket(self, key):
        hash_id = hash(key)
        bucket_id =  hash_id % self.map.count()
        return self.map.get(bucket_id)


    def get(self, key, default=None):
        """ Return the value"""
      #  default = None
        result = None
        bucket = self.get_bucket(key)
        node = bucket.begin

        while node:
            if node.value[0] == key:
                result = node.value[1]
            else:
                pass
            node = node.next


        return result or default


    def set(self, key, val):
        #print(self.bucket_id(key))
        bucket = self.get_bucket(key)

        if bucket.begin is None:
            bucket.push((key,val))
        else:
            node = bucket.begin
            while node:
                if node.value[0] == key:
                    node.value[1] = val
              #      return None
                node = node.next

        return None


    def list(self):
        bucket = self.map.begin
        while bucket:
            slot = bucket.value.begin
            while slot:
                print(slot.value)
                slot = slot.next
            bucket = bucket.next
        return None

    def get_keys(self):
        result = []
        bucket = self.map.begin
        while bucket:
            slot = bucket.value.begin
            while slot:
                #print(slot.value)
                result.append(slot.value[0])
                slot = slot.next
            bucket = bucket.next
        return result

    def get_values(self):
        result = []
        bucket = self.map.begin
        while bucket:
            slot = bucket.value.begin
            while slot:
                #print(slot.value)
                result.append(slot.value[1])
                slot = slot.next
            bucket = bucket.next
        return result
