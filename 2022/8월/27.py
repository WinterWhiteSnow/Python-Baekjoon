import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# for _ in range(one()):
#     n_list = list(wow())
#     nn_list = [n_list[1],n_list[2]]
#     for _ in range(n_list[0]-2):
#         nn_list.append(nn_list[-2]+nn_list[-1])
#     n_list =n_list[1:]
#     if n_list == nn_list:
#         print("YES")
#     else:
#         print("NO")
# import string
# for _ in range(one()):
#     s_list = list(string.ascii_lowercase)
#     l = one()
#     n_list = list(wow())
#     new_list = []
#     for index in n_list:
#         new_list.append(s_list[index])
#         a = [s_list[index]]
#         del s_list[index]
#         s_list=a+s_list
#     print(*new_list,sep="")

# a = inputing()
# b = inputing()
# cnt = 0
# for i in range(len(a)-len(b)+1):
#     count = 0
#     for x,y in zip(list(a[i:]),list(b)):
#         if x==y:
#             count+=1
#             break
#     if count == 0:
#         cnt+=1
# print(cnt)

# num = one()
# n_list = [1,1]
# while True:
#     n_list.append(n_list[-1]+n_list[-2])
#     if sum(n_list) >= num:
#         break
#     # print(n_list,n_list[-1],sum(n_list))
# print(len(n_list))

# for index in range(1,one()+1):
#     c = one()
#     l = one()
#     n_list = list(wow())
#     new_list = []
#     for a in range(l-1):
#         for b in range(a+1,l):
#             if n_list[a]+n_list[b] <= c:
#                 new_list.append([a+1,b+1,n_list[a]+n_list[b]])
#     new_list.sort(key=lambda x : x[2],reverse=True)
#     print(f"Case #{index}:",*new_list[0][:-1])

# l = one()
# n_list = list(inputing())
# for i in range(l-1):
#     if n_list[i+1] == "J":
#         print(n_list[i])

# import string
# str_str = list(string.ascii_uppercase)
# n_dict = {}
# a=["***","***","***","***","***"]
# b=["*.*","*.*","*..","*.*","*.."]
# c=["***","***","*..","*.*","***"]
# d=["*.*","*.*","*..","*.*","*.."]
# e=["*.*","***","***","***","***"]
# new_list = [a,b,c,d,e]
# l = one()
# a_list = list(inputing())
# b_list = [str_str.index(i) for i in a_list]
# for index in range(5):
#     list_list = new_list[index]
#     for l in b_list:
#         print(list_list[l],end="")
#     print()

while True:
    n_list = list(wow())
    if n_list[0] == 0:
        break
    l = n_list[0]
    n_list=n_list[1:]
    for i in range(1,1+l):
        if i == 1 :
            print((str(i)+" ")*n_list[i-1],end="")
        else:
            print((str(i)+" ")*(n_list[i-1]-n_list[i-2]),end="")
    print()





