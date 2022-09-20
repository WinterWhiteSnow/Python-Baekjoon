import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# n_list = [one() for _ in range(one())]
# n_dict = {}
# for i in list(set(n_list)):
#     n_dict[i]=n_list.count(i)

# list_list = sorted(list(n_dict.items()),key=lambda x : x[0])
# list_list.sort(key=lambda x : x[1],reverse=True)
# print(list_list[0][0])

# a,b = wow()
# n_list = [one() for _ in range(a)]
# for _ in range(b):
#     x,y = wow()
#     print(sum(n_list[x-1:y]))

# while True:
#     a = one()
#     if a == 0:
#         break
#     count = 0
#     index = 1
#     total = 0
#     for _ in range(a):
#         if count <= index:
#             total+=index
#             count+=1
#             if count == index:
#                 index+=1
#                 count=0
#     print(a,total)

# for _ in range(one()):
#     a = inputing()
#     str_str = ""
#     now = "none"
#     repeat = 1
#     for aa in list(a):
#         if now == "none":
#             now = aa
#         else:
#             if now == aa:
#                 repeat+=1
#             else:
#                 str_str+=str(repeat)+now
#                 repeat=1
#                 now = aa
#     if now != "none":
#         str_str+=str(repeat)+now
#     print(str_str)

# while True:
#     a = one()
#     if a == 0:
#         break
#     n_list = sorted([one() for _ in range(a)])
#     # min_min = min(n_list)
#     # if n_list.count(min_min) >= 2:
#     #     n_list = n_list[1:]
#     # max_max = max(n_list)
#     # if n_list.count(max_max)>=2:
#     #     n_list = n_list[:-1]
#     n_list = n_list[1:-1]
#     print(int(sum(n_list)/len(n_list)))
# cnt = 0
# for _ in range(one()):
#     a = inputing()
#     if "CD" not in a:
#         cnt+=1
# print(cnt)
# while True:
#     odd= 0 #Cheryl
#     even = 0 #tania
#     a = inputing()
#     if a == "#":
#         break
#     a = a.split()
#     for i in a[:-1]:
#         if i == "A":
#             odd+=1
#         else:
#             i = int(i)
#             if i%2:
#                 odd+=1
#             else:
#                 even+=1
#     if odd == even:
#         print("Draw")
#     else:
#         if odd > even:
#             print("Cheryl")
#         else:
#             print("Tania")

# while True:
#     Joe, Jean, Jane,James,x=0,0,0,0,0
#     a = inputing()
#     if a == "0":
#         break
#     else:
#         for _ in range(int(a)):
#             b = inputing()
#             if b == "M" or b=="L":
#                 Joe+=1
#             elif b == "S":
#                 James+=1
#             else:
#                 if b =="X":
#                     x+=1
#                 else:
#                     b = int(b)
#                     if b >= 12:
#                         Jean+=1
#                     else:
#                         Jane+=1
#     print(Joe,Jean,Jane,James,x)

# l = one()
# a = inputing()
# n_dict = {}
# for i in list(set(list(a))):
#     n_dict[i]=a.count(i)
# list_list = sorted(list(n_dict.items()),key= lambda x : x[0])
# list_list.sort(key=lambda x : x[1],reverse=True)
# print(*list_list[0])    
from itertools import combinations
n,k = wow()
n_list = list(wow())
list_list = list(combinations(n_list,r=2))
list_list = [i for i in list_list if sum(i)==k]
print(len(list_list))
    













