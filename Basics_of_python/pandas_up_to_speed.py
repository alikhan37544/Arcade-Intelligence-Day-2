# Pandas program to show basic operations of series

# Import the pandas library
import pandas as pd

# Create a series
series1 = pd.Series([1, 2, 3, 4, 5])
print("The series is: ", series1)

# Accessing the elements of a series
print("The first element of the series is: ", series1[0])
print("The second element of the series is: ", series1[1])
print("The third element of the series is: ", series1[2])
print("The fourth element of the series is: ", series1[3])
print("The fifth element of the series is: ", series1[4])

# Accessing using slicing
print("The first 3 elements of the series are: ", series1[0:3])
print("The last 3 elements of the series are: ", series1[2:5])

# Updating elements of a series
series1[0] = 10
print("The series after updating the first element is: ", series1)

# Deleting elements of a series
series1 = series1.drop(0)
print("The series after deleting the first element is: ", series1)

# Length of a series
print("The length of the series is: ", len(series1))

# Concatenation of series
series2 = pd.Series([6, 7, 8, 9, 10])
print("The second series is: ", series2)
series3 = pd.concat([series1, series2])
print("The concatenated series is: ", series3)

# Repetition of series
series4 = series1 * 3
print("The repeated series is: ", series4)

# Membership of a series
print("Is 3 a member of the series? ", 3 in series1)
print("Is 11 a member of the series? ", 11 in series1)

# Iterating through a series
print("The elements of the series are: ")
for i in series1:
    print(i)

# Maximum and minimum of a series
print("The maximum element of the series is: ", series1.max())
print("The minimum element of the series is: ", series1.min())

# Sorting a series
series5 = pd.Series([5, 4, 3, 2, 1])
print("The unsorted series is: ", series5)
series5.sort_values()
print("The sorted series is: ", series5)

# Appending an element to a series
series5 = series5.append(pd.Series([6]))
print("The series after appending 6 is: ", series5)

"""
This should be enough to get us started on the basics of Series

Now, let's move on to DataFrames
"""



# Pandas program to show basic operations of dataframe

# Import the pandas library
import pandas as pd

# Create a dataframe
dataframe1 = pd.DataFrame([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("The dataframe is: ", dataframe1)

# Accessing the elements of a dataframe and displaying it
print("The element at position (0, 0) of the dataframe is: ", dataframe1.iloc[0][0])
print("The element at position (0, 1) of the dataframe is: ", dataframe1.iloc[0][1])
print("The element at position (0, 2) of the dataframe is: ", dataframe1.iloc[0][2])
print("The element at position (0, 3) of the dataframe is: ", dataframe1.iloc[0][3])
print("The element at position (0, 4) of the dataframe is: ", dataframe1.iloc[0][4])
print("The element at position (1, 0) of the dataframe is: ", dataframe1.iloc[1][0])
print("The element at position (1, 1) of the dataframe is: ", dataframe1.iloc[1][1])
print("The element at position (1, 2) of the dataframe is: ", dataframe1.iloc[1][2])
print("The element at position (1, 3) of the dataframe is: ", dataframe1.iloc[1][3])
print("The element at position (1, 4) of the dataframe is: ", dataframe1.iloc[1][4])

# Accessing using slicing
print("The first 3 elements of the dataframe are: ", dataframe1.iloc[0][0:3])
print("The last 3 elements of the dataframe are: ", dataframe1.iloc[0][2:5])

# Updating elements of a dataframe
dataframe1.iloc[0][0] = 10
print("The dataframe after updating the first element is: ", dataframe1)

# Deleting elements of a dataframe
dataframe1 = dataframe1.drop(0)
print("The dataframe after deleting the first element is: ", dataframe1)

# Length of a dataframe
print("The length of the dataframe is: ", len(dataframe1))

# Concatenation of dataframes
dataframe2 = pd.DataFrame([[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])
print("The second dataframe is: ", dataframe2)
dataframe3 = pd.concat([dataframe1, dataframe2])
print("The concatenated dataframe is: ", dataframe3)

# Repetition of dataframes
dataframe4 = dataframe1 * 3
print("The repeated dataframe is: ", dataframe4)

# Membership of a dataframe
print("Is 3 a member of the dataframe? ", 3 in dataframe1)
print("Is 11 a member of the dataframe? ", 11 in dataframe1)

# Iterating through a dataframe
print("The elements of the dataframe are: ")
for i in dataframe1:
    print(i)

# Maximum and minimum of a dataframe
print("The maximum element of the dataframe is: ", dataframe1.max())
print("The minimum element of the dataframe is: ", dataframe1.min())

# Sorting a dataframe
dataframe5 = pd.DataFrame([[5, 4, 3, 2, 1], [10, 9, 8, 7, 6]])
print("The unsorted dataframe is: ", dataframe5)
dataframe5.sort_values()
print("The sorted dataframe is: ", dataframe5)

# Appending an element to a dataframe
dataframe5 = dataframe5.append(pd.DataFrame([[11, 12, 13, 14, 15]]))
print("The dataframe after appending 11, 12, 13, 14, 15 is: ", dataframe5)

"""
This should be enough to get us started on the basics of DataFrames

"""
