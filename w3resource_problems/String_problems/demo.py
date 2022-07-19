
def beautifulDays(i, j, k):
    # Write your code here
    count_num = 0
    for n in range(i, j+1):
        str_n = str(n)
        rev_n = int(str_n[::-1])
        value = abs(not (n-rev_n) % k)
        print("Test: {}".format(value))
        count_num = count_num + value
        # if isinstance(value, int):
        #     count_num = count_num + 1
    return count_num

# def beautifulDays(i, j, k):
#     ans = 0
#     for n in range(i, j + 1):
#         ans = ans + abs(not (n - int(str(n)[::-1])) % k)
#     return ans


print(beautifulDays(20,23,6))

