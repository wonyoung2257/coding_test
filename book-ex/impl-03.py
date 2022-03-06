N = 'c2'

x = int(ord(N[0])-96)
y = int(N[1])

dx = [2, 2,-2, -2, 1,-1 ,1,-1]
dy = [1,-1, 1, -1, 2,2, -2, -2]

cnt = 0
for i in range(len(dx)):
  nx = x+dx[i]
  ny = y+dy[i]
  if 1<=nx <=8 and 1<=ny <=8:
    cnt+=1
    print(nx, ny)

print(cnt)