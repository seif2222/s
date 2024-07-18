import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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
class_width = data_range / num_classes
print("Class width:", class_width)

# Create a DataFrame
df = pd.DataFrame(numbers, columns=["Values"])

# Plot histogram
fig_hist = px.histogram(df, x="Values", nbins=num_classes, title="Histogram of Numbers")
fig_hist.update_layout(xaxis_title="Values", yaxis_title="Frequency")
fig_hist.show()

# Plot polygon
fig_polygon = go.Figure()
fig_polygon.add_trace(go.Scatter(x=list(range(len(numbers))), y=numbers, mode='lines+markers', name='Data Polygon'))
fig_polygon.update_layout(title="Data Polygon", xaxis_title="Data Index", yaxis_title="Values")
fig_polygon.show()

# Plot trend line
x = np.arange(len(numbers))
y = numbers
coefficients = np.polyfit(x, y, 1)
polynomial = np.poly1d(coefficients)
trend_line = polynomial(x)

fig_trend = go.Figure()
fig_trend.add_trace(go.Scatter(x=x, y=y, mode='markers', name='Data Points'))
fig_trend.add_trace(go.Scatter(x=x, y=trend_line, mode='lines', name='Trend Line'))
fig_trend.update_layout(title="Trend Line", xaxis_title="Data Index", yaxis_title="Values")
fig_trend.show()

# Saif Mohamed Abozaid