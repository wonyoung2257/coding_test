from itertools import combinations
import sys
sys.stdin = open('input_py.txt','r')

n = int(input())
array = [i for i in range(n)]
matrix = []
for _ in range(n):
  matrix.append((list(map(int, input().split()))))

result = 1e9
for r1 in combinations(array, n//2):
  start = 0
  link = 0
  r2 = list(set(array) - set(r1))
  for s in combinations(r1,2):
    start += matrix[s[0]][s[1]]
    start += matrix[s[1]][s[0]]
  for s in combinations(r2,2):
    link += matrix[s[0]][s[1]]
    link += matrix[s[1]][s[0]]
  result = min(result, abs(start- link))

print(result)