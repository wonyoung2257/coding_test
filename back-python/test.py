def solution(dirs):
  answer = 0
  borad = [[0]*10 for _ in range(10)]
  x, y = 0, 0
  for i in dirs:
    if i == 'U':
      y+=1      
      if y<=-5 or y>=5:
        y-= 1
        continue
    elif i == 'D':
      y-=1
      if y<=-5 or y>=5:
        y+= 1
        continue
    elif i == 'L':
      x-=1
      if x<=-5 or x>=5:
        x+= 1
        continue
    elif i == 'R':
      x+=1
      if x<=-5 or x>=5:
        x-= 1
        continue
    if borad[x][y] == 0:
      borad[x][y] = 1
      answer+=1
  return answer+1

solution("LULLLLLLU")