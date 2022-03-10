import sys
sys.stdin = open("input_py.txt", "r")

T = int(input())
week = ['MON', 'TUE', 'WED', 'THU', 'FRI','SAT', 'SUN']
for idx in range(1, T+1):
  day = input()
  remaining = 6 - week.index(day)
  if remaining == 0:
    print(f'#{idx} 7')
  else:
    print(f'#{idx} {remaining}')