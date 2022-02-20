import sys

sys.stdin = open("../input_py.txt", "r")

input = sys.stdin.readline

n,m,b = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))


#중간값을 구성
low = min(map(min,board))
top = max(map(max,board))
leastTime = 1e9

for i in range(low, top+1):
  plus = 0 # 위로 올릴 블럭 수
  minus = 0 # 깎아야 하는 블록 수
  for x in range(n):
    for y in range(m):
      cur = board[x][y] - i
      if cur > 0:
        minus+=cur
      elif cur < 0 :
        plus += (-cur)
  
  if minus + b >= plus:
    time =0
    time += minus*2 + plus
    if time <=leastTime:
      leastTime = time
      resultHeight = i

print(leastTime, resultHeight)

# while(top>=low):
#   inven = b
#   need = 0

#   for i in range(n):
#     for j in range(m):
#       cur = board[i][j]
#       if cur <top:
#         need += top - cur
#       if cur > top:        
#         inven += cur - top
  
#   if inven >= need:
#     remove = inven - b
#     time = 0
#     time += remove * 2
#     time += need
#     if leastTime >=time:
#       leastTime = time
#       resultHeight = top
#   top-=1