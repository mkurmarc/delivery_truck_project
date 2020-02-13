# Marc
from time import time
import re
import sys
import csv

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

# create update function for hashmap
    def update_val(self):
        pass

# This dunder method prints string representation of hash_table
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)


class Truck:

    def __init__(self, s_time):
        self.start_time = s_time
        self.acc_time = s_time
        self.truck_cargo = []
        self.address_list = []

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

# These methods load packages from hash map to the truck_cargo of truck object, and
# loads the addresses to the address_list. The 1,2,3 means the 1st, 2nd, or 3rd trip.
# It is going to take a toal of three truck routes/trips to deliver all the packages
    def load_truck_1(self, list):
        package_list = list
        for i in range(len(list)):
            self.truck_cargo.append(hash_table.get_val(package_list[i]))
            package_id, package_info = truck_1.truck_cargo[i]
            self.address_list.append(package_info['delivery_address'])

    def load_truck_2(self, list):
        package_list = list
        for i in range(len(list)):
            self.truck_cargo.append(package_list[i])

    def load_truck_3(self, list):
        package_list = list
        for i in range(len(list)):
            self.truck_cargo.append(package_list[i])

def find_min(start):
    minimum = 1000
    for i in range(number_of_vertices):
        if edges[start][i] < minimum and vertices[i][1] == 0:
            minimum = edges[start][i]
            start = i
    total_traveled.append([minimum, start])
    route_list.append(vertices[start][0])
    vertices[start][1] = 1
    return start


################################ Program Script Below ################################ transfer to main later

route_list = []
total_traveled = []

# creates hash table with 41 buckets to avoid collisions
hash_table = HashTable(41)

# This reads file line by line and creates a dictionary of packages' info. Then inputs the dictionary into the hash table with set_val method.
# Also, this block of code appends all street_address to empty vertices
with open("package_file.txt") as f:
    for line in f:
        line = line.strip('\n')
        package_key, street_address, city, state, zip_code, delivery_deadline, weight, special_note = line.split(",")
        delivery_status = 'hub'
        value = {'delivery_address':street_address, 'city':city,
                 'state':state, 'zip_code':zip_code, 'delivery_deadline':delivery_deadline,
                 'package_weight':weight, 'special_note':special_note, 'delivery_status':delivery_status}
        hash_table.set_val(int(package_key), value)



# creates empty map matrix to be use for distances between addresses
edges = []

# this block of code reads in the csv file of distances and appends to edges to create a matrix
with open('wgups_distance_table_headers.csv', 'r') as csv_dist_file:
    csv_reader = csv.reader(csv_dist_file)
    vertices = next(csv_reader)
    for line in csv_reader:
        line = list(map(float, line))
        edges.append(line)

# used list comprehension to make a list of lists with vertices/addresses and 0 in each list. 0 means not visited.
vertices = [[index,0] for index in vertices]

# stores number of vertices in the vertices
number_of_vertices = len(vertices)

print(find_min(0))

print(total_traveled, route_list)
# print(edges)
print(vertices)
# print(number_of_vertices)


# lists of package IDs for each trip and truck. They are sorted too.
package_list_trip_1 = [13, 14, 15, 16, 19, 20, 1, 29, 30, 34, 40, 7, 8, 4, 39, 21]
package_list_trip_1 = sorted(package_list_trip_1)

package_list_trip_2 = [31, 32, 37, 38, 5, 3, 18, 36, 6, 25, 26, 28, 2, 33, 27, 35]
package_list_trip_2 = sorted(package_list_trip_2)

package_list_trip_3 = [9, 10, 11, 12, 17, 22, 23, 24]
package_list_trip_3 = sorted(package_list_trip_3)

# create truck objects
truck_1 = Truck('08:00:00')
truck_2 = Truck('09:05:00')
truck_3 = Truck('10:20:00')

# print(vertices)
# print(hash_table)
# print(edges)
# print(vertices)

# all three trucks are loaded with the packages according to the special notes. Packages now in truck_cargo
truck_1.load_truck_1(package_list_trip_1)
truck_2.load_truck_2(package_list_trip_2)
truck_3.load_truck_3(package_list_trip_3)

# print(truck_1.address_list)
# print(vertices.index(truck_1.address_list[0]))

# Calling function calculate_time() using rate of 18 mph
# print("The calculated time is", truck_1.calculate_time(100, 18)); # 1st parameter can be a variable received from algorithm
