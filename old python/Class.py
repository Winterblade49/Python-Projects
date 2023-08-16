class ParentClass:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def parent_method(self):
        print("This is a method from the parent class.")


class ChildClass1(ParentClass):
    def __init__(self, attribute1, attribute2, child_attribute1):
        # Call the parent class constructor
        super().__init__(attribute1, attribute2)
        self.child_attribute1 = child_attribute1

    def child_method1(self):
        print("This is a method from ChildClass1.")


class ChildClass2(ParentClass):
    def __init__(self, attribute1, attribute2, child_attribute2):
        # Call the parent class constructor
        super().__init__(attribute1, attribute2)
        self.child_attribute2 = child_attribute2

    def child_method2(self):
        print("This is a method from ChildClass2.")


# Create objects and test the classes
parent_obj = ParentClass("ParentAttribute1", "ParentAttribute2")
child1_obj = ChildClass1("ParentAttribute1", "ParentAttribute2", "ChildAttribute1")
child2_obj = ChildClass2("ParentAttribute1", "ParentAttribute2", "ChildAttribute2")

print(parent_obj.attribute1, parent_obj.attribute2)  # Output: ParentAttribute1 ParentAttribute2
parent_obj.parent_method()  # Output: This is a method from the parent class.

print(child1_obj.attribute1, child1_obj.attribute2, child1_obj.child_attribute1)  # Output: ParentAttribute1 ParentAttribute2 ChildAttribute1
child1_obj.parent_method()  # Output: This is a method from the parent class.
child1_obj.child_method1()  # Output: This is a method from ChildClass1.

print(child2_obj.attribute1, child2_obj.attribute2, child2_obj.child_attribute2)  # Output: ParentAttribute1 ParentAttribute2 ChildAttribute2
child2_obj.parent_method()  # Output: This is a method from the parent class.
child2_obj.child_method2()  # Output: This is a method from ChildClass2.