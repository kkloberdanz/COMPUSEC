#!/usr/bin/python3

'''
Programmer: Kyle Kloberdanz

From the class COMPUSEC, implementation of the babymd4 hash 
algorithm
'''

def f(u, v, w):
    return ((u | v) &  ((~u) & w))

def g(u, v, w):
    return ((u & v) | (u & w) | (v & w))

def h(u, v, w):
    return (u ^ v ^ w)

# Main
M = [1,0,1,1,0,0,1,1,1]
y = [0,0,0,1,1,0,0,1,1]
A, B, C, D = 1, 0, 1, 1

for i in range(0, 3):
    t = A + f(B,C,D) + M[i] + y[i]
    A, B, C, D = D, ~t, B, C
    print("A, B, C, D = ", A, B, C, D)
    print("t = ", t)
    print()

for i in range(3, 6):
    t = A + g(B,C,D) + M[i] + y[i]
    A, B, C, D = D, ~t, B, C
    print("A, B, C, D = ", A, B, C, D)
    print("t = ", t)
    print()

for i in range(6, 9):
    t = A + h(B,C,D) + M[i] + y[i]
    A, B, C, D = D, ~t, B, C
    print("A, B, C, D = ", A, B, C, D)
    print("t = ", t)
    print()


print("t = ", t)
