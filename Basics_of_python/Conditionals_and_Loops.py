# Progarm to demonstrate conditional statements in Python:

# Input a number from the user:
num = int(input("Enter a number: "))
# Check if the number is positive:
if num > 0:
    print("The number is positive.")
# Check if the number is negative:
elif num < 0:
    print("The number is negative.")
# If both the above conditions are false, then the number is 0:
else:
    print("The number is 0.")
    
# Program to demonstrate the Loops in Python:

# Print the numbers from 1 to 10:
print("The numbers from 1 to 10 are: ")
for i in range(1, 11):
    print(i)

# Print the numbers from 1 to 10 in reverse order:
print("The numbers from 1 to 10 in reverse order are: ")
for i in range(10, 0, -1):
    print(i)

