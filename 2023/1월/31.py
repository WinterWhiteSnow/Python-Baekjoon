import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/4056
# def sero(x,i):
#     for index in range(9):
#         if n_list[index][x]==i:
#             return False
#     return True

# def garo(y,i):
#     for index in range(9):
#         if n_list[y][index]==i:
#             return False
#     return True

# def triangle(y,x,i):
#     yy,xx = y//3*3,x//3*3
#     for y_index in range(3):
#         for x_index in range(3):
#             if n_list[y_index+yy][x_index+xx]==i:
#                 return False
#     return True

# def go(index,l):
#     global check
#     global num
#     if index == l:
#         if check == "no":
#             check="yes"
#             c = "yes"
#             for y in range(9):
#                 for x in range(9):
#                     if check_garo(y) and check_sero(x) and check_tri(x,y):
#                         pass
#                     else:
#                         c = "no"
#                         break
#                 if c == "no":
#                     break
#             if num != 0:
#                 print()
#             if c == "yes":
#                 for i in n_list:
#                     print(*i,sep="")
#             else:
#                 print("Could not complete this grid.")
#         return
    
#     y,x = index_list[index]
#     for i in range(1,10):
#         if sero(x,i) and garo(y,i) and triangle(y=y,x=x,i=i):
#             n_list[y][x]=i
#             go(index+1,l)
#             n_list[y][x]=0
# def check_sero(x):
#     n_dict = {}
#     for y in range(9):
#         a = n_list[y][x]
#         if a not in n_dict:
#             n_dict[a]=1
#         else:
#             return False
#     return True
# def check_garo(y):
#     n_dict = {}
#     for x in range(9):
#         # print("now",x)
#         a = n_list[y][x]
#         if a not in n_dict:
#             n_dict[a]=1
#         else:
#             return False
#     return True

# def check_tri(x,y):
#     n_dict = {}
#     xx,yy=x//3*3,y//3*3
#     for xxx in range(3):
#         for yyy in range(3):
#             a = n_list[xxx+xx][yyy+yy]
#             if a not in n_dict:
#                 n_dict[a]=1
#             else:
#                 return False
#     return True
# for num in range(one()):
#     n_list = [list(map(int,list(inputing()))) for _ in range(9)]

#     index_list = []
#     check = "no"
#     for y in range(9):
#         for x in range(9):
#             if n_list[y][x] == 0:
#                 index_list.append((y,x))
#     go(0,len(index_list))
#     if check == "no":
#         if num != 0:
#             print()
#         print("Could not complete this grid.")
import string
str_str = list(string.ascii_uppercase)
r,l = wow()
n_list = [list(inputing()) for _ in range(r)]
cnt = 0
visited = [0]*(len(str_str))
#직접 n_dict에 확인해보는건?
def go(y,x,r,l,visited,count):
    # print("start!",y,x,count,visited)
    global cnt
    if 0<=y<=r-1 and 0<=x<=l-1:
        if n_list[y][x] not in visited:
            visited[n_list[y][x]]=1
            move = [[0,1],[0,-1],[1,0],[-1,0]]
            for yy,xx in move:
                go(yy+y,xx+x,r,l,visited,count+1)
            del visited[n_list[y][x]]
        else:
            cnt = max(cnt,count)
    else:
        cnt = max(cnt,count)
go(0,0,r,l,{},0)
print(cnt)