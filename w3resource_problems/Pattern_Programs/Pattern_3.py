"""
****
***
**
*
"""

def star_prog(n):
    for i in range(1, n):
        for j in range(i, n):
            print("*", end="")
        print()

star_prog(6)