N = list(map(int, str(input())))


if sum(N[:len(N)//2]) == sum(N[len(N)//2:]):
  print('LUCKY')
else:
  print("READY")