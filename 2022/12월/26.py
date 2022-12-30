import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/22351
# from collections import deque
# n_list = inputing()
# a_list = deque(n_list)
# b_list = [i for i in a_list]
# start = ""
# while True:
#     index = a_list.popleft()
#     if index != " ":
#         start+=index
#     else:
#         break
#     if len(a_list) == 0:
#         break
#     if str(int(start)+1) in n_list:
#         check = ""
#         num = int(start)
#         while len(check) < len(n_list):
#             check+=str(num)
#             num+=1
#             # print(check,start,num)
#         # print("end",check,start,)
#         if check == n_list:
#             break
# # print(start)
# end = deque()
# while True:
#     index = b_list.pop()
#     # print(index)
#     if index != " ":
#         end.appendleft(str(index))
#     else:
#         break
    
#     what = "".join(end)
#     if len(b_list) == 0:
#         break
#     if str(int(what)-1) in n_list and int(what) > int(start):
#         check = ""
#         num = int(what)
#         while len(check) < len(n_list):
#             check=str(num)+check
#             num-=1
#         if check == n_list:
#             break
# print(start,"".join(end))

#https://www.acmicpc.net/problem/3085
# r= one()
# n_list = [list(inputing()) for _ in range(r)]
# total = [0]
# for y in range(r):
#     state = "none"
#     cnt = 0
#     for i in n_list[y]:
#         if state == "none":
#             state = i
#             cnt=1
#         else:
#             if state == i:
#                 cnt+=1
#             else:
#                 total[0]=max(total[0],cnt)
#                 cnt=1
#                 state=i            
#     total[0]=max(total[0],cnt)

# sero_list = {}
# for y in range(r):
#     list_list = n_list[y]
#     for x in range(r):
#         if x not in sero_list:
#             sero_list[x]=[list_list[x]]
#         else:
#             sero_list[x]+=[list_list[x]]
# sero_list = list(sero_list.values())

# for y in range(r):
#     state = "none"
#     cnt = 0
#     for i in sero_list[y]:
#         if state == "none":
#             state = i
#             cnt=1
#         else:
#             if state == i:
#                 cnt+=1
#             else:
#                 total[0]=max(total[0],cnt)
#                 cnt=1
#                 state=i            
#     total[0]=max(total[0],cnt)


# def garo_check(list_list):
#     state = "none"
#     cnt = 0
#     max_max = 0
#     for i in list_list:
#         if state == "none":
#             state = i
#             cnt=1
#         else:
#             if state == i:
#                 cnt+=1
#             else:
#                 max_max=max(max_max,cnt)
#                 cnt=1
#                 state=i            
#     max_max=max(max_max,cnt)
#     return max_max
# def go(start_y,start_x,y,x,list_list,l):
#     temp_list = []
#     for i in list_list:
#         lol = []
#         for a in i:
#             lol.append(a)
#         temp_list.append(lol)
#     if 0<=y<=l-1 and 0<=x<=l-1:
#         if temp_list[start_y][start_x] != temp_list[y][x]:
#             temp_list[start_y][start_x],temp_list[y][x]=temp_list[y][x],temp_list[start_y][start_x]
#             a=garo_check(temp_list[start_y])
#             b=garo_check(temp_list[y])
#             sero_list = []
#             for i in range(r):
#                 sero_list.append(temp_list[i][x])
#             c=garo_check(sero_list)
#             sero_list = []
#             for i in range(r):
#                 sero_list.append(temp_list[i][start_x])
#             d = garo_check(sero_list)
#             total.append(max(a,b,c,d))
# if total[0] == r:
#     print(r)
# else:
#     for start_y in range(r):
#         for start_x in range(r):
#             go(start_y,start_x,start_y-1,start_x,n_list,r)
#             go(start_y,start_x,start_y+1,start_x,n_list,r)
#             go(start_y,start_x,start_y,start_x-1,n_list,r)
#             go(start_y,start_x,start_y,start_x+1,n_list,r)
#     print(max(total))

#https://www.acmicpc.net/problem/2210
# n_list = []
# for i in sys.stdin.readlines():
#     n_list.append(i.rstrip().split())
# l = len(n_list)
# n_dict = {}
# def go(y,x,l,str_str,list_list):
#     if len(str_str) == 6:
#         n_dict[str_str]=1
#     else:
#         if 0<=y<=l-1 and 0<=x<=l-1:
#             str_str+=list_list[y][x]
#             go(y-1,x,l,str_str,list_list)
#             go(y+1,x,l,str_str,list_list)
#             go(y,x-1,l,str_str,list_list)
#             go(y,x+1,l,str_str,list_list)
# for y in range(l):
#     for x in range(l):
#         go(y,x,l,"",n_list)
# print(len(n_dict))

#https://www.acmicpc.net/problem/2531
# from collections import deque
# r,n,k,bonus=wow()
# n_list = [one() for _ in range(r)]
# n_list +=n_list[:k]
# list_list = deque(n_list[:k])
# # print(list_list)
# max_max = len(set(list(list_list)+[bonus]))
# for i in range(1,r):
#     list_list.popleft()
#     list_list.append(n_list[i+k-1])
#     # print(set(list_list[-1]+[bonus]))
#     max_max = max(len(set(list(list_list)+[bonus])),max_max)
# print(max_max)

#https://www.acmicpc.net/problem/2961
# min_min = [1000000000*10]
# n_list = [list(wow()) for _ in range(one())]   
# def go(sin,sseun,index,l,check_list):
#     # print("start!",index,check_list)
#     a,b = n_list[index]
#     sin*=a
#     sseun+=b
#     # print(sin,sseun)
#     min_min[0]=min(min_min[0],abs(sin-sseun))
#     for i in range(l):
#         if i not in check_list:
#             go(sin,sseun,i,l,check_list+[i])
# for i in range(len(n_list)):
#     a,b = n_list[i]
#     min_min[0]=min(min_min[0],abs(a-b))
#     go(1,0,i,len(n_list),[i])
# print(min_min[0])

#https://www.acmicpc.net/problem/12919
# a = inputing()
# b = list(inputing())
# total = [0]
# def go(list_list,l,answer):
#     if l != len(list_list):
#         check1 = list_list[-1]
#         check2 = list_list[::-1][-1]
#         if check1=="A":
#             go(list_list[:-1],l,answer)
#         if check2 == "B":
#             go(list_list[::-1][:-1],l,answer)
#     else:
#         # print(list_list)
#         total.append(1 if answer == "".join(list_list) else 0)
# go(b,len(a),a)
# print(max(total))




