#!/usr/bin/env python3

# def f(*arg):
#     for a in arg:
#         li = a.split(":")
        
#         id = int(li[0])
#         income = int(li[1])
#         print(id,income)

# f("10:3000","20:5000")




import sys

sys.argv.pop(0)
print(sys.argv)