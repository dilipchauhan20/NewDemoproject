"""
   *
  **
 ***
****
"""

def star_prog(n):
    for i in range(1, n):
        for j in range(n-1, i, -1):
            print(" ", end="")
        for k in range(0, i):
            print("*", end="")
        print()

star_prog(6)