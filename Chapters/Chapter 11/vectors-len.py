# Define the Vector class
class Vector:
    # Constructor: initializes a vector with a list of components
    def __init__(self, components):
        self.components = components  # Store components as a list

    # Method to add two vectors
    def __add__(self, second):
        # Perform element-wise addition using a list comprehension
        return Vector([self.components[i] + second.components[i] for i in range(len(self.components))])

    # Method to compute the dot product of two vectors
    def __mul__(self, second):
        # Multiply corresponding elements and return the sum
        return sum([self.components[i] * second.components[i] for i in range(len(self.components))])

    # Method to get the dimension (length) of the vector
    def __len__(self):
        return len(self.components)  # Simply return length of the list

    # Method to return a string representation of the vector
    def __str__(self):
        return f"Resultant vector is {self.components}"


# Create two vector instances
v1 = Vector([1, 3, 4])
v2 = Vector([2, 7, 6])

# Print dot product of v1 and v2
print(v1 * v2)  # Output: 1*2 + 3*7 + 4*6 = 2 + 21 + 24 = 47

# Print addition of v1 and v2
print(v1 + v2)  # Output: [1+2, 3+7, 4+6] = [3, 10, 10]

# Print length (dimension) of v2
print(len(v2))  # Output: 3
