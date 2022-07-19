# def repeat(fn):
#     fn()
#     fn()
#
#
# def hello_world():
#     print("Hello world!")
#
#
# repeat(hello_world)
#
# print("===================================================================")
#
#
# def repeat_decorator(fn):
#     def decorated_fn():
#         fn()
#         fn()
#     # returns a function
#     return decorated_fn
#
#
# def hello_world():
#     print ("Hello world!")
#
#
# hello_world_twice = repeat_decorator(hello_world)
#
# # call the function
# hello_world_twice()
print("===================================================================")

# function decorator that calls the function twice
def repeat_decorator(fn):
    def decorated_fn():
        fn()
        fn()
    # returns a function
    return decorated_fn

# using the decorator on hello_world function
@repeat_decorator
def hello_world():
    print ("Hello world!")

# call the function
hello_world()


# print("===================================================================")
#
# def repeat_decorator(num_repeats = 2):
#     # repeat_decorator should return a function that's a decorator
#     def inner_decorator(fn):
#         def decorated_fn():
#             for i in range(num_repeats):
#                 fn()
#         # return the new function
#         return decorated_fn
#     # return the decorator that actually takes the function in as the input
#     return inner_decorator
#
# # use the decorator with num_repeats argument set as 5 to repeat the function call 5 times
# @repeat_decorator(5)
# def hello_world():
#     print("Hello world!")
#
# # call the function
# hello_world()
