# -*- coding: utf-8 -*-

def sqrt_sum(L):
    return sum([x*x for x in L])
print sqrt_sum([1,2,3,4,5])

# 阶乘
def fact(n):
    if n == 1:
        return 1
    return fact(n - 1) * n
print fact(5)
print fact(100)
#print fact(1000) # RuntimeError: maximum recursion depth exceeded


# 汉诺塔

def move(n, a, b, c):44

    if n == 1:
        print a, '-->', c
        return
    move(n-1, a, c, b)
    move(1, a, b, c)
    move(n-1, b, a, c)
move(3,'A', 'B', 'C')
