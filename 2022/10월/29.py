import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/11582
# l = one()
# n_list = list(wow())
# r = one()
# for i in range(0,l,l//r):
#     n_list[i:i+l//r]=sorted(n_list[i:i+l//r])
# print(*n_list)

#https://www.acmicpc.net/problem/18110
# import decimal
# r = one()
# n_list = [one() for _ in range(r)]
# n_list.sort()
# remove = str(decimal.Decimal(r)*decimal.Decimal("0.15"))
# if int(remove[remove.index(".")+1])>=5:
#     remove=int(remove[:remove.index(".")])+1
# else:
#     remove=int(remove[:remove.index(".")])
# if remove != 0:
#     n_list = n_list[remove:-remove]
# if len(n_list) != 0 and sum(n_list) != 0:
#     number = str(decimal.Decimal(str(sum(n_list)))/decimal.Decimal(str(len(n_list))))
#     if "." in number:
#         answer = int(number[:number.index(".")])
#         check = int(number[number.index(".")+1])
#         # print(number,check)
#         if check >= 5:
#             answer+=1
#         print(answer)
#     else:
#         print(number)
# else:
#     print(0)

# https://www.acmicpc.net/problem/9291
# standard_list = {i for i in range(1,10)}
# for i in range(one()):
#     if i != 0:
#         inputing()
#     garo_list = {}
#     sero_list = {}
#     check = "yes"
#     for index in range(9):
#         n_list = list(wow())
#         if set(n_list) == standard_list:
#             garo_list[index]=n_list
#         else:
#             check ="no"
#             garo_list[index]=n_list
#         for ind in range(9):
#             if ind not in sero_list:
#                 sero_list[ind]=[n_list[ind]]
#             else:
#                 sero_list[ind]+=[n_list[ind]]
#     if check == "yes":
#         for a in range(9):
#             if set(sero_list[a]) != standard_list:
#                 check="no"
#     if check == "yes":
#         for row in range(0,9,3):
#             row_dict= {}
#             for garo in range(row,row+3):
#                 for rr in range(0,9,3):
#                     if rr not in row_dict:
#                         row_dict[rr]=garo_list[garo][rr:rr+3]
#                     else:
#                         row_dict[rr]+=garo_list[garo][rr:rr+3]
#             # print(row_dict)
#             for key in [0,3,6]:
#                 if set(row_dict[key])!=standard_list:
#                     check="no"
#     number = i+1
    
#     if check == "no":
#         print(f"Case {number}: INCORRECT")
#     else:
#         print(f"Case {number}: CORRECT")
















