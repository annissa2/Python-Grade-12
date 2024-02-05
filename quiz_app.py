#file name quiz_app.py
# name = input("what is your name? ")
# print ("Hello", name)

#file name
total_point = 0
question = input ("2 + 2? ") 

if question == "4":
    total_point = total_point + 1
    print('Correct')
else:
    print('Incorrect')

question_two = input ("3 + 7? ") 

if question_two == "10":
    total_point = total_point + 1
    print('Correct')
else:
    print('Incorrect')

question_three = input ("5 - 4? ") 

if question_three == "1":
    total_point = total_point + 1
    print('Correct')
else:
    print('Incorrect')

question_four = input ("8 + 5? ") 

if question_four == "13":
    total_point = total_point + 1
    print('Correct')
else:
    print('Incorrect')

question_five = input ("9 - 3? ") 

if question_five == "6":
    total_point = total_point + 1
    print('Correct')
else:
    print('Incorrect')

print(f"Your total point is: {int(total_point/5*100)}%")


