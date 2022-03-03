from math import factorial
import sys

sys.stdin = open("input_py.txt", "r")

N = int(input())
num = str(factorial(N))

i = 1
cnt = 0
while True:
  if num[len(num)-i] == '0':
    cnt +=1
    i+=1
  else:
    break
print(cnt)
