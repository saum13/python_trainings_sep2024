class MyClass:
    count_of_objects = 0
    
    def __init__(self) -> None:
        self.var1 = 20
        self.var2 = 30
        MyClass.count_of_objects += 1

    @classmethod
    def class_method(cls):
        return cls.count_of_objects
    
    @staticmethod
    def static_method():
        return f"This is a static method {MyClass.count_of_objects}."

    def __str__(self):
        return f'var1 = {self.var1}, var2 = {self.var2}, Count= {MyClass.count_of_objects}'

print(MyClass.class_method())  # Output: 0
print(MyClass.static_method())  # Output: This is a static method.
obj1 = MyClass()
print(obj1)
obj2 = MyClass()
print(obj2)
print(dir(MyClass))