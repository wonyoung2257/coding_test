import sys

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split(' '))
# 원본 지도
rap = [list(map(int, input().split(' '))) for _ in range(N)]
# 벽을 설치한 복사본 지도
temp =[[0]*M for _ in range(N)]

dx = [1,-1, 0, 0]
dy = [0 ,0 ,1, -1]

def virus(x,y):
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0<= nx < N and 0<= ny <M:
      if temp[nx][ny] == 0:
        temp[nx][ny] = 2
        virus(nx,ny)
      

def get_count():
  count =0
  for i in range(N):
    for j in range(M):
      if temp[i][j] == 0:
        count +=1
  return count

result = 0
def well(count):
  global result
  if count == 3:
    # 벽을 설치한 원본지도를 복사한다.
    for i in range(N):
      for j in range(M):
        temp[i][j] = rap[i][j]
    
    # 복사 후 바이러스를 퍼트리는 함수에 바이러스 위치를 넘겨준다.
    for i in range(N):
      for j in range(M):
        if temp[i][j] == 2:
          virus(i, j)          
    # 바이러스가 다 퍼진 후 안전지역의 갯수를 세어준다.
    result = max(result, get_count())
    return

  for i in range(N):
    for j in range(M):
      if rap[i][j] == 0:
        rap[i][j] = 1
        count +=1
        well(count)
        rap[i][j] = 0
        count -= 1

well(0)
print(result)