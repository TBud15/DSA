my_dict = {
    'name': 'Jim',  # 'name' - ключ, 'Алексей' - значение
    'age': 30,          # 'age' - ключ, 30 - значение
    'city': 'Kyiv'      # 'city' - ключ, 'Киев' - значение
}

allowed_counter = 0

while True:
    user_input = input("Please enter name you are searching for: ")
    if my_dict['name'] == user_input:
        print(f"Name {user_input} found")
        break
    
    elif allowed_counter == 1:
        print("One more attempt allowed")
        allowed_counter += 1
    
    elif allowed_counter == 2:
        print("No more attempts allowed.")
        break
    
    else:
        print("Name not found, please try again.")
        allowed_counter += 1






# for key,value in my_dict.items():
#     if key == 'name' and value == user_input:
#         print(f'Found {user_input} in hashmap')
#         break
#     print(f"Name was not found")