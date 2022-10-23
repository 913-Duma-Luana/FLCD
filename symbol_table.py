class SymbolTable:

    # Create empty list of given size, filled with "buckets"
    # A bucket is a linked list that can contain any element
    def __init__(self, size):
        self.size = size
        self.hash_map = self.create_buckets()

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
        bucket = self.hash_map[hashed_key]

        found_key = False
        for index, value in enumerate(bucket):
            # check if the bucket already contains the value to be added
            if value == val:
                found_key = True
                break

        if not found_key:
            bucket.append(val)

    def get(self, val):
        # Get the index from the key using hash function
        hashed_key = self.hash(val)

        # Get the bucket corresponding to index
        bucket = self.hash_map[hashed_key]

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
            return "No record found"

    # Remove a value with specific key
    def delete(self, val):

        # Get the index from the key using hash function
        hashed_key = self.hash(val)

        # Get the bucket corresponding to index
        bucket = self.hash_map[hashed_key]

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
        return "".join(str(item) for item in self.hash_map)

