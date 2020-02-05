# Marc
class AlgoHashTable:

    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
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

    def get_val(self, key):
        hashed_key = hash(key)%self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            return record_value
        else:
            return "No record found with that email address"

    def __str__(self):
        return "".join(str(item) for item in self.hash_table)

class Map:

    def open_package_file(self, file):
        pass

    def open_distance_file(self, file):
        pass

    def print_map(self, map):
        pass


################################ Program Script Below ################################ transfer to main later

# creates hash table
hash_table = AlgoHashTable(100)
map_matrix = []

# this reads file line by line and inputs it into the hash table with set_val method
with open("package_file.txt") as f:
    for line in f:
        key, street_address, city, state, zip_code, delivery_deadline, weight, special_note = line.split(",")
        delivery_status = 'hub'
        if special_note.endswith('\n'):
            special_note = special_note.replace('\n','')
        value = {'delivery_address':street_address, 'city':city,
                 'state':state, 'zip_code':zip_code, 'delivery_deadline':delivery_deadline,
                 'package_weight':weight, 'special_note':special_note, 'delivery_status':delivery_status}
        hash_table.set_val(key, value)

# print(hash_table.get_val('1'))
# print(hash_table)

with open("wgups_distance_table.txt") as f:
    for line in f:
        line = line.strip('\n')
        row = line.split(" ")
        map_matrix.append(row)




print(map_matrix)
