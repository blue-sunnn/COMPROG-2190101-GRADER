# -*- coding: utf-8 -*-
"""COMPROG02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yqyqQMTdA3sxmyCECnV5NzEo9ks8hXW1
"""

n = input()

a = (13 * int(n[0])) + (12 * int(n[1])) + (11 * int(n[2])) +  (10 * int(n[3]))
b = (9  * int(n[4])) + (8  * int(n[5])) + (7  * int(n[6])) +  (6  * int(n[7]))
c = (5  * int(n[8])) + (4  * int(n[9])) + (3  * int(n[10])) + (2  * int(n[11]))

d = (11 - (a + b + c) % 11) % 10

print(n[0], n[1:5], n[5:10], n[10:], str(d))

num_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

n = int(input())

print(n, '-->', num_list[n])

month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

n = input().split('/')

n[1] = int(n[1]) - 1

print(month_list[n[1]] + ' ' + n[0] + ',' + ' ' + n[2])

m = input()
n = int(input())
o = n - len(m)

print(('0' * o) + m)

n = input().split()

sum = int(n[0]) + int(n[1]) + int(n[2]) + int(n[3]) + int(n[4]) + int(n[5]) + int(n[6])

print(sum)

u = input()
v = input()

u = list(map(float, u[1:-1].split(', ')))
v = list(map(float, v[1:-1].split(', ')))

sum = [u[0] + v[0], u[1] + v[1], u[2] + v[2]]

print(str(u) + ' + ' + str(v) + ' = ' + str(sum))

alp_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
n = input()

a = n[3::7]
b = n[7::5]
c = str(int(a) + int(b) + 10000)
d = c[-4:-1]
e = str(int(d[0]) + int(d[1]) + int(d[2]))
e = int(e[-1:]) + 1
f = alp_list[e - 1]

print(d + f)

#https://cdn.discordapp.com/attachments/1141947228852867092/1141947261648130098/how_to_solve.png
from math import gcd

x = input().split(',')

n = int(x[0] + x[1] + x[2]) - int(x[0] + x[1])
d = (10 ** (len(x[1]) + len(x[2])) - (10 ** len(x[1])))

ans_n = n // gcd(n, d)
ans_d = d // gcd(n, d)

print(str(ans_n) + ' / ' + str(ans_d))