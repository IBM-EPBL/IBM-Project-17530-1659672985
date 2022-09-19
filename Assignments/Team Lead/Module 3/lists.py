list = [35, 30, 52, 30, 112, 38, 99]

def inset_into_list(value, ind):
    list.insert(ind, value)

def remove_from_list(value):
    list.remove(value)

def append_to_list(value):
    list.append(value)

def sort_list():
    list.sort()

def pop_from_list():
    list.pop()

def reverse_list():
    list.reverse()

def print_list():
    print(list)

print("Please select the operation.")
print("a. Insert an interger")
print("b. Delete an interger")
print("c. Insert an integer at end")
print("d. Sort the list")
print("e. Reverse the list")
print("f. Delete last integer")
print("g. Print the list")

choice = input("Please enter choice: ")

if choice == 'a':
    print("Enter the value to be inserted")
    value = int(input())
    print("Enter the index")
    ind = int(input())
    inset_into_list(value, ind)
    print_list()

elif choice == 'b':
   print("Enter the value to be deleted")
   value = int(input())
   remove_from_list(value)
   print_list()

elif choice == 'c':
    print("Enter the value to be added at last")
    value = int(input())
    append_to_list(value)
    print_list()
    
elif choice == 'd':
    sort_list()
    print_list()

elif choice == 'e':
    reverse_list()
    print_list()

elif choice == 'f':
    pop_from_list()
    print_list()

elif choice == 'g':
    print_list()

else:
   print("This is an invalid input")