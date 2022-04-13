#
n = int(input())

def moo(length, center, n):
  prev = (length-center)//2

  if n < prev:
    # 왼쪽
    moo(prev,center-1,n)
  elif n > prev + center:
    # 오른쪽
    moo(prev,center-1, n-(prev + center))
  else:
    if n-prev == 1:
      print('m')
    else:
      print('o')


length = 0
k = 0
while length < n:
  length = 2*length+ k+3
  k+=1

moo(length, k+2, n)