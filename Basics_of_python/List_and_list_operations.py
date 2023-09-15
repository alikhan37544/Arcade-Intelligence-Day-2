# Python program to demonstrate some basic list operations:

# Create a list:
list1 = [1, 2, 3, 4, 5]
print("The list is: ", list1)

# Accessing elements of a list:
print("The first element of the list is: ", list1[0])
print("The second element of the list is: ", list1[1])
print("The third element of the list is: ", list1[2])
print("The fourth element of the list is: ", list1[3])
print("The fifth element of the list is: ", list1[4])

# Acessing using slicing:
print("The first 3 elements of the list are: ", list1[0:3])
print("The last 3 elements of the list are: ", list1[2:5])

# Updating elements of a list:
list1[0] = 10
print("The list after updating the first element is: ", list1)

# Deleting elements of a list:
del list1[0]
print("The list after deleting the first element is: ", list1)

# Length of a list:
print("The length of the list is: ", len(list1))

# Concatenation of lists:
list2 = [6, 7, 8, 9, 10]
print("The second list is: ", list2)
list3 = list1 + list2
print("The concatenated list is: ", list3)

# Repetition of lists:
list4 = list1 * 3
print("The repeated list is: ", list4)

# Membership of a list:
print("Is 3 a member of the list? ", 3 in list1)
print("Is 11 a member of the list? ", 11 in list1)

# Iterating through a list:
print("The elements of the list are: ")
for i in list1:
    print(i)

# Maximum and minimum of a list:
print("The maximum element of the list is: ", max(list1))
print("The minimum element of the list is: ", min(list1))

# Sorting a list:
list5 = [5, 4, 3, 2, 1]
print("The unsorted list is: ", list5)
list5.sort()
print("The sorted list is: ", list5)

# Appending an element to a list:
list5.append(6)
print("The list after appending 6 is: ", list5)

# Inserting an element at a particular index:
list5.insert(0, 0)
print("The list after inserting 0 at index 0 is: ", list5)

# Removing an element from a list:
list5.remove(0)
print("The list after removing 0 is: ", list5)

# Poping an element from a list:
list5.pop()
print("The list after poping an element is: ", list5)

# Clearing a list:
list5.clear()
print("The list after clearing is: ", list5)

# Counting the number of occurences of an element in a list:
list6 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print("The list is: ", list6)
print("The number of occurences of 1 in the list is: ", list6.count(1))

# Extending a list:
list6.extend([6, 7, 8, 9, 10])
print("The list after extending is: ", list6)

# Index of an element in a list:
print("The index of 1 in the list is: ", list6.index(1))

# Reversing a list:
list6.reverse()
print("The reversed list is: ", list6)

# Copying a list:
list7 = list6.copy()
print("The copied list is: ", list7)

