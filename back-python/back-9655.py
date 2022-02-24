import sys

sys.stdin = open("./input_py.txt", "r")

T = int(sys.stdin.readline())

if T% 2 == 0:
  print('CY')
else:
  print('SK')