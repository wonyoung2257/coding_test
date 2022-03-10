import sys
sys.stdin = open("input_py.txt", "r")

T  = int(input())

for i in range(1, T+1):
  n, P_D, P_G = map(int, input().split())

  if P_G == 0 and P_D !=0:
    print(f'#{i} Broken')
    continue
  elif P_G == 100 and P_D != 100:
    print(f'#{i} Broken')
    continue
  else:
    check = False
    for q in range(1, n+1):
      if (q*P_D/100) == (q*P_D //100):
        check = True
        break
    if check:
      print(f'#{i} Possible')
    else:
      print(f'#{i} Broken')