import sys

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())

book = {}
question  = []

for i in range(1, n+1):
  monster = input().strip()
  book[i] = monster
  book[monster] = i

for _ in range(m):
  question.append(input().strip())

for i in question:
  if i.isdecimal():
    print(book[int(i)-1])
  else:
    print(book[i])