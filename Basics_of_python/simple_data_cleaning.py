# Program to do simple data cleaning in Python:

# Import the pandas library
import pandas as pd

# Read the csv file
df = pd.read_csv("data.csv")

# Print the first 5 rows of the dataframe
print("The first 5 rows of the dataframe are: ")
print(df.head())

# Print the last 5 rows of the dataframe
print("The last 5 rows of the dataframe are: ")
print(df.tail())

# Print the shape of the dataframe
print("The shape of the dataframe is: ", df.shape)

# Drop the rows with missing values
df = df.dropna()

# Print the shape of the dataframe after dropping the rows with missing values
print("The shape of the dataframe after dropping the rows with missing values is: ", df.shape)


