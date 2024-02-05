my_str = "Hello, World!"

my_multiline_str = '''
this is my new line
this is another new line
this is also another new line
'''

print(my_str[1])

# this is a for loop this will
# loop through each character in a string
# and printing it out
for i in my_str:
    print(i)

my_longer_str '''
this is my multiline string
I want to show how the len() function work for the long string one
'''

# the len function will show the number of character in a string
print(len(my_longer_str))

# checking if the word "or" is nside the phrase "Hello, World"

print("or" in my_str)

print(my_str.upper())
print(my_str.lower())