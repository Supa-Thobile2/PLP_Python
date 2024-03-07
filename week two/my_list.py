# create an empty list called my_list

my_list = []

print(my_list)

# Append the following list: 10, 20, 30, 40

for i in range(10, 50, 10):
    my_list.append(i)
print(my_list)

# Insert the value 15 at the second position on the list

my_list.insert(1, 15)
print("my new list is: ")
print(my_list)

# Extend the list with another: 50, 60, 70
extend_list = [50, 60, 70]
my_list.exttend(extend_list)
print("my extended list is: ")
print(my_list)

# Remove the last element from my_list

my_list.pop(-1)
print(my_list)

# sort the list in ascending order
print('Sort my list: ')
sorted(my_list)
print(my_list)
# find and print the index of the value 30 in my_list

print('Find the index of 30 in my list: ')
print(my_list[3])