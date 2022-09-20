import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# cnt = one()
# x = one()
# state = "two"
# count = 0
# for i in sys.stdin.readlines():
#     i = i.split()
#     if len(i) == 2:
#         a,b = map(int,i)
#         if abs(a-b) >x:
#             pass
#         else:
#             count+=max(a,b)
#     else:
#         count+=int(i[0])
# print(count)

# while True:
#     l = one()
#     if l==0:
#         break
#     n_list = list(wow())
#     average = sum(n_list)/l
#     cnt = [1 for i in n_list if i <= average]
#     print(sum(cnt))

# while True:
#     l = one()
#     if l == 0:
#         break
#     n_list = inputing().replace(" ","")
#     cnt = 0
#     for i in range(len(n_list)-3):
#         if n_list[i:i+4] == "2020":
#             cnt+=1
#     print(cnt)

# l = one()
# a = inputing()
# b = inputing()
# cnt = 0
# for x,y in zip(list(a),list(b)):
#     if x==y=="C":
#         cnt+=1
# print(cnt)

# l,ll = wow()
# l_list = inputing().split()
# ll_list = inputing().split()
# for _ in range(one()):
#     index = one()-1
#     print(l_list[index%l]+ll_list[index%ll])

        
















