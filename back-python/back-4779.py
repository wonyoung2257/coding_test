import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

def sol(line):
  if len(line)==1:

    return '-'
  
  print(sol(line[0:len(line)//3]), end='')
  print(' '*int(len(line)//3), end='')
  print(sol(line[0:len(line)//3]), end='')

  return ''

while True:
  n = input().strip()
  if not n :    
    break
  
  print(sol('-'*(3**int(n))))