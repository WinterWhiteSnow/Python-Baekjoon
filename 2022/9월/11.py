import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# l = one()
# n_list = list(wow())
# nn_list = [n_list[0]]
# a_list = list(wow())
# aa_list = [a_list[0]]
# for nn,aa in zip(n_list[1:],a_list[1:]):
#     nn_list.append(nn_list[-1]+nn)
#     aa_list.append(aa_list[-1]+aa)
# cnt = "none"
# for index in range(l):
#     if nn_list[index] == aa_list[index]:
#         cnt=index
# print(0 if cnt == "none" else cnt+1)

# for _ in range(one()):
#     index,k,a =wow()
#     n_list = []
#     while a != 0:
#         n_list.append(str(a%k))
#         a//=k
#     cnt = 0
#     for i in n_list:
#         cnt+=int(i)**2
#     print(index,cnt)
# index = 1
# for _ in range(one()):
#     r,l = wow()
#     n_list = inputing()
#     n_dict = {}
#     for _ in range(r):
#         a_list = inputing()
#         for ll in range(l):
#             if ll not in n_dict:
#                 n_dict[ll]=[a_list[ll]]
#             else:
#                 n_dict[ll]+=[a_list[ll]]
#     cnt = 0
#     for i in range(l):
#         if n_list[i] in n_dict[i]:
#             pass
#         else:
#             cnt+=1
#     if index != 1:
#         print()
#     print(f"Data Set {index}:")
#     print(f"{cnt}/{l}")
#     index+=1


            
            
            
            
            