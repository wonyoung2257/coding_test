import sys
from itertools import combinations

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

n = int(input())
board = [] # 기존 판
teachers = [] # 선생의 위치
spaces =[] # 빈 공간의 위치

for i in range(n):
  board.append(list(input().split()))
  for j in range(n):
    if board[i][j] == 'T':
      teachers.append((i, j))
    if board[i][j] =='X':
      spaces.append((i,j))

def watch(x,y, direction):
  if direction ==0:
    while y >= 0:
      if board[x][y] == 'S':
        return True
      if board[x][y] == 'O':
        return False
      y -= 1
  if direction == 1:
    while y < n:
      if board[x][y] == 'S':
        return True
      if board[x][y] == 'O':
        return False
      y +=1
  
  if direction == 2:
    while x >= 0:
      if board[x][y] == 'S':
        return True
      if board[x][y] == 'O':
        return False
      x-=1
  if direction == 3:
    while x < n:
      if board[x][y] == 'S':
        return True
      if board[x][y] == 'O':
        return False
      x +=1
  return False

def process():
  for x, y in teachers:
    for i in range(4):
      if watch(x,y,i):
        return True
  return False

find = False

for data in combinations(spaces, 3):
  print(data)
  for x, y in data:
    board[x][y] ='O'
  if not process():
    find = True
    break
  for x, y in data:
    board[x][y] ='X'

if find:
  print('YES')
else:
  print('NO')





# n = int(input())
# graph = []
# teacher = 0
# for _ in range(n):
#   data = list(input().strip().split(' '))
#   teacher += data.count('T')
#   graph.append(data)

# dx = [1,-1, 0, 0]
# dy = [0, 0, 1, -1]

# def check_S(x,y):
#   for i in range(4):
#     nx = x + dx[i]
#     ny = y + dy[i]
#     # 직선 방향으로 확인
#     while 0<= nx < n and 0<= ny < n and graph[nx][ny] !='O':
#       if graph[nx][ny] == 'S':
#         # 감시가능하다z
#         return True            
#       else:        
#         # T 나 X으면 계속 탐색
#         nx += dx[i]
#         ny += dy[i]
#   # 감시 불가능하다
#   return False

# def solution(count):
#   global answer
#   if count == 3:
#     cnt = 0
#     for i in range(n):
#       for j in range(n):
#         if graph[i][j] == 'T':
#           if not check_S(i,j):          
#             cnt+=1
#     # 모든 선생이 감시가 불가능할 때
#     if cnt == teacher:
#       answer = True
#     return

#   for i in range(n):
#     for j in range(n):
#       if graph[i][j] == 'X':
#         graph[i][j] = 'O'
#         count +=1
#         solution(count)
#         graph[i][j] = 'X'
#         count -=1

# answer = False
# solution(0)
# if answer:
#   print('YES')
# else:
#   print('NO')