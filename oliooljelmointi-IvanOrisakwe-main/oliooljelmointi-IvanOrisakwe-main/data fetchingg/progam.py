import module

def main():
    input_filename = input("Enter the filename to read: ")
    file_contents = module.read_file(input_filename)

 
    data_set = module.create_set(file_contents)

    data_list = module.create_list(data_set)

    dict_list = module.create_dictionary(data_list)


    user_objects = []
    for person_dict in dict_list:
        user = module.User(
            name=person_dict["Name"],
            email=person_dict["email"],
            ip=person_dict["IP"]
        )
        user_objects.append(user)


    output_filename = input("Enter the filename to write user info: ")
    with open(output_filename, 'w') as file:
        for user in user_objects:
            file.write(f"The person's name is {user.name}, email {user.email} and IP address: {user.ip}\n")

if __name__ == "__main__":
    main()