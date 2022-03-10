import sys
sys.stdin = open("input_py.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
  num = int(input())
  print(f'#{test_case} {num//3}')
