import sys
sys.stdin = open('input_py.txt','r')
input = sys.stdin.readline

n = int(input())
arr= [list(map(int, input().split())) for _ in range(n)]

s=[]
def dfs():
  if len(s) == n:
    print(*s)
    return 
  
  for i in range(1, n+1):
    if i not in s:
      s.append(i)
      dfs()
      s.pop()

dfs()