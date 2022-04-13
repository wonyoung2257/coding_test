# def solution(member, N, start, end):
#     temp = []
#     if N == 2:
#         for i in range(start, start+N):
#             for j in range(end, end+N):
#                 temp.append(member[i][j])
#         temp.sort()
#         return temp[1]
#     else:
#         temp.append(solution(member, N//2, start, end))
#         temp.append(solution(member, N//2, start, end+N//2))
#         temp.append(solution(member, N//2, start+N//2, end))
#         temp.append(solution(member, N//2, start+N//2, end+N//2))
#         temp.sort()
#         return temp[1]
# N = int(input())
# members = [list(map(int, input().split())) for i in range(N)]
# answer = []
# if N == 1:
#     answer.append(members[0][0])
# else:
#     answer.append(solution(members, N, 0, 0))
# print(answer[0])

# 포기!
import sys
sys.setrecursionlimit(10**8)
sys.stdin = open("input_py.txt", "r")

n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]

def sol(n, x, y):
  if n == 2:
    x -=1
    y -=1
    return sorted([table[x][y], table[x-1][y], table[x][y-1], table[x-1][y-1]])[1]
  num1 = (sol(n//2, x- n//2, y- n//2))
  num2 = (sol(n//2, x, y- n//2))
  num3 = (sol(n//2, x- n//2, y))
  num4 = (sol(n//2, x, y))
  return sorted([num1, num2, num3,num4])[1]
if n ==1:
  print(table[0][0])
else:
  print(sol(n,n,n))