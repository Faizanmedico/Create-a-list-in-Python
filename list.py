
#  1. Create a list:

my_list = [1, 2, 3, "apple", True]
print(my_list)  # Output: [1, 2, 3, 'apple', True]

my_list = ["apple", "banana", "cherry"]
print(my_list[0])  # Output: apple (pehla item)
print(my_list[1])  # Output: banana (doosra item)
print(my_list[2])  # Output: cherry (teesra item)

# Negative indexing last se shuru hoti hai (-1 last item hai)
print(my_list[-1]) # Output: cherry
print(my_list[-2]) # Output: banana

my_list = ["apple", "banana", "cherry"]
for item in my_list:
    print(item)
# Output:
# apple
# banana
# cherry


my_list = ["apple", "banana", "cherry"]
if "banana" in my_list:
    print("Yes, 'banana' is in the list")
else:
    print("No, 'banana' is not in the list")

if "orange" not in my_list:
    print("Yes, 'orange' is not in the list")


my_list = ["apple", "banana", "cherry"]
length = len(my_list)
print(length)  # Output: 3


my_list = ["apple", "banana", "cherry"]
my_list.append("orange")
print(my_list)  # Output: ['apple', 'banana', 'cherry', 'orange']



my_list = ["apple", "banana", "cherry"]
my_list.insert(1, "mango")
print(my_list)  # Output: ['apple', 'mango', 'banana', 'cherry']


my_list = ["apple", "banana", "cherry"]
last_item = my_list.pop()
print(my_list)      # Output: ['apple', 'banana']
print(last_item)    # Output: cherry


my_list = ["apple", "banana", "cherry"]
my_list.clear()
print(my_list)  # Output: []

my_list_2 = ["apple", "banana", "cherry"]
my_list_2 = []
print(my_list_2) # Output: []



my_list = ["apple", "banana", "cherry"]
my_list.clear()
print(my_list)  # Output: []

my_list_2 = ["apple", "banana", "cherry"]
my_list_2 = []
print(my_list_2) # Output: []


my_tuple = ("apple", "banana", "cherry")
my_list_from_tuple = list(my_tuple)
print(my_list_from_tuple)  # Output: ['apple', 'banana', 'cherry']

my_string = "hello"
my_list_from_string = list(my_string)
print(my_list_from_string)  # Output: ['h', 'e', 'l', 'l', 'o']


my_list = [0, 1, 2, 3, 4, 5]
subset = my_list[1:4]  # Items index 1 se 3 tak (4 included nahi)
print(subset)  # Output: [1, 2, 3]

subset_from_start = my_list[:3] # Shuru se index 2 tak
print(subset_from_start) # Output: [0, 1, 2]

subset_to_end = my_list[3:] # Index 3 se aakhir tak
print(subset_to_end) # Output: [3, 4, 5]

