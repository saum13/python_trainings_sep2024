class A(object):
    pass

class B(A):
    pass  

class C(B):
    pass

obj1 = A()
obj2 = B()
obj3 = C()
print(isinstance(obj1, B))
print(isinstance(obj2, B))
print(isinstance(obj3, B))
