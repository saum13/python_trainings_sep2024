try:
    nithin = print('Nithin') # print() returns nothing
    print(nithin) #None
    print(len(nithin)) # causes exception
except TypeError as exp:
    print('Some Error Occured')
    print(exp)

#TypeError: object of type 'NoneType' has no len()