import sys

sys.stdin = open("./input_py.txt", "r")
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
result = [0]*3

def check(n,x,y):
  
  if n == 1:
    return True
  temp = paper[x][y]
  for i in range(x,x+n):
    for j in range(y,y+n):
      if paper[i][j] != temp:
        return False
  return True

def cut(n,x,y):
  # 더이상 자를 수 없는지 확인
  if check(n, x, y):
    result[paper[x][y]+1] += 1
    return
  
  for i in range(3):
    for j in range(3):
      cut(n//3, x+n//3*i,y+n//3*j)

cut(n,0,0)
for i in result:
  print(i)