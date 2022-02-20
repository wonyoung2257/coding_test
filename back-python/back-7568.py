import sys

sys.stdin = open("../input_py.txt", "r")

testCase = int(sys.stdin.readline())

arr = []
for _ in range(testCase):
  w, h  = map(int, sys.stdin.readline().split())
  arr.append((w, h))

for i in arr:
  rank =1
  for j in arr:
    if i[0] < j[0] and i[1] < j[1]:
      rank+=1
  print(rank, end=' ')

