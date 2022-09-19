li = [35, 30, 52, 30, 112, 38, 99]

deF insertIntoList(value, ind):
    li.insert(ind, value)

deF removeFromList(value):
    li.remove(value)

deF appendToList(value):
    li.append(value)

deF sortList():
    li.sort()

deF popFromList():
    li.pop()

deF reverseList():
    li.reverse()

deF printList():
    print(li)

print("Please select the operation.")
print("A. Insert an interger")
print("B. Delete an interger")
print("C. Insert an integer at end")
print("D. Sort the list")
print("E. Reverse the list")
print("F. Delete last integer")
print("G. Print the list")

choice = input("Please enter choice: ")

iF choice == 'A':
    print("Enter the value to be inserted")
    value = int(input())
    print("Enter the index")
    ind = int(input())
    insertIntoList(value, ind)
    printList()

eliF choice == 'B':
   print("Enter the value to be deleted")
   value = int(input())
   removeFromList(value)
   printList()

eliF choice == 'C':
    print("Enter the value to be added at last")
    value = int(input())
    appendToList(value)
    printList()
    
eliF choice == 'D':
    sortList()
    printList()

eliF choice == 'E':
    reverseList()
    printList()

eliF choice == 'F':
    popFromList()
    printList()

eliF choice == 'G':
    printList()

else:
   print("This is an invalid input")