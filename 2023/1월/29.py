import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/2580
# n_list = [list(wow()) for _ in range(9)]
# index_list = []
# for y in range(9):
#     for x in range(9):
#         if n_list[y][x] == 0:
#             index_list.append((y,x))

# def triangle(y,x,i):
#     y_index =y//3*3
#     x_index =x//3*3
#     for yy in range(3):
#         for xx in range(3):
#             if n_list[y_index+yy][xx+x_index] == i:
#                 return False
#     return True

# def sero(x,i):
#     for y in range(9):
#         if n_list[y][x] == i:
#             return False
#     return True

# def garo(y,i):
#     for x in range(9):
#         if n_list[y][x] == i:
#             return False
#     return True

# def go(index):
#     if index == len(index_list):
#         for i in range(9):
#             print(*n_list[i])
#         exit()
#     y,x = index_list[index]
#     for i in range(1,10):
#         if triangle(y,x,i) and sero(x,i) and garo(y,i):
#             n_list[y][x]=i
#             go(index+1)
#             n_list[y][x]=0
# go(0)

n_list = [list(map(list(inputing()))) for _ in range(9)]


            













