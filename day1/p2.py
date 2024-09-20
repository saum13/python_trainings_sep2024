#Average Score
avg_score=int(input())
if (avg_score>=0 or avg_score<101):
    print("fail")
elif (avg_score>=50 ):
    print("SC")
elif(avg_score>=75 ):
    print("FC")
elif(avg_score>=91 ):
    print("Distinction")
else:
    print("Invalid Input")

