"""
Nuance program questions:
1. Count number of digits for the number of 3s to n number(for example if a number is 20 then the count is 2)
"""

num = 3528934373
num_str = str(num)
count_char = 0

for i in num_str:
    if i == "3":
        count_char += 1

print(count_char)