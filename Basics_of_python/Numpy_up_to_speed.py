# This file will get you up to speed with some of the basic Numpy commands

# Program to create a numpy array and perform basic operations on them

# Import the numpy library
import numpy as np

# Create a numpy array
arr1 = np.array([1, 2, 3, 4, 5])
print("The array is: ", arr1)

# Accessing elements of a numpy array
print("The first element of the array is: ", arr1[0])
print("The second element of the array is: ", arr1[1])
print("The third element of the array is: ", arr1[2])
print("The fourth element of the array is: ", arr1[3])
print("The fifth element of the array is: ", arr1[4])

# Accessing using slicing
print("The first 3 elements of the array are: ", arr1[0:3])
print("The last 3 elements of the array are: ", arr1[2:5])

# Updating elements of a numpy array
arr1[0] = 10
print("The array after updating the first element is: ", arr1)

# Deleting elements of a numpy array
arr1 = np.delete(arr1, 0)
print("The array after deleting the first element is: ", arr1)

# Length of a numpy array
print("The length of the array is: ", len(arr1))

# Concatenation of numpy arrays
arr2 = np.array([6, 7, 8, 9, 10])
print("The second array is: ", arr2)
arr3 = np.concatenate((arr1, arr2))
print("The concatenated array is: ", arr3)

# Repetition of numpy arrays
arr4 = arr1 * 3
print("The repeated array is: ", arr4)

# Membership of a numpy array
print("Is 3 a member of the array? ", 3 in arr1)
print("Is 11 a member of the array? ", 11 in arr1)

# Iterating through a numpy array
print("The elements of the array are: ")
for i in arr1:
    print(i)


# Maximum and minimum of a numpy array
print("The maximum element of the array is: ", np.max(arr1))
print("The minimum element of the array is: ", np.min(arr1))

# Sorting a numpy array
arr5 = np.array([5, 4, 3, 2, 1])
print("The unsorted array is: ", arr5)
arr5.sort()
print("The sorted array is: ", arr5)

# Appending an element to a numpy array
arr5 = np.append(arr5, 6)
print("The array after appending 6 is: ", arr5)

# Reshaping a numpy array
arr6 = np.array([[1, 2, 3], [4, 5, 6]])
print("The array is: ", arr6)
print("The shape of the array is: ", arr6.shape)
arr6 = arr6.reshape(3, 2)
print("The reshaped array is: ", arr6)
print("The shape of the array is: ", arr6.shape)

# Transposing a numpy array
arr7 = np.array([[1, 2, 3], [4, 5, 6]])
print("The array is: ", arr7)
print("The shape of the array is: ", arr7.shape)
arr7 = arr7.transpose()
print("The transposed array is: ", arr7)
print("The shape of the array is: ", arr7.shape)

# Stacking numpy arrays
arr8 = np.array([1, 2, 3])
arr9 = np.array([4, 5, 6])
print("The first array is: ", arr8)
print("The second array is: ", arr9)
arr10 = np.stack((arr8, arr9))
print("The stacked array is: ", arr10)

# Splitting numpy arrays
arr11 = np.array([1, 2, 3, 4, 5, 6])
print("The array is: ", arr11)
arr12 = np.split(arr11, 3)
print("The splitted array is: ", arr12)

# Searching in a numpy array
arr13 = np.array([1, 2, 3, 4, 5, 6])
print("The array is: ", arr13)
print("The index of 3 in the array is: ", np.where(arr13 == 3))

# Filtering a numpy array
arr14 = np.array([1, 2, 3, 4, 5, 6])
print("The array is: ", arr14)
print("The elements greater than 3 in the array are: ", arr14[arr14 > 3])

# Sorting a numpy array
arr15 = np.array([5, 4, 3, 2, 1])
print("The unsorted array is: ", arr15)
arr15.sort()
print("The sorted array is: ", arr15)

# Reversing a numpy array
arr16 = np.array([1, 2, 3, 4, 5, 6])
print("The array is: ", arr16)
print("The reversed array is: ", np.flip(arr16))

# Array concatenations using stack
arr17 = np.array([1, 2, 3])
arr18 = np.array([4, 5, 6])
print("The first array is: ", arr17)
print("The second array is: ", arr18)
arr19 = np.stack((arr17, arr18))
print("The stacked array is: ", arr19)

# Array concatenations using concatenate
arr20 = np.array([1, 2, 3])
arr21 = np.array([4, 5, 6])
print("The first array is: ", arr20)
print("The second array is: ", arr21)
arr22 = np.concatenate((arr20, arr21))
print("The concatenated array is: ", arr22)

# Reshaping using numpy arrays
arr23 = np.array([[1, 2, 3], [4, 5, 6]])
print("The array is: ", arr23)
print("The shape of the array is: ", arr23.shape)
arr24 = arr23.reshape(3, 2)
print("The reshaped array is: ", arr24)
print("The shape of the array is: ", arr24.shape)

# Transposing using numpy arrays
arr25 = np.array([[1, 2, 3], [4, 5, 6]])
print("The array is: ", arr25)
print("The shape of the array is: ", arr25.shape)
arr26 = arr25.transpose()
print("The transposed array is: ", arr26)
print("The shape of the array is: ", arr26.shape)

# Splitting using numpy arrays
arr27 = np.array([1, 2, 3, 4, 5, 6])
print("The array is: ", arr27)
arr28 = np.split(arr27, 3)
print("The splitted array is: ", arr28)

# Searching using numpy arrays
arr29 = np.array([1, 2, 3, 4, 5, 6])
print("The array is: ", arr29)
print("The index of 3 in the array is: ", np.where(arr29 == 3))

# Filtering using numpy arrays
arr30 = np.array([1, 2, 3, 4, 5, 6])
print("The array is: ", arr30)
print("The elements greater than 3 in the array are: ", arr30[arr30 > 3])




