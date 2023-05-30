import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1644
# n_dict = {}
# num = one()
# n_list = [1]*(num+1)
# for i in range(2,num+1):
#     if n_list[i]:
#         for a in range(i*2,num+1,i):
#             n_list[a]=0
# n_list = [i for i in range(2,num+1) if n_list[i]]
# count = 0
# l = len(n_list)
# # print(n_list)
# start = 0
# while start<l:
#     end = start
#     cnt = n_list[start]
#     # print("Start",cnt)
#     while end<l:
#         # print(start,end,cnt)
#         if end+1<l and cnt<num:
#             end+=1
#             cnt+=n_list[end]
#         else:
#             break
#     if cnt == num:
#         count+=1
#     start+=1
# print(count)

#https://www.acmicpc.net/problem/2023
# n = one()
# index = 10**n
# num_list = ["2","3","5","7"]
# def go(list_list):
#     new_list = []
#     for a in list_list:
#         for i in range(10):
#             b = a
#             b+=str(i)
#             # print(b,int(int(b)**(1/2))+1)
#             check = "yes"
#             for index in range(2,int(int(b)**(1/2))+1):
#                 if int(b)%index == 0:
#                     check = "no"
#                     break
#             if check == "yes":
#                 new_list.append(b)
#     # print(new_list)
#     return new_list
# for _ in range(n-1):
#     num_list = go(num_list)
# for i in sorted(num_list):
#     print(i)

num = one()
cnt = 0
for i in range(1,num+1):
    if num%i == 0:
        print(i,cnt)
        cnt+=num//i
print(cnt)
        
            











