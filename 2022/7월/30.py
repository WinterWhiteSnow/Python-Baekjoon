import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# n = [i for i in range(1,one()+1)]
# n_list = sorted(list(wow()))
# if n == n_list:
#     print("TAK")
# else:
#     print("NIE")

# l = one()
# n_list = list(wow())
# index = 1
# for i in n_list:
#     if i == index:
#         index+=1
# print(l-index+1)
# from itertools import product,permutations
# l = one()
# n_list = inputing().replace(" ","")
# list_list = [i for i in range(3)]
# list_list = list(permutations(list_list,r=3))
# aa = "no"
# for i in list_list:
#     str_str = ""
#     for ii in i:
#         str_str+=str(ii)
#     if str_str in n_list:
#         aa = "yes"
# if aa =="yes":
#     print("TAK")
# else:
#     print("NIE")

# n_dict = {}
# for _ in range(one()):
#     a,b = wow()
#     if b not in n_dict:
#         n_dict[b]=a
# print(len(list(n_dict.keys())))

while True: