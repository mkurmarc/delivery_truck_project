# Marc
from time import time
import re

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
            return record_key, record_value
        else:
            return "No package found with that key"

# This dunder method prints string representation of hash_table
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)


class Truck:

    def __init__(self, s_time):
        self.start_time = s_time
        self.acc_time = s_time
        self.truck_cargo = []

    def __str__(self):
        return (f"Truck's cargo includes {self.truck_cargo}\nTruck left from hub at {self.start_time}\
                \nTotal time is {self.acc_time}") # use total time to mark packages on board as either in transit, delivered, or at hub

    # function to calculate time given distance and speed. Time = Distance / Speed
    def calculate_time(self, distance, speed):
        float_time = distance/speed
        time_in_seconds = float_time * 60 * 60
        minutes, seconds = divmod(time_in_seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return "%02d:%02d:%02d" % (hours, minutes, seconds)

#SAVE THIS BELOW
    # These methods load packages from hash map to the truck_cargo of truck object. The 1,2,3 means the 1st, 2nd, or 3rd trip.
    # It is going to take a toal of three truck routes/trips to deliver all the packages
    def load_truck_1(self, package):
        package_id, package_info = package
        if package not in self.truck_cargo:
            pattern = re.compile(r'[1-9]+[1-9]+')
            match = pattern.findall(package_info['special_note'])
            if match:
                self.truck_cargo.append(package_id)
                match_1 = int(match[0])
                match_2 = int(match[1])
                if match_1 not in self.truck_cargo:
                    package_2 = hash_table.get_val(int(match[0]))
                    package_2_id, package_2_info = package_2
                    self.truck_cargo.append(package_2_id)
                if match_2 not in self.truck_cargo:
                    package_3 = hash_table.get_val(int(match[1]))
                    package_3_id, package_3_info = package_3
                    self.truck_cargo.append(package_3_id)

    def load_truck_2(self, package):
        self.truck_cargo.append(package)

    def load_truck_3(self, package):
        self.truck_cargo.append(package)



################################ Program Script Below ################################ transfer to main later

# creates hash table with 41 buckets to avoid collisions
hash_table = HashTable(41)

# creates list of vertices aka addresses, hub address is added here
hub = '4001 South 700 East'
vertex_list = [hub]

# creates empty map matrix to be use for distances between addresses
map_matrix = []

# creates truck object
truck_1 = Truck('08:00:00')
truck_2 = Truck('09:05:00')

# This reads file line by line and creates a dictionary of packages' info. Then inputs the dictionary into the hash table with set_val method.
# Also, this block of code appends all street_address to empty vertex_list
with open("package_file.txt") as f:
    for line in f:
        line = line.strip('\n')
        package_key, street_address, city, state, zip_code, delivery_deadline, weight, special_note = line.split(",")
        delivery_status = 'hub'
        value = {'delivery_address':street_address, 'city':city,
                 'state':state, 'zip_code':zip_code, 'delivery_deadline':delivery_deadline,
                 'package_weight':weight, 'special_note':special_note, 'delivery_status':delivery_status}
        hash_table.set_val(int(package_key), value)
        vertex_list.append(street_address)

# this reads distance file line by line and fills the empty map matrix . There are only 27 unique addresses
with open("wgups_distance_table.txt") as f:
    for line in f:
        line = line.strip('\n')
        row = line.split(" ")
        map_matrix.append(row)

# print(hash_table.get_val('1'))
# print(hash_table)
# print(map_matrix)
# print(vertex_list)

print(truck_1)
# print(truck_2)

for package in range(1, hash_table.size):
    truck_1.load_truck_1(hash_table.get_val(package))

# for package in range(hash_table.size):
#     package = 1
#     truck_2.load_truck_2(hash_table.get_val(package))

# truck_2.load_truck(hash_table.get_val('2'))
print(truck_1)
# print(truck_2)

# Calling function calculate_time() using rate of 18 mph
print("The calculated time is", truck_1.calculate_time(100, 18)); # 1st parameter can be a variable received from algorithm
