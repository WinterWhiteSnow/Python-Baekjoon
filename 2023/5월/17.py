import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1025
# r,c = wow()
# n_list = [list(inputing()) for _ in range(r)]
# list_list = []
# max_max = -1
# def away(text):
#     text = [i for i in text]
#     while len(text) != 0:
#         t = "".join(text)
#         x = int(t)
#         y = x**(1/2)
#         if x==int(y)**2:
#             return x
#         text.pop()
#     return "X"
# new_list = []
# for i in range(r):
#     a = n_list[i]
#     A,B = away(a),away(a[::-1])
#     if type(A) == int:
#         max_max = max(max_max,A)
#     if type(B) == int:
#         max_max= max(max_max,B)
# move = [(1,0),(0,1),(1,1),(0,-1),(-1,0),(-1,-1),(-1,1),(1,-1)]

# for y in range(r):
#     for x in range(c):
#         for step in range(1,max(r,c)+1):
#             for plus in range(0,max(r,c)+1):
#                 #남동쪽
#                 str_str = ""
#                 y_index,x_index = y,x
#                 str_str+=n_list[y][x]
#                 while y_index<r and x_index<c:
#                     y_index+=plus
#                     x_index+=step
#                     if 0<=y_index<r and 0<=x_index<c:
#                         pass
#                     else:
#                         break
#                     str_str+=n_list[y_index][x_index]
#                 A,B=away(list(str_str)),away(list(str_str)[::-1])
#                 if type(A)==int:
#                     max_max = max(max_max,A)
#                 if type(B)==int:
#                     max_max=max(max_max,B)
#                 #북동쪽
#                 str_str = ""
#                 y_index,x_index = y,x
#                 str_str+=n_list[y][x]
#                 while y_index<r and x_index<c:
#                     y_index-=plus
#                     x_index+=step
#                     if 0<=y_index<r and 0<=x_index<c:
#                         pass
#                     else:
#                         break
#                     str_str+=n_list[y_index][x_index]
#                 A,B=away(list(str_str)),away(list(str_str)[::-1])
#                 if type(A)==int:
#                     max_max = max(max_max,A)
#                 if type(B)==int:
#                     max_max=max(max_max,B)
#                 #남서쪽
#                 str_str = ""
#                 str_str+=n_list[y][x]
#                 y_index,x_index = y,x
#                 while y_index<r and x_index>=0:
#                     y_index+=plus
#                     x_index-=step
#                     if 0<=y_index<r and 0<=x_index<c:
#                         pass
#                     else:
#                         break
#                     str_str+=n_list[y_index][x_index]
#                 A,B=away(list(str_str)),away(list(str_str)[::-1])
#                 if type(A)==int:
#                     max_max = max(max_max,A)
#                 if type(B)==int:
#                     max_max=max(max_max,B)
#                 #북서쪽
#                 str_str = ""
#                 str_str+=n_list[y][x]
#                 y_index,x_index = y,x
#                 while y_index<r and x_index>=0:
#                     y_index-=plus
#                     x_index-=step
#                     if 0<=y_index<r and 0<=x_index<c:
#                         pass
#                     else:
#                         break
#                     str_str+=n_list[y_index][x_index]
#                 A,B=away(list(str_str)),away(list(str_str)[::-1])
#                 if type(A)==int:
#                     max_max = max(max_max,A)
#                 if type(B)==int:
#                     max_max=max(max_max,B)
#                 #동쪽
#                 str_str = ""
#                 str_str+=n_list[y][x]
#                 y_index,x_index = y,x
#                 while y_index<r and x_index<c:
#                     x_index+=step
#                     if 0<=y_index<r and 0<=x_index<c:
#                         pass
#                     else:
#                         break
#                     str_str+=n_list[y_index][x_index]
#                 A,B=away(list(str_str)),away(list(str_str)[::-1])
#                 if type(A)==int:
#                     max_max = max(max_max,A)
#                 if type(B)==int:
#                     max_max=max(max_max,B)
#                 #서쪽
#                 str_str = ""
#                 str_str+=n_list[y][x]
#                 y_index,x_index = y,x
#                 while y_index<r and x_index<c:
#                     x_index-=step
#                     if 0<=y_index<r and 0<=x_index<c:
#                         pass
#                     else:
#                         break
#                     str_str+=n_list[y_index][x_index]
#                 A,B=away(list(str_str)),away(list(str_str)[::-1])
#                 if type(A)==int:
#                     max_max = max(max_max,A)
#                 if type(B)==int:
#                     max_max=max(max_max,B)
#                 #남쪽
#                 str_str = ""
#                 str_str+=n_list[y][x]
#                 y_index,x_index = y,x
#                 while y_index<r and x_index>=0:
#                     y_index+=step
#                     if 0<=y_index<r and 0<=x_index<c:
#                         pass
#                     else:
#                         break
#                     str_str+=n_list[y_index][x_index]
#                 # print("wow!",str_str)
#                 A,B=away(list(str_str)),away(list(str_str)[::-1])
#                 if type(A)==int:
#                     max_max = max(max_max,A)
#                 if type(B)==int:
#                     max_max=max(max_max,B)
#                 #북쪽
#                 str_str = ""
#                 str_str+=n_list[y][x]
#                 y_index,x_index = y,x
#                 while y_index<r and x_index>=0:
#                     y_index-=step
#                     if 0<=y_index<r and 0<=x_index<c:
#                         pass
#                     else:
#                         break
#                     str_str+=n_list[y_index][x_index]
#                 A,B=away(list(str_str)),away(list(str_str)[::-1])
#                 if type(A)==int:
#                     max_max = max(max_max,A)
#                 if type(B)==int:
#                     max_max=max(max_max,B)
# print(max_max)

                
            















