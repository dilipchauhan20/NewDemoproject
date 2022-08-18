"""
Move all zeroes to the end of the array- Given an array of integers, Move all zero’s to the
end of the array. Push all the zero’s of a given array to the end of the array.
Example 1:INPUT: myArray={2,5,0,4,2,7,0,0,1,9,4}
OUTPUT: myArray={2,5,4,2,7,1,9,4,0,0,0}
"""

list1 = [2,5,0,4,2,7,0,0,1,9,4]

for i in list1:
    if i == 0:
        list1.remove(i)
        list1.append(i)


print(list1)
