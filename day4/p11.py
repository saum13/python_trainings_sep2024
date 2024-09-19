class employee:
    def __init__(self,name,designation,salary) -> None:
        self.name=name
        self.designation=designation
        self.salary=salary
        


    def __str__(self) -> str:
        return f"{self.name},{self.designation},{self.salary}"

emp1=employee("hi","abc",["hi","a"])
print(emp1)