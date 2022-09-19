def add(a, b):
   return a + b

def subtract(a, b):
   return a - b

def multiply(a, b):
   return a * b

def divide(a, b):
   return a / b

print("Please select the operation.")
print("A. Add")
print("B. Subtract")
print("C. Multiply")
print("D. Divide")

choice = input("Please enter choice: ")

operand_a = int(input("Please enter the first number: "))
operand_b = int(input("Please enter the second number: "))

if choice == 'A':
   print(operand_a, " + ", operand_b, " = ", add(operand_a, operand_b))

elif choice == 'B':
   print(operand_a, " - ", operand_b, " = ", subtract(operand_a, operand_b))

elif choice == 'C':
   print(operand_a, " * ", operand_b, " = ", multiply(operand_a, operand_b))

elif choice == 'D':
   print(operand_a, " / ", operand_b, " = ", divide(operand_a, operand_b))

else:
   print("This is an invalid input")