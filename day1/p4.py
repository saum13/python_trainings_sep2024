#print the Math table of a number upto the 20

num=int(input("Enter Number"))
for i in range(1,21):
    print("%d * %02d = %03d" % (num , i , num * i))
