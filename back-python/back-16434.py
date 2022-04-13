import math
import sys
sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

n, atk = map(int ,input().split())
room_info = []
for i in range(n):
  t, a, h = map(int ,input().split())
  room_info.append((t,a,h))

def game(mid):
  # mid 가 최대 피
  global atk
  Acur = atk
  Hcur = mid
  for t, a, h in room_info:

    if t == 1:      
      Hcur -= (math.ceil(h/Acur)-1)*a
      if Hcur <=0:
        break
    else:
      #표션일 때 a만큼 공격력 올리고 h만큼 회복
      Acur += a
      Hcur = min(mid, Hcur+h)

  return Hcur


def binary_search():
  start= 1
  end = int(1e18)
  answer = 0
  while start <= end:
    mid = start + (end-start)//2

    if game(mid) > 0:
      end = mid-1
      answer = mid
    else:
      start = mid+1
  
  return answer

print(binary_search())
