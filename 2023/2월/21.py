import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/14890
# n,k = wow()
# n_list = [list(wow()) for _ in range(n)]
# n_dict = {}
# for i in range(n):
#     list_list = n_list[i]
#     for ii in range(n):
#         if ii not in n_dict:
#             n_dict[ii]=[list_list[ii]]
#         else:
#             n_dict[ii]+=[list_list[ii]]
# list_list =  list(n_dict.values())


# def check(m_list):
#     global n,k
#     # print("start!!!!",m_list)
#     visited = [False]*n
#     index = 0
#     state = "none"
#     for i in range(len(m_list)):
#         if index >i:
#             continue
#         if state == "none":
#             state = m_list[i]
#             index =i
#         else:
#             if state == m_list[i]:
#                 index=i
#                 continue
#             # print("else",index,state,m_list[i],i)
#             if abs(state-m_list[i]) == 1:
#                 if state > m_list[i]: #내려가는 경사로
#                     cnt = 0
#                     for a in range(i,min(i+k,n)):
#                         if abs(state-m_list[a])==1:
#                             if visited[a] == False:
#                                 cnt+=1
#                                 visited[a]=True
#                             else:
#                                 break
#                     if cnt == k:
#                         index=i+k-1
#                         state = m_list[i]
#                     else:
#                         break    
#                 else: #올라가는 경사로
#                     cnt = 0
#                     for a in range(index,max(index-k,-1),-1):
#                         if state==m_list[a] and m_list[i]-m_list[a] == 1:
#                             if visited[a] == False:
#                                 cnt+=1
#                                 visited[a]=True
#                             else:
#                                 break
#                     if cnt == k:
#                         index=i
#                         state = m_list[i]
#                     else:
#                         break 
#             else:
#                 break   
#     #     print(index,state)
#     # print("end!!!",index,state)
#     if index == n-1:
#         return True
#     else:
#         return False
# count = 0
# for i in range(n):
#     a = n_list[i]
#     b = n_list[i][::-1]
#     c = list_list[i]
#     d = list_list[i][::-1]
#     front = [a,b]
#     back = [c,d]
#     total = []
#     front_check = "no"
#     back_check = "no"
#     for ebs in front:
#         if check(ebs):
#             # print("front",i,ebs)
#             front_check = "yes"
#     for ebs in back:
#         if check(ebs):
#             # print("back",i,ebs)
#             back_check = "yes"
#     if front_check == "yes":
#         count+=1
#     if back_check == "yes":
#         count+=1
# # check([2,2,3,3,2,2])
# # check([1, 1, 1, 3, 3, 1])
# # check([3, 4, 3, 3, 3, 3, 3])
# print(count)
        









