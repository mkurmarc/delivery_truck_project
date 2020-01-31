# Marc
class AlgoHashTable:

    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_cans()

    def create_cans(self):
        return [[] for _ in range(self.size)]

    def set_val(self, key, value): # insert and update method
        hashed_key = hash(key)%self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket[index] = (key, value)
        else:
            bucket.append((key, value)) # appending stops collisions from happening
