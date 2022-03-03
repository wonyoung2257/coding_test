from collections import Counter
import sys

sys.stdin = open("./input_py.txt", "r")
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  N = int(input())
  dic = []
  for i in range(N):
    item, k = input().strip().split(' ')
    dic.append(k)

  num = 1
  result = Counter(dic)
  for key in result:
    num *= result[key] +1
  print(num-1)