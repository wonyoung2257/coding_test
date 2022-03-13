# s = input().strip()
s = 'ddz=z='
answer = ['c=', 'c-', 'dz=', 'd-','lj', 'nj','s=','z=']
total = 0
length = len(s)
for i in answer:  
  s = s.replace(i,'*')

print(len(s))