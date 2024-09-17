#pdb python debug
import math
import pdb

pdb.set_trace()

num=int(input("Enter Number\n"))
sqrt=math.sqrt(num)
floor_value=math.floor(sqrt)
if(floor_value*floor_value==num):
    print(f"{num} is a perfect square")
else:
    print(f"{num} is not a perfect square")
