# Marc
from time import time
import re
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
    def load_truck(self, list):
        package_list = list
        for i in range(len(list)):
            self.truck_cargo.append(hash_table.get_val(package_list[i]))
            package_id, package_info = self.truck_cargo[i]
            self.address_list.append(package_info['delivery_address'])

def find_create_minimum_route(start, address_list_size, route_empty, traveled_empty):
    while len(traveled_empty) < address_list_size:
        if len(traveled_empty) == 0:
            next_dest, route_empty, traveled_empty = find_min_distance(start, route_empty, traveled_empty)
        next_dest, route_empty, traveled_empty = find_min_distance(next_dest, route_empty, traveled_empty)
        if len(traveled_empty) == address_list_size:
            traveled_empty.append([edges[next_dest][0],0]) # this line return last index to hub
            route_empty.append([vertices[0][0],0])
            vertices[next_dest][1] = 1

def find_min_distance(start, route_empty, traveled_empty):
    minimum = 1000
    global new_v
    for i in range(number_of_vertices):
        if edges[start][i] <= minimum and vertices[i][1] == 0:
            minimum = edges[start][i]
            new_v = i
    traveled_empty.append([minimum, new_v])
    route_empty.append([vertices[new_v][0], new_v])
    vertices[start][1] = 1
    return new_v, route_empty, traveled_empty

def sum_of_route(total_traveled):
    sum = 0
    for i in range(len(total_traveled)):
        sum += total_traveled[i][0]
    return sum

def change_del_status_to_1(vertices_list, package_address_list):
    for i in range(number_of_vertices):
        if vertices_list[i][0] not in package_address_list:
            vertices_list[i][1] = 1
    vertices_list[0][1] = 0

def reset_del_status():
    for i in range(number_of_vertices):
        vertices[i][1] = 0


################################ Program Script Below ################################ transfer to main later

# creates hash table with 41 buckets to avoid collisions
hash_table = HashTable(41)

# This reads file line by line and creates a dictionary of packages' info. Then inputs the dictionary into the hash table with set_val method.
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

# three empty lists for address, index of address on matrix. This will show the path from address to address for each truck
route_list_1 = []
route_list_2 = []
route_list_3 = []
# three empty lists for distance traveled between points, index traveled to for each truck
total_traveled_1 = []
total_traveled_2 = []
total_traveled_3 = []

# this prints the matrix in a more readable format
# for k in range(len(edges)):
#     print(f"{k}  {edges[k]} \n")

# lists of package IDs for each trip and truck according to the special notes
package_list_trip_1 = [13, 14, 15, 16, 19, 20, 1, 29, 30, 34, 40, 7, 8, 4, 39, 21]
package_list_trip_2 = [31, 32, 37, 38, 5, 3, 18, 36, 6, 25, 26, 28, 2, 33, 27, 35]
package_list_trip_3 = [9, 10, 11, 12, 17, 22, 23, 24]

# create truck objects
truck_1 = Truck('08:00:00')
truck_2 = Truck('09:05:00')
truck_3 = Truck('10:20:00')

# truck 1 is loaded with the packages. Packages now in truck_cargo
truck_1.load_truck(package_list_trip_1)

# these two lines of code remove duplicate addresses from the truck_1 address list
truck_1_address_list = truck_1.address_list
truck_1_address_list = list(set(truck_1_address_list))
# saves size of non-duplicate list
truck_1_address_list_size = len(truck_1_address_list)
# below this changes vertices that are not in the truck_1_address_list to visited aka 1
change_del_status_to_1(vertices, truck_1_address_list)
# below this finds the minimum distance route using Nearest Neighbor technique
find_create_minimum_route(0, truck_1_address_list_size, route_list_1, total_traveled_1)
# below this resets all vertices to unvisited aka 0
reset_del_status()
# code block saves the sum of truck_1 route, its address route, and distance traveled between each index/address
truck_1_total_dist = sum_of_route(total_traveled_1)

# truck 2 is loaded with the packages. Packages now in truck_cargo
truck_2.load_truck(package_list_trip_2)
# these two lines of code remove duplicate addresses from the truck_2 address list
truck_2_address_list = truck_2.address_list
truck_2_address_list = list(set(truck_2_address_list))
# saves size of non-duplicate list
truck_2_address_list_size = len(truck_2_address_list)
# below this changes vertices that are not in the truck_1_address_list to visited aka 1
change_del_status_to_1(vertices, truck_2_address_list)
# below this finds the minimum distance route using Nearest Neighbor technique
find_create_minimum_route(0, truck_2_address_list_size, route_list_2, total_traveled_2)
# below this resets all vertices to unvisited aka 0
reset_del_status()
# sum of the route
truck_2_total_dist = sum_of_route(total_traveled_2)

# truck 3 is loaded with the packages. Packages now in truck_cargo
truck_3.load_truck(package_list_trip_3)
# these two lines of code remove duplicate addresses from the truck_2 address list
truck_3_address_list = truck_3.address_list
truck_3_address_list = list(set(truck_3_address_list))
# saves size of non-duplicate list
truck_3_address_list_size = len(truck_3_address_list)
# below this chang es vertices that are not in the truck_3_address_list to visited aka 1
change_del_status_to_1(vertices, truck_3_address_list)
# below this finds the minimum distance route using Nearest Neighbor technique
find_create_minimum_route(0, truck_3_address_list_size,route_list_3, total_traveled_3)
# below this resets all vertices to unvisited aka 0
reset_del_status()
# sum of the route
truck_3_total_dist = sum_of_route(total_traveled_3)

# this is the total distance of all three truck routes
distance_of_routes = round(truck_1_total_dist + truck_2_total_dist + truck_3_total_dist, 2)

# print(route_list_1,'\n')
# print(total_traveled_1,'\n')
# print(truck_1_total_dist,'\n\n')
# print(route_list_2,'\n')
# print(total_traveled_2,'\n')
# print(truck_2_total_dist,'\n\n')
# print(route_list_3,'\n')
# print(total_traveled_3,'\n')
# print(truck_3_total_dist,'\n')

print(distance_of_routes)
# Calling function calculate_time() using rate of 18 mph
# print("The calculated time is", truck_1.calculate_time(100, 18)); # 1st parameter can be a variable received from algorithm
