def sol():
  # n = int(input())
  n = '1234567'
  cnt = 0
  while True:
    if len(str(n)) == 1:
      print(cnt)
      print('YES') if n % 3 ==0 else print('NO')
      break
    
    add = 0
    for i in str(n):
      add += int(i)
    n = add
    cnt+=1

sol()