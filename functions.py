# Marc
import datetime
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

# insert and update key, value information with O(1) complexity
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

# retrieves value from hash table with O(1) complexity
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

    def update_val_with_address(self, key_to_update, address_to_search, new_val):
        for i in range(1, self.size):
            package_id, package_details = hash_table.get_val(i)
            if package_details['delivery_address'] == address_to_search:
                package_details[key_to_update] = new_val

# This dunder method prints string representation of hash_table
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)


class Truck:

    def __init__(self, s_time):
        self.start_time = s_time
        self.truck_cargo = []
        self.address_list = []

# These methods load packages from hash map to the truck_cargo of truck object, and loads the addresses to the address_list.
    def load_truck(self, list):
        package_list = list
        for i in range(len(list)):
            self.truck_cargo.append(hash_table.get_val(package_list[i]))
            package_id, package_info = self.truck_cargo[i]
            self.address_list.append(package_info['delivery_address'])

# this method adds the truck objects time it leaves from the hub to the time between each delivery address and
# updates the route_list to show the accumulated time (time it arrives at address)
    def add_truck_time(self, route_list):
        h, m, s = self.start_time.split(":")
        acc_time_delta = datetime.timedelta(hours=int(h), minutes=int(m),seconds=int(s))
        for t in range(len(route_list)):
            hour, minute, second = route_list[t][1].split(':')
            t_delta = datetime.timedelta(hours=int(hour), minutes=int(minute), seconds=int(second))
            acc_time_delta = acc_time_delta + t_delta
            route_list[t][1] = str(acc_time_delta)

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

def sum_of_route(total_traveled):
    sum = 0
    for i in range(len(total_traveled)):
        sum += total_traveled[i][0]
    return sum

def calc_distance_of_all_routes():
    distance_of_routes = round(truck_1_total_dist + truck_2_total_dist + truck_3_total_dist, 2)
    return distance_of_routes

def change_del_status_to_1(vertices_list, package_address_list):
    for i in range(number_of_vertices):
        if vertices_list[i][0] not in package_address_list:
            vertices_list[i][1] = 1
    vertices_list[0][1] = 0

def reset_del_status():
    for i in range(number_of_vertices):
        vertices[i][1] = 0

def calculate_time(distance):
    speed = 18
    float_time = distance/speed
    time_in_seconds = float_time * 60 * 60
    minutes, seconds = divmod(time_in_seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%02d:%02d:%02d" % (hours, minutes, seconds)

def find_packages_for_address():
    temp_list = []
    for i in range(1, packages_plus_one):
        temp_list.append(hash_table.get_val(i))
        package_id, package_details = temp_list[i-1]
        if package_details['delivery_address'] in package_delivered_list:
            package_details['delivery_status'] = 'delivered'
            print(package_id, package_details, '\n')
        else:
            print(package_id, package_details, '\n')

def compare_user_input_to_times(user_input):
    hr, min, sec = user_input.split(":")
    time_user_input = datetime.time(hour=int(hr), minute=int(min), second=int(sec))
    for i in range(len(combined_route_list)):
        hour, minute, second = combined_route_list[i][1].split(":")
        time_to_compare = datetime.time(hour=int(hour), minute=int(minute), second=int(second))
        if time_user_input >= time_to_compare:
            package_delivered_list.append(combined_route_list[i][0])
            print(f"append {time_to_compare} to text file")

################################ Program Script Below ################################ transfer to main later

# creates hash table with 41 buckets to avoid collisions since there are 40 packages
packages_plus_one = 41
hash_table = HashTable(packages_plus_one)

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

# three empty lists for delivery address and time delivered
route_list_1 = []
route_list_2 = []
route_list_3 = []
# three empty lists for distance traveled between points and index on edges matrix index traveled to for each truck
total_traveled_1 = []
total_traveled_2 = []
total_traveled_3 = []

# empty lists for time of deliveries and delivery location
delivery_time_1 = []

# this prints the matrix in a more readable format
# for k in range(len(edges)):
#     print(f"{k}  {edges[k]} \n")

# lists of package IDs for each trip and truck according to the special notes. All special criteria has been met and verified.
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
truck_1.add_truck_time(route_list_1)

# similar to block of code above but the truck object and lists are different
truck_2.load_truck(package_list_trip_2)
truck_2_address_list = truck_2.address_list
truck_2_address_list = list(set(truck_2_address_list))
truck_2_address_list_size = len(truck_2_address_list)
change_del_status_to_1(vertices, truck_2_address_list)
find_create_minimum_route(0, truck_2_address_list_size, route_list_2, total_traveled_2)
reset_del_status()
truck_2_total_dist = sum_of_route(total_traveled_2)
truck_2.add_truck_time(route_list_2)

# similar to block of code above but the truck object and lists are different
truck_3.load_truck(package_list_trip_3)
truck_3_address_list = truck_3.address_list
truck_3_address_list = list(set(truck_3_address_list))
truck_3_address_list_size = len(truck_3_address_list)
change_del_status_to_1(vertices, truck_3_address_list)
find_create_minimum_route(0, truck_3_address_list_size,route_list_3, total_traveled_3)
reset_del_status()
truck_3_total_dist = sum_of_route(total_traveled_3)
truck_3.add_truck_time(route_list_3)

# this is the total distance of all three truck routes
# please uncomment line below to see total miles traveled for all routes
# print(calc_distance_of_all_routes())

# this block of code combines all the route_lists into one list called combined_route_list
combined_route_list = route_list_3.copy()
combined_route_list.extend(route_list_2)
combined_route_list.extend(route_list_1)


# print(route_list_1,'\n')
# print(total_traveled_1,'\n')
# print(truck_1_total_dist,'\n\n')
# print(route_list_2,'\n')
# print(total_traveled_2,'\n')
# print(truck_2_total_dist,'\n\n')
# print(route_list_3,'\n')
# print(total_traveled_3,'\n')
# print(truck_3_total_dist,'\n')
# print(distance_of_routes)

# empty list for the addresses delivered to before the user input time
package_delivered_list = []

hash_table.update_val_with_address('delivery_status', '5025 State St', 'in route')
print(hash_table.get_val(24))

# Block of code create user menu to intereact with the program
# user_input = ""
# while user_input != 'exit':
#     print("To see the delivery status of packages at any given time, please enter the time in HH:MM:SS format. \
# To exit the application, please enter 'exit'")
#     pattern = re.compile(r'\d\d:\d\d:\d\d')
#     user_input = input("Please enter a time in HH:MM:SS format to see status of all packages: ")
#     if pattern.search(user_input):
#         compare_user_input_to_times(user_input)
#         find_packages_for_address()
#     elif pattern.search(user_input) == None and user_input != 'exit':
#         print("incorrect format. Please try again")
