import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/3518
# n_dict= {}
# n_list = []
# for i in sys.stdin.readlines():
#     a = i.rstrip().split()
#     for i in range(len(a)):
#         if i not in n_dict:
#             n_dict[i]=[a[i]]
#         else:
#             n_dict[i]+=[a[i]]
#     n_list.append(a)
# a_dict = {}
# for key in n_dict.keys():
#     list_list = n_dict[key]
#     max_max = 0
#     for i in list_list:
#         max_max=max(max_max,len(i))
#     a_dict[key]=max_max

# # print(a_dict)
# for i in n_list:
#     list_list = i
#     for a in range(len(list_list)):
#         list_list[a]=list_list[a].ljust(a_dict[a]," ")
#     list_list[-1]=list_list[-1].rstrip()
#     print(*list_list)

#https://www.acmicpc.net/problem/11507
# n_list = inputing()
# n_dict = {}
# check = "yes"
# for i in range(len(n_list)//3):
#     str_str = n_list[3*i:3*i+3]
#     symbol = str_str[0]
#     number = int(str_str[1:])
#     if symbol not in n_dict:
#         n_dict[symbol]=[number]
#     else:
#         if number not in n_dict[symbol]:
#             n_dict[symbol]+=[number]
#         else:
#             check = "no"
#             break
# if check  =="no":
#     print("GRESKA")
# else:
#     for i in "P,K,H,T".split(","):
#         if i in n_dict:
#             print(13-len(n_dict[i]),end=" ")
#         else:
#             print(13,end=" ")
#     print()

n_dict = {}
number = int((4*(10**9))**(1/2))+1
for i in range(2,number):
    if i not in n_dict:
        for a in range(i,number,i):
            n_dict[a]=0
        n_dict[i]=1
list_list = [a for a,b in n_dict.items() if b == 1]
print(list_list)
    










