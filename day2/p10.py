#dict frequency
a = [1, 2, 3, 1, 3, 14, 41, 3, 3, 1, 2, 31, 3]


frequency_dict = {}

for i in a:
    if i in frequency_dict:
        frequency_dict[i] += 1
    else:
        frequency_dict[i] = 1

print(f"frequency of elements of list \n{frequency_dict}")

