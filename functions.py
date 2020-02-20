# Marc Rios ID 787989
import datetime
import re
import csv

class HashTable:

# Initializes the object and creates the empty hash table with empty buckets
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

# Creates the empty buckets. O(n) time complexity
    def create_buckets(self):
        return [[] for _ in range(self.size)]

# Insert and update key, value information with O(n) complexity
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
            bucket[index] = [key, value]
        else:
            bucket.append([key, value]) # appending stops collisions from happening

# Retrieves value from hash table with O(n) complexity
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
            return [record_key, record_value]
        else:
            return "No package found with that key"

# Updates inputed key of dictionary with inputed value using the address to search.
# O(n) time complexity
    def update_val_with_address(self, key_to_update, address_to_search, new_val):
        for i in range(1, self.size):
            package_id, package_details = hash_table.get_val(i)
            if package_details['delivery_address'] == address_to_search:
                package_details[key_to_update] = new_val

# This dunder method prints string representation of hash_table
    def __str__(self):
        return "\n\n".join(str(item) for item in self.hash_table)


class Truck:

# This initializes the truck object
    def __init__(self, s_time):
        self.start_time = s_time
        self.address_list = []

# These methods load packages from hash map to the truck_cargo of truck object,
# and loads the addresses to the address_list. O(n) time complexity
    def load_truck(self, list):
        package_list = list
        for i in range(len(list)):
            package_id, package_info = hash_table.get_val(package_list[i])
            package_info['delivery_status'] = 'in route'
            self.address_list.append(package_info['delivery_address'])

# This method adds the truck objects time it leaves from the hub to the time between
# each delivery address and updates the route_list to time it arrives at the address.
# O(n) time complexity.
    def add_truck_start_time(self, route_list):
        h, m, s = self.start_time.split(":")
        acc_time_delta = datetime.timedelta(hours=int(h), minutes=int(m),seconds=int(s))
        for t in range(len(route_list)):
            hour, minute, second = route_list[t][1].split(':')
            t_delta = datetime.timedelta(hours=int(hour), minutes=int(minute), seconds=int(second))
            acc_time_delta = acc_time_delta + t_delta
            route_list[t][1] = str(acc_time_delta)

# This mthod changes the string representation of time into datetime comparable object.
# O(1) time complexity.
    def truck_tstring_to_time(self):
        t_hr, t_min, t_sec = self.start_time.split(":")
        truck_time = datetime.time(hour=int(t_hr), minute=int(t_min), second=int(t_sec))
        return truck_time

# 1) Select a start point, the hub address
# 2) Find the nearest unvisited address and go there
# 3) Mark the current address as visited
# 4) Are there any unvisited addresses? If yes, go to step 2
# 5) Return to the starting start, the hub
# find_min_distance and find_create_minimum_route work together to create the algorithm Nearest Neighbor described in steps above
# Time-complexity is O(N2log2(N)) iterations, where N is the number of addresses to be visited
def find_min_distance(start, route_empty, traveled_empty):
    minimum = 1000
    global new_v
    for i in range(number_of_vertices):
        if edges[start][i] <= minimum and vertices[i][1] == 0:
            minimum = edges[start][i]
            new_v = i
    traveled_empty.append([minimum, new_v])
    route_empty.append([vertices[new_v][0], calculate_time(minimum)])
    vertices[start][1] = 1
    return new_v, route_empty, traveled_empty

def find_create_minimum_route(start, address_list_size, route_empty, traveled_empty):
    while len(traveled_empty) < address_list_size:
        if len(traveled_empty) == 0:
            next_dest, route_empty, traveled_empty = find_min_distance(start, route_empty, traveled_empty)
        next_dest, route_empty, traveled_empty = find_min_distance(next_dest, route_empty, traveled_empty)
        if len(traveled_empty) == address_list_size:
            traveled_empty.append([edges[next_dest][0],0])
            last_distance = traveled_empty[len(traveled_empty)-1][0]
            route_empty.append([vertices[0][0], calculate_time(last_distance)])
            vertices[next_dest][1] = 1

