import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# a = inputing()
# l = len(a)//3
# a_list = []
# for i in range(3):
#     a_list.append(a[l*i:l*i+l])
# set_list = list(set(a_list))
# print(set_list[0] if a.count(set_list[0])>=2 else set_list[1])

# for _ in range(one()):
#     start = list(inputing())
#     s_dict = {}
#     for i in set(start):
#         s_dict[i]=start.count(i)
#     for _ in range(one()):
#         a = list(inputing())
#         check = "yes"
#         for s in set(a):
#             if s in s_dict:
#                 # print(s,a.count(s),s_dict[s])
#                 if a.count(s)>s_dict[s]:
#                     check = "no"
#             else:
#                 check ="no"
#         print("YES" if check == "yes" else "NO")
# import math
# import decimal
# for _ in range(one()):
#     a,b,c = inputing().split()
#     d = (decimal.Decimal("90")-(decimal.Decimal(a)*decimal.Decimal("0.15")+decimal.Decimal(b)*decimal.Decimal("0.2")+decimal.Decimal(c)*decimal.Decimal("0.25")))/decimal.Decimal("0.4")
#     print(math.ceil(d) if d<=100 else "impossible")

a = list(inputing())
b = set(a)
n_dict = {}
for i in b:
    n_dict[i]=a.count(i)
n_list = sorted(list(n_dict.items()),key= lambda x : x[1],reverse=True)
cnt = 0
for a,b in n_list[2:]:
    cnt+=b
print(cnt)
