import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#19575 호너의 방법
# n,x = wow()
# n_list = [list(wow()) for _ in range(n+1)]
# cnt = n_list[0][0]*x+n_list[1][0]
# cnt%=(10**9+7)
# n_list = n_list[2:]
# for i in n_list:
#     cnt*=x
#     cnt+=i[0]
#     cnt%=(10**9+7)
# print(cnt)

#23886
# n_list = list(map(int,list(inputing())))
# state= "none"
# check = "yes"
# answer_list = []
# for i in range(1,len(n_list)):
#     if state == "none":
#         state = n_list[i]-n_list[i-1]
#         if state <0:
#             check="no"
#             break
#             # answer_list.append("-")
#         elif state > 0:
#             answer_list.append("+")
#         else:
#             check ="no"
#             break
#     else:
#         gap = n_list[i]-n_list[i-1]
#         if gap == 0:
#             check="no"
#             break
#         else:
#             if state == gap:
#                 pass
#             else:
#                 if state != 0 and gap !=0:
#                     if (state > 0 and gap >0) or (state<0 and gap<0):
#                         check="no"
#                         break
#                 else:
#                     check = "no"
#                     break
#             state = gap
#             if state <0:
#                 answer_list.append("-")
#             else:
#                 answer_list.append("+")
#     # print(check,answer_list)
# a_list = sorted(list(set(answer_list)))
# print("ALPSOO" if check == "yes" and a_list == ["+","-"] and answer_list[-1] == "-" else "NON ALPSOO")

#15722
# x,y = 0,0
# n = one()
# if n == 0:
#     print(0,0)
# else:
#     n_list = []
#     index = 1
#     d_list = [[0,1],[1,0],[0,-1],[-1,0]]
#     d_index = 0
#     while len(n_list)<n:
#         for _ in range(2):
#             for _ in range(index):
#                 x+=d_list[d_index][0]
#                 y+=d_list[d_index][1]
#                 n_list.append([x,y])
#             d_index+=1
#             d_index%=4
#         index+=1
#     print(*n_list[n-1])














