import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/14430
# r,l = wow()
# n_list = [list(wow()) for _ in range(r)]
# for i in range(1,l):
#     n_list[0][i]+=n_list[0][i-1]
# for y in range(1,r):
#     for x in range(l):
#         if x == 0:
#             n_list[y][x]+=n_list[y-1][x]
#         else:
#             n_list[y][x]+=max(n_list[y-1][x],n_list[y][x-1])
# print(n_list[r-1][l-1])

# for t in range(int(input())):
#     t = t+1
#     str_str = ""
#     l = int(input())
#     cnt = 0
#     while True:
#         temp_str = input()
#         for m in ["?",".","!"]:
#             cnt+=temp_str.count(m)
#             temp_str = temp_str.replace(m,"@")
#         str_str+=temp_str
#         if cnt == l:
#             break
#     str_str = str_str.split("@")[:-1]
#     a = len(str_str)
#     total = [0]*a
#     for i in range(a):
#         new_list = str_str[i].split()
#         count = 0
#         for n in new_list:
#             if n[0].isupper():
#                 check = True
#                 for index in range(1,len(n)):
#                     if n[index].islower():
#                         pass
#                     else:
#                         check = False
#                         break
#                 if check:
#                     count+=1
#         total[i]=count
#     print("#"+str(t),*total)     

# for t in range(int(input())):
#     t = t+1
#     r,k = map(int,input().split())
#     total = [[0]*(k+1) for _ in range(r+1)]
#     for i in range(1,r+1):
#         weight,value = map(int,input().split())
#         for w in range(1,k+1):
#             if w < weight:
#                 total[i][w]=total[i-1][w]
#             else:
#                 total[i][w]=max(total[i-1][w],total[i-1][w-weight]+value)
#     print("#"+str(t),total[r][k])
# answer = []
# for t in range(int(input())):
#     t = t+1
#     n = list(input())
#     while len(n) > 1:
#         new_list = list(str(sum(list(map(int,n)))))
#         n = new_list
#     answer.append(f"#{t} {n[0]}")
# for i in answer:
#     print(i)

# for t in range(int(input())):
#     t = t+1
#     a,b = map(int,input().split())
#     a_list = set(input().split())
#     b_list = set(input().split())
#     c_list = a_list & b_list
#     print("#"+str(t),len(c_list))

# import heapq    
# list_list =  []
# for t in range(int(input())):
#     t = t+1
#     r = int(input())
#     h = []
#     answer = [f"#{t}"]
#     # print("#"+str(t),end=" ")
#     for _ in range(r):
#         order = input()
#         if order[0]=="1":
#             a,b = order.split()
#             b = int(b)
#             heapq.heappush(h,-b)
#         else:
#             if len(h) > 0:
#                 answer.append(-heapq.heappop(h))
#             else:
#                 answer.append(-1)
#     # list_list.append()
#     list_list.append(answer)
# for i in list_list:
#     print(*i)

# answer=  []

# for t in range(int(input())):
#     t = t+1
#     a,b,c,d = map(int,input().split())
#     x,y = max(a,c),min(b,d)
#     # print(x,y)
#     gap = y-x
#     if gap <0:
#         gap = 0
#     answer.append(f"#{t} {gap}")
#     # print("#"+str(t),gap)
# for i in answer:
#     print(i)
# from collections import deque
# for t in range(int(input())):
#     t = t+1
#     num = int(input())
#     n_list = deque(list(map(int,input().split())))
#     answer_list = []
#     for _ in range(7):
#         n_list.rotate(-1)
#         zero_list = [i for i in list(n_list)]
#         index = 1
#         for i in range(7):
#             if zero_list[i] == 1:
#                 zero_list[i]=index
#                 index+=1
#         total = sum(n_list)
#         if num%total != 0:
#             day = num//total*7
#             remainder = num%total
#             day+=zero_list.index(remainder)+1
#             # print(day)
#         else:
#             day = (num-total)//total*7
#             day+=zero_list.index(total)+1
#         answer_list.append(day)
#         # print(total,zero_list,day)
#     # print(answer_list)
#     print("#"+str(t),min(answer_list))

wow = lambda : map(int,input().split())
one = lambda : int(input())
# for t in range(int(input())):
#     t = t+1
#     l = int(input())
#     n_list = list(wow())
#     zero_list = [0]*l
#     zero_list[0]=n_list[0]
#     for i in range(1,l):
#         zero_list[i]=max(zero_list[i-1]+n_list[i],n_list[i])
#     print("#"+str(t),max(zero_list))



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    