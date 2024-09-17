def reduce_to_single_digit(num):
    while num >= 10:
        temp = 0
        while num > 0:
            temp += num % 10 
            num //= 10  
        num = temp  
    return num

num = int (input())
result = reduce_to_single_digit(num)
print(result)
