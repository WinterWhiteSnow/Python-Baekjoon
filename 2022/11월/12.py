import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/22970
# l = one()
# n_list = list(wow())
# max_max = 0
# for start in range(l):
#     le =  1
#     state = "plus"
#     number = "none"
#     for a in range(start,l):
#         if number == "none":
#             number = n_list[a]
#         else:
#             if state == "plus":
#                 if number < n_list[a]:
#                     number=n_list[a]
#                     le+=1
#                 elif number == n_list[a]:
#                     break
#                 else:
#                     number = n_list[a]
#                     le+=1
#                     state = "minus"
#             else:
#                 if number < n_list[a]:
#                     break
#                 elif number == n_list[a]:
#                     break
#                 else:
#                     le+=1
#                     number=n_list[a]
#     max_max = max(max_max,le)
# print(max_max)

#https://www.acmicpc.net/problem/4881
# def go(num,n_dict):
#     if num not in n_dict:
#         n_dict[num]=1
#     else:
#         return
#     num = list(map(int,list(str(num))))
#     cnt = 0
#     for i in num:
#         cnt+=i**2
#     num = cnt
#     go(num,n_dict)
        
# while True:
#     a,b = wow()
#     if a==b==0:
#         break
#     a_dict = {}
#     b_dict = {}
#     go(a,a_dict)
#     go(b,b_dict)
#     # print(a_dict)
#     # print(b_dict)
#     a_list = list(a_dict.keys())
#     b_list = list(b_dict.keys())
#     check = set(a_list)&set(b_list)
#     min_min = 100001
#     if len(check) != 0:
#         for i in check:
#             a_index = a_list.index(i)+1
#             b_index = b_list.index(i)+1
#             min_min=min(min_min,a_index+b_index)
#         print(a,b,min_min)
#     else:
#         print(a,b,0)

#https://www.acmicpc.net/problem/1021
# n,l = wow()
# n_list = [i for i in range(1,n+1)]
# a_list = list(wow())
# cnt = 0
# for i in a_list:
#     p_index = n_list.index(i)
#     m_index=len(n_list)-p_index
#     # print(n_list,p_index,i)
#     cnt+=min(p_index,m_index)
#     n_list = n_list[p_index:]+n_list[:p_index]
#     del n_list[n_list.index(i)]
#     # print(n_list,cnt)
# print(cnt)

#https://www.acmicpc.net/problem/1740
# num = one()
# index = 0
# cnt = 0
# for i in bin(num)[2:][::-1]:
#     cnt+=int(i)*(3**index)
#     index+=1
# print(cnt)

#https://www.acmicpc.net/problem/16439
# n,l = wow()
# n_list = [list(wow()) for _ in range(n)]
# max_max = 0
# n_dict = {}
# for y in range(n):
#     for x in range(l):
#         if x not in n_dict:
#             n_dict[x]=[]
#         n_dict[x]+=[n_list[y][x]]

# for a in range(l-2):
#     for b in range(a+1,l-1):
#         for c in range(b+1,l):
#             x=n_dict[a]
#             y=n_dict[b]
#             z=n_dict[c]
#             cnt = 0
#             for index in range(n):
#                 count = max(x[index],y[index],z[index])
#                 cnt+=count
#             max_max=max(cnt,max_max)
# print(max_max)

#https://www.acmicpc.net/problem/21920
# import math
# l = one()
# n_list = list(wow())
# num = one()
# cnt = 0
# count = 0
# for i in n_list:
#     if math.gcd(i,num) == 1:
#         count+=1
#         cnt+=i
# print(cnt/count)

#https://www.acmicpc.net/problem/13414
# n_dict = {}
# limit,r = wow()
# for _ in range(r):
#     a = inputing()
#     if len(a) == 8:
#         if a not in n_dict:
#             n_dict[a]=1
#         else:
#             del n_dict[a]
#             n_dict[a]=1
#         # print(n_dict)
# print(*list(n_dict.keys())[:limit],sep="\n")
    
num = one()
cnt = [0]
n_dict = {}
def go(number):
    cnt[0]+=1
    cnt[0]%=1000000007
    if number in n_dict:
        return n_dict[number]
    if number < 2:
        print(number,n_dict,cnt)
        n_dict[number]=cnt[0]
        return
    else:
        print("wow",number)
        return go(number-2)+go(number-1)
go(num)
print(n_dict[num-1],n_dict[num-2])











    
    






