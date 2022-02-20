# r = 31
# M = 1234567891
import sys

sys.stdin = open('input_py.txt', "r")

n = input()
m = input()
total = 0
r = 1
for i in m:
  num = ord(i) - 96
  total += num * r
  r *=31

print(total % 1234567891)