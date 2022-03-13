import sys

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

x = []
y = []
for _ in range(3):
  a, b = map(int, input().split(' '))
  x.append(a)
  y.append(b)
temp = [0,0]
for i in range(3):
  if x.count(x[i]) == 1:
    temp[0] = x[i]
  if y.count(y[i]) == 1:
    temp[1] = y[i]

print(temp[0], temp[1])

import math

r= 1
print(r*r*math.pi)
print(r*r*2)