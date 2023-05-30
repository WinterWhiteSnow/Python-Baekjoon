import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# n_list = [list(wow()) for _ in range(one())]
# n_list.sort(key=lambda x : x[0])
# # print(n_list)
# n_list = [b for a,b in n_list]
# l = len(n_list)
# total = [0]*(l)
# total2 = [0]*l
# for i in range(l):
#     total[i]=1
#     for a in range(i):
#         # print(i,a)
#         if n_list[i]>n_list[a]:
#             total[i]=max(total[i],total[a]+1)
# print(l-max(total))

# total = [0]*(10**6+1)
# total[1]=1
# plus = 3
# for i in range(2,10**6+1):
#     total[i]=total[i-1]+plus
#     plus+=2
# for t in range(int(input())):
#     t =t+1
#     a,b = map(int,input().split())
#     print("#"+str(t),end=" ")
#     if total[a]%total[b] == 0:
#         print(total[a]//total[b])
#     else:
#         print(0)

# for t in range(int(input())):
#     t = t+1
#     l = int(input())
#     n_list = list(map(int,input().split()))
#     total = [1]*l
#     for i in range(1,l):
#         num = n_list[i]
#         for a in range(i):
#             if num > n_list[a]:
#                 total[i]=max(total[i],total[a]+1)
#     print("#"+str(t),max(total))

# total = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
# for i in range(91):
#     total.append(total[-2]+total[-3])
# for t in range(int(input())):
#     t = t+1
#     print("#"+str(t),total[int(input())-1])

# for t in range(int(input())):
#     t = t+1
#     # print(len(inputing().split()))
#     l = int(input())
#     n_list = []
#     str_str = ""
#     while len(n_list) != l:
#         a = input().split()
#         n_list.extend(a)
#         str_str+="".join(a)
#         # print(len(n_list),l)
#     index = 0
#     # print(n_list,str_str)
#     while True:
#         if str(index) not in str_str:
#             break
#         index+=1
#     print("#"+str(t),index)

# for t in range(int(input())):
#     t = t+1
#     r,k = map(int,input().split())
#     n_list = [list(map(int,input().split())) for _ in range(r)]
#     total = [0]*10001
#     for i in range(r):
#         value,c = n_list[i]
#         for w in range(k,0,-1):
#             if w > c:
#                 total[w]=max(total[w],total[w-c]+value)
#             else:
#                 break
#         # print(i,total[k])
#     print("#"+str(t),total[k])

# for t in range(int(input())):
#     t = t+1
#     n_list = list(input())
#     clap = 0
#     count = 0
#     for i in range(len(n_list)):
#         if n_list[i] != "0":
#             if clap >= i:
#                 clap+=int(n_list[i])
#             else:
#                 count+=i-clap
#                 clap+=i-clap+int(n_list[i])
#         # print(i,count,clap)
#     print("#"+str(t),count)

# for t in range(int(input())):
#     t = t+1
#     r = int(input())
#     state = [[int(input())]]
#     # print("start",state)
#     for _ in range(r-1):
#         num = int(input())
#         check = False
#         for i in range(len(state)):
#             if len(state[i])> 1:
#                 a,b = state[i][-2],state[i][-1]
#                 if b-a == num-b:
#                     state[i].append(num)
#                     check = True
#             else:
#                 state[i].append(num)
#                 check=True
#         if check == False:
#             state.append([1,num])
#     print("#"+str(t),len(state))

for t in range(int(input())):
    t = t+1
    
                
    
                





















