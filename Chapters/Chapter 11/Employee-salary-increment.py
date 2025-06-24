# Define the Employee class
class Employee:
    
    # Class attributes (shared by all objects unless overridden)
    salary = 234           # Base salary before increment
    increment = 20         # Increment percentage (initially 20%)

    # Property decorator: makes this method accessible like an attribute
    @property
    def salary_After_Increment(self):
        # This calculates the salary after applying the increment
        # Formula: salary + (salary × increment%)
        return self.salary + (self.salary * (self.increment / 100))

    # Setter for salary_After_Increment: lets you set the final salary
    @salary_After_Increment.setter
    def salary_After_Increment(self, salary):
        # When a new final salary is set, this reverses the formula
        # to calculate what the new increment % would be
        # Formula: increment = ((final salary / base salary) - 1) × 100
        self.increment = ((salary / self.salary) - 1) * 100

# Create an object of the Employee class
e = Employee()

# Print the salary after 20% increment
# Should output: 280.8 (234 + 20% of 234)
print(e.salary_After_Increment)

# Now we want to set the final salary directly
# It will auto-update the increment value
e.salary_After_Increment = 280.8

# Print the new increment calculated based on the new final salary
# Should output: 20.0 (since 280.8 is exactly 20% more than 234)
print(e.increment)
