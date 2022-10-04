import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#23881
# l,k = wow()
# n_list = list(wow())
# m_list = sorted(n_list)
# cnt = 0
# index = -1
# n_dict = {}
# while l != 0:
#     max_max = n_list.index(max(n_list[:l]))
#     check = m_list.index(max(n_list[:l]))
#     if max_max == check:
#         pass
#     else:
#         cnt+=1
#         n_dict[cnt]=sorted([n_list[max_max],n_list[index]])
#         n_list[max_max],n_list[index]=n_list[index],n_list[max_max]
#     index-=1
#     l-=1
# if k in n_dict:
#     print(*n_dict[k])
# else:
#     print(-1)

#23882
# l,k = wow()
# n_list = list(wow())
# index = l-1
# n_dict = {}
# cnt = 0
# new_list = []
# while l != 0:
#     max_max = n_list.index(max(n_list[:l]))
#     if max_max == index:
#         pass
#     else:
#         cnt+=1
#         n_list[index],n_list[max_max]=n_list[max_max],n_list[index]
#         list_list = []
#         for i in n_list:
#             list_list.append(i)
#         n_dict[cnt]=list_list
#         new_list.append(list_list)
#     index-=1
#     l-=1
# if k in n_dict:
#     print(*n_dict[k])
# else:
#     print(-1)

#선택?
# l=one()
# n_list = list(wow())
# m_list = list(wow())
# index = l-1
# if n_list == m_list:
#     print(1)
# else:
#     while l != 0:
#         max_max = n_list.index(max(n_list[:l]))
#         if max_max == index:
#             pass
#         else:
#             n_list[max_max],n_list[index]=n_list[index],n_list[max_max]
#         new_list = []
#         for i in n_list:
#             new_list.append(i)
#         if new_list == m_list:
#             print(1)
#             exit()
#         index-=1
#         l-=1
#     print(0)

l,k = wow()
n_list = list(wow())
m_list = sorted(n_list)
cnt = 0
i = 0
n_dict = {}
while n_list != m_list:
    a,b= (i)%l,(i+1)%l
    if n_list[a]>n_list[b]:
        cnt+=1
        n_dict[cnt] = [n_list[b],n_list[a]]
        n_list[a],n_list[b]=n_list[b],n_list[a]
    # print(n_list)
    i+=1
    if i == l-1:
        i=0
if k in n_dict:
    print(*n_dict[k])
else:
    print(-1)






