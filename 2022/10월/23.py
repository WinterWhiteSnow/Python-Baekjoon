import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/3036
# import math
# l = one()
# n_list = list(wow())
# start = n_list[0]
# n_list = n_list[1:]
# for i in n_list:
#     gcd = math.gcd(i,start)
#     a = start//gcd
#     b = i//gcd
#     print(f"{a}/{b}")

#https://www.acmicpc.net/problem/1244
# l = one()
# n_list = list(wow())
# r = one()
# for _ in range(r):
#     a,b = wow()
#     if a == 1:
#         for index in range(b-1,l,b):
#             n_list[index]= not n_list[index]
#     else:
#         index = b-1
#         start = index-1
#         end = index+1
#         # print("start!!!!",start,end)
#         if 0<=start<=l-1 and 0<=end<=l-1:
#             if n_list[start] == n_list[end]:
#                 while 0<=start<=l-1 and 0<=end<=l-1:
#                     if n_list[start] == n_list[end]:
#                         if 0<=start-1<=l-1 and 0<=end+1<=l-1:
#                             if n_list[start-1] == n_list[end+1]:
#                                 start-=1
#                                 end+=1
#                             else:
#                                 break
#                         else:
#                             break
#                     else:
#                         break
#                 # print(start,end)
#                 for i in range(start,end+1):
#                     n_list[i]= not n_list[i]
#             else:
#                 n_list[b-1]= not n_list[b-1]
#         else:
#             n_list[b-1]= not n_list[b-1]
#     # print(n_list)
# for i in range(len(n_list)):
#     n_list[i]=1 if n_list[i] == True else 0
# for i in range(0,len(n_list),20):
#     print(*n_list[i:i+20])

#https://www.acmicpc.net/problem/2578
# n_list = [list(wow()) for _ in range(5)]
# a_list = [list(wow()) for _ in range(5)]
# garo_dict = {}
# sero_dict = {}
# diagonal_dict = {"plus":[],"minus":[]}
# for i in range(5):
#     garo_dict[i]=n_list[i]
#     for index in range(5):
#         if index not in sero_dict:
#             sero_dict[index]=[n_list[i][index]]
#         else:
#             sero_dict[index]+=[n_list[i][index]]
# for i in range(5):
#     diagonal_dict["plus"]+=[n_list[i][i]]
#     diagonal_dict["minus"]+=[n_list[i][4-i]]
# cnt = 0
# key_list = ["plus","minus"]
# count = 0
# for y in range(5):
#     for x in range(5):
#         count+=1
#         num = a_list[y][x]
#         for i in range(5):
#             if num in garo_dict[i]:
#                 index = garo_dict[i].index(num)
#                 garo_dict[i][index]="X"
#                 if garo_dict[i].count("X") == 5:
#                     cnt+=1
#                 break
#         for i in range(5):
#             if num in sero_dict[i]:
#                 index = sero_dict[i].index(num)
#                 sero_dict[i][index]="X"
#                 if sero_dict[i].count("X") == 5:
#                     cnt+=1
#                 break
#         for key in key_list:
#             if num in diagonal_dict[key]:
#                 index = diagonal_dict[key].index(num)
#                 diagonal_dict[key][index]="X"
#                 if diagonal_dict[key].count("X") == 5:
#                     cnt+=1
#                     del key_list[key_list.index(key)]
#         if cnt >= 3:
#             print(count)
#             exit()
#     if cnt == 3:
#         break
    # print(y,x,cnt,count)
    # print("가로")
    # for i in range(5):
    #     print(*garo_dict[i])
    # print("세로")
    # for i in range(5):
    #     print(*sero_dict[i])
    # for key in key_list:
    #     print(diagonal_dict[key])

#https://www.acmicpc.net/problem/10157
# location = [[0,1],[1,0],[0,-1],[-1,0]]
# location_index = 0
# index = 1
# l,r = wow()
# answer = one()
# if l*r >= answer:
#     n_list = [[0]*l for _ in range(r)]
#     x,y =0,0
#     while index <= l*r:
#         if 0<=x<=l-1 and 0<=y<=r-1:
#             if n_list[y][x] == 0:
#                 n_list[y][x]=index
#                 if index == answer:
#                     # print("first")
#                     print(x+1,y+1)
#                     exit()
#                 x+=location[location_index][0]
#                 y+=location[location_index][1]
#             else:
#                 x-=location[location_index][0]
#                 y-=location[location_index][1]
#                 location_index+=1
#                 location_index%=4
#                 x+=location[location_index][0]
#                 y+=location[location_index][1]
#                 if n_list[y][x] != 0:
#                     break
#                 else:
#                     n_list[y][x]=index
#                     if index == answer:
#                         # print("second")
#                         print(x+1,y+1)
#                         exit()
#                     x+=location[location_index][0]
#                     y+=location[location_index][1]
#         else:
#             x-=location[location_index][0]
#             y-=location[location_index][1]
#             location_index+=1
#             location_index%=4
#             x+=location[location_index][0]
#             y+=location[location_index][1]
#             if n_list[y][x] != 0:
#                 break
#             else:
#                 n_list[y][x]=index
#                 if index == answer:
#                     # print("third")
#                     print(x+1,y+1)
#                     exit()
#                 x+=location[location_index][0]
#                 y+=location[location_index][1]
#         # for i in range(r):
#         #     print(*n_list[i])
#         index+=1
# else:
#     print(0)

#https://www.acmicpc.net/problem/13900
# l = one()
# n_list = list(wow())
# zero_list = [sum(n_list[1:])]
# for i in n_list[1:]:
#     zero_list.append(zero_list[-1]-i)
# cnt = 0
# for i in range(l):
#     cnt+=n_list[i]*zero_list[i]
# print(cnt)

#https://www.acmicpc.net/problem/11502
# n_dict = {}
# for i in range(2,1001):
#     if i not in n_dict:
#         for ii in range(i,1001,i):
#             n_dict[ii]=0
#         n_dict[i]=1
# list_list = [a for a,b in n_dict.items() if b == 1]
# for _ in range(one()):
#     a = one()
#     check = "no"
#     for x in range(len(list_list)-2):
#         for y in range(x+1,len(list_list)-1):
#             xx = list_list[x]
#             yy = list_list[y]
#             zz = a-(xx+yy)
#             if zz in list_list:
#                 a_list = [xx,yy,zz]
#                 print(*sorted(a_list))
#                 check = "yes"
#             if check == "yes":
#                 break
#             if xx+yy+zz > a:
#                 break
#         if check == "yes":
#             break
#     if check == "no":
#         print(0)
            

        
            