# This function calculates the sum of the passed in route traveled. O(n) time complexity.
def sum_of_route(total_traveled):
    sum = 0
    for i in range(len(total_traveled)):
        sum += total_traveled[i][0]
    return sum

# This function calculates the total of all truck routes traveled. O(1) time complexity.
def calc_distance_of_all_routes():
    distance_of_routes = round(truck_1_total_dist + truck_2_total_dist + truck_3_total_dist, 2)
    return distance_of_routes

# Changes the visted/unvisited element of vertices list to only visited aka 1
# O(n) time complexity
def change_del_status_to_1(vertices_list, package_address_list):
    for i in range(number_of_vertices):
        if vertices_list[i][0] not in package_address_list:
            vertices_list[i][1] = 1
    vertices_list[0][1] = 0

# Changes the visted/unvisited element of vertices list to only unvisited aka 0
# O(n) time complexity
def reset_del_status():
    for i in range(number_of_vertices):
        vertices[i][1] = 0

# Calculates the time it takes to get somewhere given the distance and speed and
# returns 00:00:00 format. O(1) time complexity
def calculate_time(distance):
    speed = 18
    float_time = distance/speed
    time_in_seconds = float_time * 60 * 60
    minutes, seconds = divmod(time_in_seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%02d:%02d:%02d" % (hours, minutes, seconds)

# Compares the user input time to the combined_route_list to determine which items have
# been delivered, are in route, or at hub. O(n^2) time complexity.
def compare_times_and_update_status(user_input):
    hr, min, sec = user_input.split(":")
    time_user_input = datetime.time(hour=int(hr), minute=int(min), second=int(sec))
    time_t1, time_t2, time_t3 = truck_1.truck_tstring_to_time(), truck_2.truck_tstring_to_time(), truck_3.truck_tstring_to_time()
    t1_addresses, t2_addresses, t3_addresses = truck_1.address_list, truck_2.address_list, truck_3.address_list
    for i in range(len(combined_route_list)):
        hour, minute, second = combined_route_list[i][1].split(":")
        time_to_compare = datetime.time(hour=int(hour), minute=int(minute), second=int(second))
        if time_user_input >= time_to_compare:
            hash_table.update_val_with_address('delivery_status', combined_route_list[i][0], f'delivered at {time_to_compare}')
        if i < len(t1_addresses) and time_user_input < time_t1:
            hash_table.update_val_with_address('delivery_status', t1_addresses[i], 'at hub')
        if i < len(t2_addresses) and time_user_input < time_t2:
            hash_table.update_val_with_address('delivery_status', t2_addresses[i], 'at hub')
        if i < len(t3_addresses) and time_user_input < time_t3:
            hash_table.update_val_with_address('delivery_status', t3_addresses[i], 'at hub')

################################ Program Script Below ################################
# creates hash table with 41 buckets to avoid collisions since there are 40 packages
hash_table = HashTable(41)
# This reads file line by line and creates a dictionary of packages' info. Then inputs the
# dictionary into the hash table with set_val method. O(n) time complexity
with open("package_file.txt") as f:
    for line in f:
        line = line.strip('\n')
        package_key, street_address, city, state, zip_code, delivery_deadline, weight, special_note = line.split(",")
        delivery_status = 'hub'
        value = {'delivery_address':street_address, 'city':city,
                 'state':state, 'zip_code':zip_code, 'delivery_deadline':delivery_deadline,
                 'package_weight':weight, 'special_note':special_note, 'delivery_status':delivery_status}
        hash_table.set_val(int(package_key), value)

# Creates empty list that will be filled with other lists to create an adjacency matrix
# to be use for distances between addresses
edges = []
# This block of code reads in the csv file of distances and appends to edges to
# create the matrix. Also, it creates list of addresses under vertices list.
# O(n) time complexity
with open('wgups_distance_table_headers.csv', 'r') as csv_dist_file:
    csv_reader = csv.reader(csv_dist_file)
    vertices = next(csv_reader)
    for line in csv_reader:
        line = list(map(float, line))
        edges.append(line)

# Used list comprehension to make a list of lists with vertices/addresses and 0 in each list.
# 0 means not visited.
vertices = [[index,0] for index in vertices]
# Stores number of vertices in the vertices
number_of_vertices = len(vertices)

# Three empty lists for delivery address and time delivered
route_list_1 = []
route_list_2 = []
route_list_3 = []
# Three empty list for each truck. Each that will hold a list of 2 elements.
# Distance traveled, index on edges matrix
total_traveled_1 = []
total_traveled_2 = []
total_traveled_3 = []

# lists of package IDs for each trip and truck according to the special notes. All
# special criteria has been met and verified.
package_list_trip_1 = [13, 14, 15, 16, 19, 20, 1, 29, 30, 34, 40, 7, 8, 4, 39, 21]
package_list_trip_2 = [31, 32, 37, 38, 5, 3, 18, 36, 6, 25, 26, 28, 2, 33, 27, 35]
package_list_trip_3 = [9, 10, 11, 12, 17, 22, 23, 24]

# Creates 3 truck objects
truck_1 = Truck('08:00:00')
truck_2 = Truck('09:05:00')
truck_3 = Truck('10:20:00')

# Truck 1 is loaded with the packages. Packages now in truck_cargo
truck_1.load_truck(package_list_trip_1)
# These two lines of code remove duplicate addresses from the truck_1 address list
truck_1_address_list = truck_1.address_list
truck_1_address_list = list(set(truck_1_address_list))
# Saves size of non-duplicate list
truck_1_address_list_size = len(truck_1_address_list)
# Below this changes vertices that are not in the truck_1_address_list to visited aka 1
change_del_status_to_1(vertices, truck_1_address_list)
# Below this finds the minimum distance route using Nearest Neighbor technique
find_create_minimum_route(0, truck_1_address_list_size, route_list_1, total_traveled_1)
# Below this resets all vertices to unvisited aka 0
reset_del_status()
# Code block saves the sum of truck_1 route, its address route, and distance
# traveled between each index/address
truck_1_total_dist = sum_of_route(total_traveled_1)
truck_1.add_truck_start_time(route_list_1)

# similar to block of code above but the truck object and lists are different
truck_2.load_truck(package_list_trip_2)
truck_2_address_list = truck_2.address_list
truck_2_address_list = list(set(truck_2_address_list))
truck_2_address_list_size = len(truck_2_address_list)
change_del_status_to_1(vertices, truck_2_address_list)
find_create_minimum_route(0, truck_2_address_list_size, route_list_2, total_traveled_2)
reset_del_status()
truck_2_total_dist = sum_of_route(total_traveled_2)
truck_2.add_truck_start_time(route_list_2)

# similar to block of code above but the truck object and lists are different
truck_3.load_truck(package_list_trip_3)
truck_3_address_list = truck_3.address_list
truck_3_address_list = list(set(truck_3_address_list))
truck_3_address_list_size = len(truck_3_address_list)
change_del_status_to_1(vertices, truck_3_address_list)
find_create_minimum_route(0, truck_3_address_list_size,route_list_3, total_traveled_3)
reset_del_status()
truck_3_total_dist = sum_of_route(total_traveled_3)
truck_3.add_truck_start_time(route_list_3)

# To see each individual truck's distance please uncomment the three lines below
# print(truck_1_total_dist)
# print(truck_2_total_dist)
# print(truck_3_total_dist)

# This is the total distance of all three truck routes
# please uncomment line below to see total miles traveled for all routes
# print(calc_distance_of_all_routes())

# This block of code combines all the route_lists into one list called combined_route_list
combined_route_list = route_list_3.copy()
combined_route_list.extend(route_list_2)
combined_route_list.extend(route_list_1)

# Block of code creates simple user interface to intereact with the program
user_input = ""
while user_input != 'exit':
    print("To see the delivery status of packages at any given time, please enter the time in HH:MM:SS format. \
To exit the application, please enter 'exit'")
    pattern = re.compile(r'\d\d:\d\d:\d\d')
    user_input = input("Please enter a time in HH:MM:SS format to see status of all packages: ")
    if pattern.search(user_input):
        compare_times_and_update_status(user_input)
        print(hash_table, "\n\n")
    elif pattern.search(user_input) == None and user_input != 'exit':
        print("Incorrect format. Please try again")
