list1 = [13, 7, 6, 45, 21, 9, 2, 100]






# my_funcdef my_func():
#     """
#     Write a program to count characters in a string
#     """


# print(my_func.__doc__)
# str1 = "laksjdkjasfdshfhds"
# dict1 = {}
#
# for i in str1:
#     if i not in dict1:
#         dict1[i] = 1
#     else:
#         dict1[i] += 1
#
# for key, value in dict1.items():
#     print(key, "-->", value)


# if True:
#     break
#     print("abcd")


# a = True
# b = False
# c = False
#
# if a or b and c:
#     print("Hello")
# else:
#     print("Test")





# a = 15
# b = 4
#
# print(a//b)


# #Example of shallow copy
# list_example = [1,2,3,4,5]
# another_list = list_example
# another_list[0] = 100
# print(list_example)


# #Example of Deep copy
# list_example = [1,2,3,4,5]
# #Iniating Deep copy with .copy attribute
# another_list = list_example.copy()
# another_list[0] = 100
# print(list_example)

# class sample:
#     pass
# test=sample()
# test.name="test1"
# print(test.name)


# #Example membership operators
# print('me' in 'membership')
# print('mes' not in 'membership')


# #Example Identity operators
# print(1 is '1')
# print(2 is not '2')


#Zip function example
# print(list(zip([1,2,3], ['apple', 'grape', 'orange'], ['x', 2, True])))
# for num, fruit, thing in zip([1,2,3], ['apple', 'grape', 'orange'], ['x', 2, True]):
#     print(num)
#     print(fruit)
#     print(thing)
# test = zip([1,2,3], ['apple', 'grape', 'orange'], ['x', 2, True])


# counter = 0
#
# def increment():
#    counter += 1
#
# increment()


# def my_function():
#     '''Demonstrates triple double quotes
#     docstrings and does nothing really.'''
#
#     return None
#
#
# print("Using __doc__:")
# print(my_function.__doc__)
#
# print("Using help:")
# help(my_function)












# def beautifulDays(i, j, k):
#     # Write your code here
#     count_num = 0
#     for n in range(i, j+1):
#         str_n = str(n)
#         rev_n = int(str_n[::-1])
#         value = abs(not (n-rev_n) % k)
#         print("Test: {}".format(value))
#         count_num = count_num + value
#         # if isinstance(value, int):
#         #     count_num = count_num + 1
#     return count_num
#
# # def beautifulDays(i, j, k):
# #     ans = 0
# #     for n in range(i, j + 1):
# #         ans = ans + abs(not (n - int(str(n)[::-1])) % k)
# #     return ans
#

# print(beautifulDays(20,23,6))

