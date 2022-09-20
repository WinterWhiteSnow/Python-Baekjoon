
import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#57

# order = list(inputing())
# n_list = [1,0,0,2]
# for i in order:
#     if i == "A":
#         n_list[0],n_list[1] = n_list[1],n_list[0]
#     if i == "B":
#         n_list[0],n_list[2] = n_list[2],n_list[0]
#     if i == "C":
#         n_list[0],n_list[3] = n_list[3],n_list[0]
#     if i == "D":
#         n_list[1],n_list[2] = n_list[2],n_list[1]
#     if i == "E":
#         n_list[1],n_list[3] = n_list[3],n_list[1]
#     if i == "F":
#         n_list[2],n_list[3] = n_list[3],n_list[2]
# print(n_list.index(1)+1)
# print(n_list.index(2)+1)

# a,b = wow()
# x = a//b
# y = a%b
# if y >= 0:
#     print(x)
#     print(y)
# else:
#     # print("no",x,y)
#     x+=1
#     y=a-x*b
#     print(x)
#     print(y)
# import decimal
# a,b,c = wow()
# x = str(a*b)
# c = str(c)
# print(decimal.Decimal(x)/decimal.Decimal(c))

# for _ in range(one()):
#     l,r = wow()
#     n_dict = {}
#     for _ in range(r):
#         list_list = list(wow())
#         for i in range(1,l+1):
#             if i not in n_dict:
#                 n_dict[i]=list_list[i-1]
#             else:n_dict[i]+=list_list[i-1]
#     new_list = sorted(list(n_dict.items()), key= lambda x : x[1],reverse=True)
#     print(new_list[0][0])

# n_dict = {}
# for i in range(one()):
#     n_dict[i]=one()
# list_list = sorted(list(n_dict.items()),key= lambda x : x[0])
# list_list = sorted(list_list,key= lambda x : x[1],reverse=True)
# print("S" if list_list[0][0] == 0 else "N")

# n_list = set([one() for _ in range(one())])
# a_list = set([i for i in range(1,max(n_list)+1)])
# new_list = sorted(list(a_list-n_list))
# if new_list:
#     for i in new_list:
#         print(i)
# else:
#     print("good job")
# l = one()
# str_str = inputing()
# two = str_str.count("2")
# ee = str_str.count("e")
# if two == ee:
#     print("yee")
# else:
#     if two>ee:
#         print("2")
#     else:
#         print("e")

# import datetime
# for _ in range(one()):
#     y,m = wow()
#     mm = str(m).zfill(2)
#     now = datetime.datetime.strptime(f"{y}{mm}{mm}","%Y%m%d")
#     answer = str(now-datetime.timedelta(m))[:10+1]
#     new_list = [i.lstrip("0") for i in answer.split("-")]
#     print(*new_list)
import string
s_list = list(string.ascii_uppercase)
print(s_list)


