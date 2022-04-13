import bisect
import sys
sys.stdin = open("input_py.txt", "r")

n = int(input())
card = sorted(list(map(int, input().split())))
m = int(input())
said = list(map(int, input().split()))

answer = []
for num in said:
  start = 0
  end = len(card)-1
  
  find = False
  while start <= end:
    mid = (start +end)//2

    if num == card[mid]:
      answer.append(1)
      find = True
      break
    if num > card[mid]:
      start = mid+1
    else:
      end = mid -1
  if not find:
    answer.append(0)
print(*answer)