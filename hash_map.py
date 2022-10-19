class HashMap:
    # Create empty bucket list of given size
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

    # Insert values into hash map
    def set_val(self, val):

        # Get the index from the key
        hashed_key = self.hash(val)

        # Get the bucket corresponding to index
        bucket = self.hash_map[hashed_key]

        found_key = False
        index = 0
        for index, key in enumerate(bucket):

            # check if the bucket has same key as
            # the key to be inserted
            if key == val:
                found_key = True
                break

        # If the bucket has same key as the key to be inserted,
        # Update the key value
        # Otherwise append the new key-value pair to the bucket
        if not found_key:
            bucket.append(val)

    # Return searched value with specific key
    def get_val(self, key):

        # Get the index from the key using
        # hash function
        hashed_key = self.hash(key)

        # Get the bucket corresponding to index
        bucket = self.hash_map[hashed_key]

        found_key = False
        for index, val in enumerate(bucket):

            # check if the bucket has same key as
            # the key being searched
            if val == key:
                found_key = True
                break

        # If the bucket has same key as the key being searched,
        # Return the value found
        # Otherwise indicate there was no record found
        if found_key:
            return val
        else:
            return "No record found"

    # Remove a value with specific key
    def delete_val(self, key):

        # Get the index from the key using
        # hash function
        hashed_key = self.hash(key)

        # Get the bucket corresponding to index
        bucket = self.hash_map[hashed_key]

        found_key = False
        for index, val in enumerate(bucket):
            # check if the bucket has same key as
            # the key to be deleted
            if val == key:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
        return

    # To print the items of hash map
    def __str__(self):
        return "".join(str(item) for item in self.hash_map)

