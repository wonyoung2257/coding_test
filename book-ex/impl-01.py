from importlib.abc import SourceLoader


def solution(string):
  N =5
  string = string.split(' ')
  
  dx = [0, 0, -1, 1]
  dy = [-1 , 1, 0, 0]
  move = ['L', 'R', 'U', 'D']
  x ,y = 1, 1
  for i in string:
    idx = move.index(i)
    if 1<= x+dx[idx] <=5  and 1<=y+dy[idx] <=5:
      x += dx[idx]
      y += dy[idx]
  print(x, y)


solution('R R R U D D')