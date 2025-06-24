# Define a class to represent complex numbers
class Complex:
    
    # Constructor: initializes real and imaginary parts
    def __init__(self, r, i):
        self.r = r  # Real part
        self.i = i  # Imaginary part

    # Define how to add two Complex objects using the + operator
    def __add__(self, second):
        # Add real parts and imaginary parts separately
        return Complex(self.r + second.r, self.i + second.i)

    # Define how to multiply two Complex objects using the * operator
    def __mul__(self, second):
        # Apply complex number multiplication formula:
        # (a + bi)(c + di) = (ac - bd) + (ad + bc)i
        real_part = (self.r * second.r) - (self.i * second.i)
        imaginary_part = (self.r * second.i) + (self.i * second.r)
        
        # Return a new Complex object with the result
        return Complex(real_part, imaginary_part)

    # String representation of a Complex number (when printed)
    def __str__(self):
        return f"{self.r} + {self.i}i"

# Create two complex number objects: c1 = 1 + 2i, c2 = 3 + 6i
c1 = Complex(1, 2)
c2 = Complex(3, 6)

# Print the result of c1 + c2 (uses __add__)
print(c1 + c2)  # Output: 4 + 8i

# Print the result of c1 * c2 (uses __mul__)
print(c1 * c2)  # Output: -9 + 12i
