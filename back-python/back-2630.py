import sys

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
result = [0,0]

def check(n, x,y):
  if n == 1:
    return True
  temp = paper[x][y]

  for i in range(x, x+n):
    for j in range(y,y+n):
      if temp != paper[i][j]:
        return False

  return True
def cut(n, x, y):
  if check(n,x,y):
    result[paper[x][y]] += 1
    return
  n //= 2
  cut(n, x, y)
  cut(n, x, y+n)
  cut(n, x+n, y)
  cut(n, x+n, y+n)

cut(n,0,0)
print(result[0])
print(result[1])