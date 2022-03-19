import sys

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0

# def check_color(paper):
#   global white, blue
#   length = len(paper)
  
#   temp = paper[0][0]
#   check = True
#   for i in range(length):
#     for j in range(length):
#       # 서로 다른 색종이가 들어 있다면 나누기
#       if temp != paper[i][j]:
#         paper[length/2][length/2]
#         paper[length/2][-length/2]
#         paper[-length/2][length/2]
#         paper[-length/2][-length/2]
#         check_color()
#         check = False
  
#   if check:
#     if temp ==0:
#       white +=1
#     else:
#       blue +=1

#   return