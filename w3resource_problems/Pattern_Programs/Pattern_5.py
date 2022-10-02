"""
****
 ***
  **
   *
"""

def star_prog(n):
    for i in range(n, 0, -1):
        for j in range(i, n-1):
            print(" ", end="")
        for k in range(0, i):
            print("*", end="")
        print()

star_prog(6)