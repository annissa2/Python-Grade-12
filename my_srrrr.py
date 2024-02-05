my_str = " Hello, World! "

print(my_str)
#delete the blank space from the front and the back only in my string
print(my_str.strip())

#replace the old name to new one
print(my_str.replace('Hello','Bye'))

#split string
print(my_str.split("o"))

#concatenation is adding two string together
str_one = "Hello"
str_two = "World"

print (str_one + " " + str_two)
print("Bye Bye," + str_two)

#format string
print(f"hello, {str_two}")

print("Hello," + str_one + "add more string here")
print(f"{str_two} {str_two}")

#my name is name I'm here
#escape character
print('my name is name I\'m here')

