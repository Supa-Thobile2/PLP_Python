# Write a program tha asks the user for their name, age and location and then print out a personalixed message
def user_input():

name = input('Enter your name: ')
print('Your name is: ', name)

age = input('Enter your age: ')
print('Your age is: ', age)

location = input('Enter your location: ')
print('Your location is: ', location)

print('Hello ${name}, you are ${age} years old and live in ${location}')