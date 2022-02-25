from lib2to3.pgen2 import grammar
import sys
sys.stdin = open("input_py.txt", "r")

N = int(input())
arr = list(map(int, input().split()))
remove = int(input())

graph = [[] for _ in range(N)]

for i in range(N):
  if arr[i] == -1:
    continue
  graph[arr[i]].append(i)
  graph[i].append(arr[i])

print(graph)