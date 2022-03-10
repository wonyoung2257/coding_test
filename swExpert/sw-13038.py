import sys
sys.stdin = open("input_py.txt", "r")

T = int(input())
for idx in range(1, T+1):
  n = int(input())
  week = list(map(int, input().split(' ')))
  total_day = 0
  study_cnt = week.count(1)
  
  if n >study_cnt and n != 2 and n!= 1:
    total_day = (n-1)//study_cnt*7
    n = (n-1)%study_cnt +1
  
  min_day = 999999999
  for i, val in enumerate(week):
    day_cnt= 0
    temp = n
    if val == 1:
      j = i
      while temp !=0:
        day_cnt+=1
        if week[j%7] == 1:
          temp -= 1
        j+=1
      min_day = min(min_day, day_cnt)
  print(f'#{idx} {min_day+total_day}') 