def add(R, S):
   return R + S

def subtract(R, S):
   return R - S

def multiply(R, S):
   return R * S

def divide(R, S):
   return R / S

print("Please select the operation.")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")

choice = input("Please enter choice: ")

num_1 = int(input("Please enter the first number: "))
num_2 = int(input("Please enter the second number: "))

if choice == 'a':
   print(num_1, " + ", num_2, " = ", add(num_1, num_2))

elif choice == 'b':
   print(num_1, " - ", num_2, " = ", subtract(num_1, num_2))

elif choice == 'c':
   print(num_1, " * ", num2, " = ", multiply(num1, num2))

elif choice == 'd':
   print(num_1, " / ", num_2, " = ", divide(num_1, num_2))

else:
   print("This is an invalid input")