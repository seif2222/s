import numpy as np 
import matplotlib.pyplot as plt 

# Set matplotlib to display plots in a separate window
plt.switch_backend('TkAgg')

# Input numbers from the user
input_str = input("Enter numbers separated by spaces: ")
numbers = np.array([int(x) for x in input_str.split()])

# Calculate minimum and maximum values using NumPy
minimum = np.min(numbers)
maximum = np.max(numbers)

print("Minimum value:", minimum)
print("Maximum value:", maximum)

# Calculate range
data_range = maximum - minimum
print("Range:", data_range)

# Input number of classes from the user
num_classes = int(input("Enter the number of classes: "))

# Calculate class width
class_width = data_range / (num_classes )
print("Class width:", class_width)

# Plot histogram
plt.hist(numbers, bins=num_classes, alpha=0.7, rwidth=0.85)
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram of Numbers')
plt.grid(True)
plt.show()

# Plot polygon
plt.plot(numbers, 'b-', marker='o')
plt.xlabel('Data Index')
plt.ylabel('Values')
plt.title('Data Polygon')
plt.grid(True)
plt.show()

# Plot trend line
x = np.arange(len(numbers))
y = numbers
coefficients = np.polyfit(x, y, 1)
polynomial = np.poly1d(coefficients)
trend_line = polynomial(x)
plt.plot(x, y, 'bo', x, trend_line, 'r-')
plt.xlabel('Data Index')
plt.ylabel('Values')
plt.title('Trend Line')
plt.grid(True)
plt.show()