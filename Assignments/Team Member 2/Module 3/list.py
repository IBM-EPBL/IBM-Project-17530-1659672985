r = [35, 30, 52, 30, 112, 38, 99]

def insertIntoList(val, ind):
    r.insert(ind, val)

def removeFromList(val):
    r.remove(val);

def appendToList(val):
    r.append(val)

def sortList():
    r.sort();

def popFromList():
    r.pop();

def reverseList():
    r.reverse();

def printList():
    print(r);

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
    print("Enter the val to be inserted")
    val = int(input())
    print("Enter the index")
    ind = int(input())
    insertIntoList(val, ind);
    printList();

elif choice == 'b':
   print("Enter the val to be deleted");
   val = int(input())
   removeFromList(val)
   printList()

elif choice == 'c':
    print("Enter the val to be added at last")
    val = int(input())
    appendToList(val);
    printList();
    
elif choice == 'd':
    sortList();
    printList();

elif choice == 'e':
    reverseList();
    printList();

elif choice == 'f':
    popFromList();
    printList();

elif choice == 'g':
    printList();

else:
   print("This is an invalid input")