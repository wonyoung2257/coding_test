"""
정사각형 겹치기 x
도형은 모두 연결
정사각형은 변끼리 연결
5가지 모양을 놓아 판에 적힌 숫자가 가장 높게 만들 수 있는 값 찾기

모든 모양의 경우의 수 19가지(5가지 모양의 회전 대칭)
500 * 500 * 19 = 4,750,000번
완전탐색으로 풀만함

- 풀이 아이디어
완전탐색
1. 각 모양을 정의하여 판을 옮기며 모든 값을 찾는다.
"""
import sys
sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

def sol():
  n, m = map(int, input().split())
  board = [list(map(int, input().split()))for _ in range(n)]

  tetromino = [[(0,0),(0,1),(1,0),(1,1)],
    [(0,0),(0,1),(0,2),(0,3)], [(0,0),(1,0),(2,0),(3,0)],
    [(0,1),(1,1),(1,0),(2,0)], [(0,0), (0,1),(1,1),(1,2)],[(1,0), (1,1),(0,1),(0,2)], [(0,0),(1,0),(1,1),(2,1)],
    [(0,1), (1,0),(1,1),(1,2)],[(0,1),(1,0),(1,1),(2,1)], [(0,0),(1,0),(2,0),(1,1)], [(0,0),(0,1), (0,2),(1,1)],
    [(0,0), (1,0),(2,0),(2,1)], [(1,0),(1,1),(1,2),(0,2)], [(0,0),(0,1),(1,1),(2,1)], [(0,0),(0,1),(0,2),(1,0)],
    [(0,1),(1,1),(2,1),(2,0)], [(0,0),(1,0),(1,1),(1,2)],[(0,0),(0,1),(1,0),(2,0)], [(0,0),(0,1),(0,2),(1,2)]
    ]

  answer = 0

  for i in range(n):
    for j in range(m):
      for el in tetromino:
        temp = 0
        for x,y in el:
          dx = i + x
          dy = j + y
          
          if 0 <= dx <n and 0<= dy <m:
            temp += board[dx][dy]
          else:
            temp = 0
            break

        answer = max(temp, answer)

  print(answer)
sol()