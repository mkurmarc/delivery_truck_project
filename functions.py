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

# this function determines which of the unvisited nodes need ot be visited next
def to_be_visited():
    global visited_and_distance
    v = -10

    for index in range(number_of_vertices):
        if visited_and_distance[index][0] == 0 and (v < 0 or visited_and_distance[index][1] <= visited_and_distance[v][1]):
            v = index
    return v



################################ Program Script Below ################################ transfer to main later

# creates hash table with 41 buckets to avoid collisions
hash_table = HashTable(41)

# creates list of vertices aka addresses, hub address is added here
hub = '4001 South 700 East'
vertex_list = [hub]

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
        if street_address not in vertex_list:
            vertex_list.append(street_address)

# creates empty map matrix to be use for distances between addresses
edges = []

# this block of code reads in the csv file of distances and appends to edges to create a matrix
with open('wgups_distance_table.csv', 'r') as csv_dist_file:
    csv_reader = csv.reader(csv_dist_file)
    for line in csv_reader:
        line = list(map(float, line))
        edges.append(line)

# uses list comprehension to create a vetices map with all 1's
vertices = [[1 for x in range(len(edges))] for e in range(len(edges))]

# stores number of vetices in the vertex_list
number_of_vertices = len(vertices[0])

for element in range(number_of_vertices):
    vertices[element][element] = 0

print(vertices)

# The first element of the lists inside visited_and_distance denotes if the vertex has been visited.
# The second element of the lists inside the visited_and_distance denotes the distance from the source.
# visited_and_distance = [[0,0], [0, sys.maxsize], [0, sys.maxsize], [0, sys.maxsize]]
xyz = 0,sys.maxsize
visited_and_distance = [[xyz for x in range(len(edges))] for e in range(len(edges))]
for element in range(number_of_vertices):
    new_element = 0,0
    visited_and_distance[element][element] = new_element


for vertex in range(number_of_vertices):
    to_visit = to_be_visited() # Finding the next vertex to be visited
    for neighbor_index in range(number_of_vertices):
        # Calculating the new distance for all unvisited neighbours of the chosen vertex.
        if vertices[to_visit][neighbor_index] == 1 and visited_and_distance[neighbor_index][0] == 0:
            new_distance = visited_and_distance[to_visit][1] + edges[to_visit][neighbor_index]
            # Updating the distance of the neighbor if its current distance is greater than the distance that has just been calculated
            if visited_and_distance[neighbor_index][1] > new_distance:
                visited_and_distance[neighbor_index][1] = new_distance
        # Visiting the vertex found earlier
        visited_and_distance[to_visit][0] = 1
i = 0

# Printing out the shortest distance from the source to each vertex
for distance in visited_and_distance:
    print("The shortest distance of ",chr(ord('a') + i)," from the source vertex a is: ", distance[1])
    i = i + 1

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
# print(vertex_list)

# all three trucks are loaded with the packages according to the special notes. Packages now in truck_cargo
truck_1.load_truck_1(package_list_trip_1)
truck_2.load_truck_2(package_list_trip_2)
truck_3.load_truck_3(package_list_trip_3)

# print(truck_1.address_list)
# print(vertex_list.index(truck_1.address_list[0]))

# Calling function calculate_time() using rate of 18 mph
# print("The calculated time is", truck_1.calculate_time(100, 18)); # 1st parameter can be a variable received from algorithm
