# Marc
class HashTable:

# initializes the object and creates the empty hash table with empty buckets
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

# creates the empty buckets
    def create_buckets(self):
        return [[] for _ in range(self.size)]

# insert and update key, value information with O(N) complexity
    def set_val(self, key, value):
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

# retrieves value from hash table with O(N) complexity
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

# This dunder method prints string representation of hash_table
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)


class CreateDict:

# initializes the object with empty dictionary
    def __init__(self):
        self.dictionary = {}

    def add_to_dict(self, key, index):
        if key in self.dictionary:
            list_of_indices = [self.dictionary[key],index]
            self.dictionary[key] = list_of_indices
        else:
            self.dictionary[key] = index

# This dunder method prints string representation of dictionary
    def __str__(self):
        return str(self.dictionary)



################################ Program Script Below ################################ transfer to main later

# creates hash table
hash_table = HashTable(100)

# creates empty map matrix to be use for distances between addresses
map_matrix = []

# creates empty address dictionary that will be used to map an address to its corresponding index to the list in the map matrix
address_dictionary = CreateDict()

# this reads file line by line and creates a dictionary of packages' info. Then inputs the dictionary into the hash table with set_val method
with open("package_file.txt") as f:
    for line in f:
        line = line.strip('\n')
        package_key, street_address, city, state, zip_code, delivery_deadline, weight, special_note = line.split(",")
        delivery_status = 'hub'
        address_dictionary.add_to_dict(street_address, package_key)
        value = {'delivery_address':street_address, 'city':city,
                 'state':state, 'zip_code':zip_code, 'delivery_deadline':delivery_deadline,
                 'package_weight':weight, 'special_note':special_note, 'delivery_status':delivery_status}
        hash_table.set_val(package_key, value)

# this reads distance file line by line and fills the empty map matrix
with open("wgups_distance_table.txt") as f:
    for line in f:
        line = line.strip('\n')
        row = line.split(" ")
        map_matrix.append(row)



# print(hash_table.get_val('1'))
# print(hash_table)
# print(map_matrix)
print(address_dictionary) # the reason the index is off is because the street addresses have duplicates
                          # and keys of dictionaries are unique. The address gets assigned to the last
                          # address of the duplicates. That is why there are fewer than 40 entries into
                          # the dictionary
