import sys

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline
s = input().strip()
li = s.replace('XXXX', 'AAAA').replace('XX','BB')
answer = ''.join(li)
if 'X' in answer:
  print(-1)
else:
  print(answer)