import check_nums

num1 = 15
num5 = 37
from check_nums import check_if_even
from check_nums import check_if_prime
from check_nums import check_if_odd

if check_if_even(num1):
    print(f'{num1} is Even')
else:
    print(f'{num1} is not Even')

if check_if_prime(num5):
    print(f'{num5} is Prime')
else:
    print(f'{num5} is not Prime')