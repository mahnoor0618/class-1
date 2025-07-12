#Exercise 1

#Write a program in that prints the same notes from the previous lesson using what you have learnt about the Python print function.

print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

#Exercise 2

#Fix the code below 👇
"""
print("Day 1 - String Manipulation")
print("String Concatenation is done with the + sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")
"""
print("Day 1 - String Manipulation")
print("String Concatenation is done with the + sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

#Exercise 3

#Write a program that prints the number of characters in a user's name. You might need to Google for a function that calculates the length of a string.

name=str(input("Enter your name: "))
n=len(name)
print(f"The number of characters in a user's name are: \n{n}")

#Exercise 4

#Write a program that switches the values stored in the variables a and b.

a=int(input("Enter any number: ")) #20
b=int(input("Enter any number: ")) #30
print(f"a before swapping is {a}")
print(f"b before swapping is {b}")
a=a+b #50
b=a-b #20
a=a-b #30
print(f"a after swapping is {a}")
print(f"b after swapping is {b}")

#Capstone Project: Personalized Greeting and Name Length Checker
"""
Requirements:
The program should ask the user to enter their name.
Store the user's name in a variable.
Print a personalized greeting using the print function, such as "Hello, [name]!".
Calculate the number of characters in the user's name using the len() function.
Print a message displaying the number of characters in their name.
"""

name=str(input("Enter your name: "))
n=len(name)
print(f"Assalam o Alaikum {name}")
print(f"The number of characters in your name are {n}")