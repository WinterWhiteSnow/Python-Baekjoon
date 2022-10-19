import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/10709
# r,l= wow()
# n_list = [list(inputing()) for _ in range(r)]
# new_list = [[0]*l for _ in range(r)]
# for r_index in range(r):
#     check = "no"
#     index ="none"
#     for l_index in range(l):
#         if check == "no":
#             if n_list[r_index][l_index]=="c":
#                 check="yes"
#                 index = 0
#                 new_list[r_index][l_index]=index
#             else:
#                 new_list[r_index][l_index]=-1
#         else:
#             if n_list[r_index][l_index]=="c":
#                 index = 0
#             else:
#                 index+=1
#             new_list[r_index][l_index]=index
# for i in new_list:
#     print(*i)
                
#https://www.acmicpc.net/problem/14582
# n_list = list(wow())
# m_list = list(wow())
# str_str = ""
# n_cnt = 0
# m_cnt = 0
# for a,b in zip(n_list,m_list):
#     n_cnt+=a
#     if n_cnt > m_cnt:
#         str_str += "n"
#     else:
#         str_str += "m"
#     m_cnt+=b
#     if n_cnt > m_cnt:
#         str_str += "n"
#     else:
#         str_str += "m"

# new_str = ""
# for i in str_str:
#     if len(new_str) == 0:
#         new_str+=i
#     else:
#         if new_str[-1] != i:
#             new_str+=i
# print("Yes" if new_str[-2:] == "nm" else "No")

#https://www.acmicpc.net/problem/11971
# r,rr = wow()
# n_list = []
# for _ in range(r):
#     a,b = wow()
#     n_list.extend([b]*a)
# state = 0
# gap = 0
# for _ in range(rr):
#     a,b = wow()
#     start = state
#     state+=a
#     min_min = min(n_list[start:state])
#     gap = max(gap,b-min_min)
# print(gap)


# https://www.acmicpc.net/problem/12760
# r,l = wow()
# n_list = [sorted(list(wow())) for _ in range(r)]
# n_dict = {}
# for i in range(r):
#     n_dict[i]=0
# for i in range(l):
#     new_list = [n_list[a][i]for a in range(r)]
#     max_max = max(new_list)
#     for ii in range(r):
#         if new_list[ii]==max_max:
#             n_dict[ii]+=1
# max_value = max(n_dict.values())
# list_list = [a+1 for a,b in n_dict.items() if b == max_value]
# print(*list_list)







