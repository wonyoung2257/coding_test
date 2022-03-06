from shutil import move
import sys
sys.stdin = open("input_py.txt", "r")

input = sys.stdin.readline

N, M = map(int, input().split())
x, y, d = map(int, input().split())
moveArr = [[0]*N for _ in range(M)]
board = [list(map(int, input().split(' '))) for _ in range(M)]

# 초기 위치 이동 처리
moveArr[x][y] = 1 
dx = [0, 1,0, -1]
dy = [1, 0,-1, 0]

def moveLeft():
  global d
  d-=1
  if d <0:
    d = 3

cnt = 1
turnTime = 0
while True:
  # 1. 현재 방향(d)를 기준으로 왼쪽 방향으로 돌림
  # 2. 돌린쪽에 갈 수 있는 방향이면 전진, 갈 수 없으면 다시 1번
  # 3. 네 방향 모두 방문했거나 바다면 바라보는 방향을 유지한테 한칸 뒤로 이동 뒤가 바다면 멈춤
  
  moveLeft()
  
  nx = x + dx[d]
  ny = y + dy[d]
  # 이동가능한 위치가 가보지 않은 칸이고 바다가 아닐때
  if moveArr[nx][ny] == 0 and board[nx][ny] == 0:
    moveArr[nx][ny] =1
    x, y = nx, ny
    turnTime = 0
    cnt +=1
    continue
  else:
    turnTime += 1 
  if turnTime == 4:
    # 4방향 모두 갈때가 없음
    
    if board[x][y] == 1:
      break
    else:
      x -= dx[d]
      y -= dx[d]
    turnTime = 0

print(cnt)