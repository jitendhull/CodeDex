# Create a pure function to calculate the area of a circle given its radius.

# Define a calculate_circle_area() function that takes the radius of the circle as input.
# Compute the area of the circle using the formula: area=π∗r 
# 2
#  .
# Return the result.

radius = 2

def calculate_circle_area(radius):
    return 3.14159 * radius ** 2


print(calculate_circle_area(radius))