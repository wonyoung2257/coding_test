import sys
sys.stdin = open("input_py.txt", "r")

x, y = map(int, input().split())
temp = (y*100) // x
if temp >= 99:
  print(-1)
  exit()

start = 1
end = x

answer = 0
while start <= end:
  mid = (start+end)//2

  if (y+mid)*100//(x+mid) <= temp:
    start = mid+1
  else:
    answer = mid
    end = mid-1

print(answer)