# Creating a dictionary
hashmap = {
    'apple': 3,
    'banana': 5,
    'orange': 2,
    'mango': 7,
    'grape': 4
}

# Using get to retrieve values
apple_quantity = hashmap.get('apple')
print("Quantity of apples:", apple_quantity)  # Output: Quantity of apples: 3

# Using get to retrieve a value with a default if the key is not found
pineapple_quantity = hashmap.get('pineapple', 0)
print("Quantity of pineapples:", pineapple_quantity)  # Output: Quantity of pineapples: 0

# Using get without providing a default (will return None if key is not found)
kiwi_quantity = hashmap.get('kiwi')
print("Quantity of kiwis:", kiwi_quantity)  # Output: Quantity of kiwis: None


hashmap['avocado'] = 2 # Adds new key-value pair

print(hashmap) # Output: {'apple': 3, 'banana': 5, 'orange': 2, 'mango': 7, 'grape': 4, 'avocado': 2}

if 'apple' in hashmap:  # Checks if apple key is in hashmap. It checks key!, not value
    print("Apple in hashmap") # Output: apple in hashmap