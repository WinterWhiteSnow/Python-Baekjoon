import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/11568
# l = one()
# n_list = list(wow())
# total = [1]*(l+1)
# for i in range(1,l+1):
#     num = n_list[i-1]
#     for w in range(1,i):
#         num2 = n_list[w-1]
#         if num > num2:
#             total[i]=max(total[i],total[w]+1)
# print(max(total))

#https://www.acmicpc.net/problem/18353
# l = one()
# n_list = list(wow())
# total = [1]*l
# for i in range(1,l):
#     num = n_list[i]
#     for a in range(i):
#         num2 = n_list[a]
#         if num2 > num:
#             total[i]=max(total[i],total[a]+1)
# print(l-max(total))

# n_dict = {}
# n_list = []
# for i in range(2,int((10**7)**(1/2))+1):
#     if i not in n_dict:
#         for a in range(i,int((10**7)**(1/2))+1,i):
#             n_dict[a]=0
#         n_list.append(i)
# answer = []
# def check(num):
#     num = int(num**(1/2))+1
#     start = 0
#     end = len(n_list)-1
#     while start<=end:
#         mid = (start+end)//2
#         if n_list[mid]>num:
#             end = mid-1
#         else:
#             start=mid+1
#     # print(start,end,n_list[start],n_list[end],num)
#     return end
# for t in range(int(input())):
#     t = t+1
#     n = int(input())
#     end_index = check(n)
#     count = 1
#     for i in range(end_index+1):
#         x = n_list[i]
#         cnt = 0
#         if n%x == 0:
#             while n%x == 0 and x <= n:
#                 cnt+=1
#                 n//=x
#         if cnt%2 == 1:
#             count*=x
#     total = count*n
#     answer.append(f"#{t} {total}")
#     # print(f"#{t} {total}")
# print(*answer,sep="\n")   
  
import string
str_str = list(string.ascii_lowercase)

for t in range(int(input())):
    t = t+1
    a = input().rstrip()   
    b = input().rstrip()   
    a_l = len(a)
    b_l = len(b)
    min_min = min(a_l,b_l)
    max_max = max(a_l,b_l)
    
# print(*answer,sep="\n")
        












