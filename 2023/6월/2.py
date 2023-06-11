import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/27494
# n = one()
# if n <2023:
#     print(0)
# else:
#     cnt = 1
#     n_list = ["2","0","2","3"]
#     for i in range(2024,n+1):
#         num = str(i)
#         if i%10 == 0:
#             num = num.rstrip("0")
#         n_index = 0
#         if num.count("2") >= 2 and num.count("0")>=1 and num.count("3")>=1:
#             for number in num:
#                 if number == n_list[n_index]:
#                     n_index+=1
#                     if n_index == 4:
#                         break
#             if n_index == 4:
#                 cnt+=1
#     print(cnt)

#https://www.acmicpc.net/problem/26518
# b,c,a1,a2 = wow()
# n_list = [a1,a2]
# state = "none"
# while True:
#     x,y = n_list[-1],n_list[-2]
#     if state == "none":
#         state =x/y
#     else:
#         if state == x/y:
#             break
#         else:
#             state =x/y
#     n_list.append(b*x+c*y)
# print(state)

#https://www.acmicpc.net/problem/24725
# from collections import deque
# r,c = wow()
# n_list = [list(inputing()) for _ in range(r)]
# cnt = 0
# move = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
# for y in range(r):
#     for x in range(c):
#         q=deque()
#         if n_list[y][x] == "E" or n_list[y][x] == "I":
#             for my,mx in move:
#                 if 0<=y+my*3<r and 0<=x+mx*3<c:
#                     count = 0
#                     for i in range(1,4):
#                         if i == 1:
#                             if n_list[y+my*i][x+mx*i]== "N" or n_list[y+my*i][x+mx*i]=="S":
#                                 count+=1
#                             else:
#                                 break
#                         if i == 2:
#                             if n_list[y+my*i][x+mx*i]== "F" or n_list[y+my*i][x+mx*i]=="T":
#                                 count+=1
#                             else:
#                                 break
#                         if i == 3:
#                             if n_list[y+my*i][x+mx*i]== "P" or n_list[y+my*i][x+mx*i]=="J":
#                                 count+=1
#                             else:
#                                 break
#                     if count == 3:
#                         cnt+=1
# print(cnt)

n = list(inputing())
l = len(n)
               
        

            
            
    










        
















