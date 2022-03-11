import sys

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().split(' '))

answer = 0
while str(bin(N)).count('1') > K:
  plus = 2 ** (bin(N)[::-1].index('1'))
  answer += plus
  N += plus
print(answer)
