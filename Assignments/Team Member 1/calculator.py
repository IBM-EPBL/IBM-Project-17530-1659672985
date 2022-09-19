def add(i, j):
   return i + j

def subtract(i, j):
   return i - j

def multiply(i, j):
   return i * j

def divide(i, j):
   return i / j

print("Please select the operation.")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")

choice = input("Please enter choice: ")

first_num = int(input("Please enter the first number: "))
second_num = int(input("Please enter the second number: "))

if choice == 'a':
   print(first_num, " + ", second_num, " = ", add(first_num, second_num))

elif choice == 'b':
   print(first_num, " - ", second_num, " = ", subtract(first_num, second_num))

elif choice == 'c':
   print(first_num, " * ", second_num, " = ", multiply(first_num, second_num))

elif choice == 'd':
   print(first_num, " / ", second_num, " = ", divide(first_num, second_num))

else:
   print("This is an invalid input")