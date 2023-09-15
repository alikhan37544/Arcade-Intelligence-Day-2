# Line Plot
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 7, 6]

# Create a line plot
plt.plot(x, y)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')

# Display the plot
plt.show()


# Scatter plot 
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 7, 6]

# Create a scatter plot
plt.scatter(x, y, label='Data Points', color='blue', marker='o')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')

# Add legend
plt.legend()

# Display the plot
plt.show()



# Bar chart
import matplotlib.pyplot as plt

# Data
categories = ['A', 'B', 'C', 'D']
values = [5, 12, 7, 9]

# Create a bar chart
plt.bar(categories, values, color='green')

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart')

# Display the plot
plt.show()






# Histogram
import matplotlib.pyplot as plt
import numpy as np

# Generate random data
data = np.random.randn(1000)

# Create a histogram
plt.hist(data, bins=20, color='purple', alpha=0.7)

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')

# Display the plot
plt.show()




# Pie chart 
import matplotlib.pyplot as plt

# Data
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]

# Create a pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

# Add title
plt.title('Pie Chart')

# Display the plot
plt.show()
