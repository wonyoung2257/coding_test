import sys

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

string = input()

UCPC = 'UCPC'
idx = 0
for i in string:
  if idx > 3:
    break
  if UCPC[idx] == i and idx<4:
    idx+=1

print('I love UCPC' if idx==4 else 'I hate UCPC')