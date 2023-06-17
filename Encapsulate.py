class MyClass:
    def __init__(self):
        self._protected_attr = 42  # Protected attribute

    def _private_method(self):
        return "This is a private method."

    def public_method(self):
        # Accessing the protected attribute
        print(f"The protected attribute value is: {self._protected_attr}")
        # Calling the private method
        private_result = self._private_method()
        print(private_result)

# Creating an object of the class
obj = MyClass()

# Accessing the protected attribute (allowed)
print(f"Protected attribute value: {obj._protected_attr}")

# Calling the public method (allowed)
obj.public_method()

# Accessing the private method or attribute (not recommended, but still possible)
private_result = obj._private_method()
print(private_result)
