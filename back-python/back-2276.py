import sys
sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

T = int(input())
for i in range(T):
    
  n = int(input())
  note1 = set(map(int, input().split()))
  m = int(input())
  note2 = list(map(int, input().split()))

  answer = []
  for i in note2:
    if i in note1:
      answer.append(1)
    else:
      answer.append(0)
  
  for i in answer:
    print(i)
