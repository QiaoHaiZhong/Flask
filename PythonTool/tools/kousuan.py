# coding=utf-8
'''
打印20以内的口算题目

'''
import random

plus = ['+', '-']

 
for i in range(0, 1000):
    a = random.randint(50, 100)
    b = random.randint(50, 100)
    c = random.randint(50, 100)
    d = random.randint(50, 100)
    e = random.randint(50, 100)
    f = random.randint(50, 100)
    if a > b & e > f :
        print "%2d - %2d =       %2d + %2d =         %2d - %2d = " % (a, b, c, d, e, f)
    elif a < b & e > f :
        print "%2d - %2d =       %2d + %2d =         %2d - %2d = " % (b, a, c, d, e, f)
    elif c > d:
        print "%2d + %2d =       %2d - %2d =         %2d + %2d = " % (a, b, c, d, e, f)
    elif a > c & b > d:
        print "%2d - %2d =       %2d + %2d =         %2d - %2d = " % (a, c, e, f, b, d)
    elif f > d:
        print "%2d + %2d =       %2d - %2d =         %2d + %2d = " % (a, b, f, d, e, c)

