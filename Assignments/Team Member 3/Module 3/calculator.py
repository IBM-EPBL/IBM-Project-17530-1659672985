def add(A, B):
   return A + B

def subtract(A, B):
   return A - B

def multiply(A, B):
   return A * B

def divide(A, B):
   return A / B

print("Please select the operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Please enter choice: ")

number_1 = int(input("Please enter the first number: "))
number_2 = int(input("Please enter the second number: "))

if choice == '1':
   print(number_1, " + ", number_2, " = ", add(number_1, number_2))

elif choice == '2':
   print(number_1, " - ", number_2, " = ", subtract(number_1, number_2))

elif choice == '3':
   print(num1, " * ", num2, " = ", multiply(num1, num2))

elif choice == '4':
   print(number_1, " / ", number_2, " = ", divide(number_1, number_2))

else:
   print("This is an invalid input")