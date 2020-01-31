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

################################ Program Script Below ################################

# creates hash table
hash_table = AlgoHashTable(100)

# hash_table.set_val('1', {'delivery_address':'7454 Fhdjfhjkh Ave', 'city':'Salt Lake City',
#                          'state':'UT', 'zip_code':'91790', 'package_weight':'10',
#                          'delivery_status':'in route'})


# print(hash_table.get_val('janedoe@yohoo.com'))

# this reads file line by line and inputs it into the hash table
with open("package_file.txt") as f:
    for line in f:
        key, street_address, city, state, zip_code, weight, delivery_status = line.split(",")
        value = {'delivery_address':street_address, 'city':city,
                 'state':state, 'zip_code':zip_code, 'package_weight':weight,
                 'delivery_status':delivery_status}
        hash_table.set_val(key, value)

print(hash_table)
