import math


class SymbolTable:

    # Create empty list of given size, filled with "buckets"
    # A bucket is a linked list that can contain any element
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def hash(self, key):
        skey = key
        if not isinstance(key, str):
            skey = str(key)
        sum_of_ascii_codes = sum(ord(ch) for ch in skey)
        return sum_of_ascii_codes % self.size

    def add(self, val):
        hashed_key = self.hash(val)
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, value in enumerate(bucket):
            # check if the bucket already contains the value to be added
            if value == val:
                found_key = True
                return hashed_key, index

        if not found_key:
            bucket.append(val)
        return hashed_key, len(bucket)-1

    def get(self, val):
        # Get the index from the key using hash function
        hashed_key = self.hash(val)

        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found = False
        for index, value in enumerate(bucket):

            # check if the bucket contains the value being searched
            if value == val:
                found = True
                break

        # If the bucket contains the value being searched, return it
        # Otherwise indicate there was no record found
        if found:
            return val
        else:
            return None

    # Remove a value with specific key
    def delete(self, val):

        # Get the index from the key using hash function
        hashed_key = self.hash(val)

        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found = False
        index = 0
        for index, value in enumerate(bucket):
            # check if the bucket contains the value to be deleted
            if value == val:
                found = True
                break
        if found:
            bucket.pop(index)
        return

    # To print the items of hash map
    def __str__(self):
        final_str = ""
        for i in range(len(self.hash_table)):
            item = self.hash_table[i]
            if len(item) > 0:
                final_str += str(i) + ": " + str(item) + "\n"
        return final_str

    def stringTableLook(self):
        idx = 0
        final_str = ""
        for item in self.hash_table:
            final_str += str(item) + ' '
            if idx == math.isqrt(self.size) + 1:
                final_str += '\n'
                idx = 0
            else:
                idx += 1
        return final_str