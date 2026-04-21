import random

def read_file(filename):
    while True:
        try:
            with open(filename, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            filename = input("Please enter a valid filename: ")

def create_set(file_contents):
    return set(line.strip() for line in file_contents if line.strip())

def create_list(data_set):
    # Convert each line into a list of components
    result = [item.split() for item in data_set]
    random.shuffle(result)
    return result

def create_dictionary(list_data):
    dict_list = []
    for person in list_data:
        person_dict = {
            "Name": person[0] + " " + person[1] if len(person) > 1 else "Not available",
            "email": person[2] if len(person) > 2 else "Not available",
            "IP": person[3] if len(person) > 3 else "Not available"
        }
        dict_list.append(person_dict)
    return dict_list

class User:
    def __init__(self, name="Not available", email="Not available", ip="Not available"):
        self.name = name
        self.email = email
        self.ip = ip

def write_to_file(user_obj, filename):
    with open(filename, 'w') as file:
        file.write(f"The person's name is {user_obj.name}, email {user_obj.email} "
                  f"and IP address: {user_obj.ip}\n")