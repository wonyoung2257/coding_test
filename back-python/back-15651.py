from itertools import product

import sys

sys.stdin = open('input_py.txt','r')

input = sys.stdin.readline

n, m = map(int, input().split())
temp = list(range(1,n+1))

result = list(product(list(range(1,n+1)), repeat = m))

for i in result:
  print(*i)