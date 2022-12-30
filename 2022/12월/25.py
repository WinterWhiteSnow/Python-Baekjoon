import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())


#https://www.acmicpc.net/problem/16198
# l = one()
# n_list = list(wow())
# total = []
# def go(index,list_list,cnt):
#     # print("start",list_list,index)
#     a,b = list_list[index-1],list_list[index+1]
#     temp_list = [i for i in list_list]
#     del temp_list[index]
#     cnt+=a*b
#     if len(temp_list)>=3:
#         for i in range(1,len(temp_list)-1):
#             go(i,temp_list,cnt)
#     else:
#         total.append(cnt)
# for i in range(1,l-1):
#     go(i,n_list,0)
# print(max(total))

#https://www.acmicpc.net/problem/14620
# n_list = [list(wow()) for _ in range(one())]
# total = [3000]
# def go(y,x,list_list,cnt,count,l,cnt_list):
#     cnt_list = [i for i in cnt_list]
#     temp_list = []
#     for a in list_list:
#         new_list = []
#         for b in a:
#             new_list.append(b)
#         temp_list.append(new_list)
#     # print("start")
#     # for i in temp_list:
#     #     print(*i)
#     garo = temp_list[y][x-1:x+2]
#     sero = [temp_list[y-1][x],temp_list[y][x],temp_list[y+1][x]]
#     # print(garo,sero)
#     if "X" in garo or "X" in sero:
#         pass
#     else:
#         cnt+=sum(garo)+sero[0]+sero[-1]
#         cnt_list.append(sum(garo)+sum(sero))
#         temp_list[y][x-1:x+2]=["X"]*3
#         for i in range(y-1,y+2):
#             temp_list[i][x]="X"
#         count+=1
#         # print("wow",cnt,count)
#         # for i in temp_list:
#         #     print(*i)
#         if count == 3:
#             # if cnt < total[0]:
#                 # print(cnt,cnt_list)
#                 # for i in temp_list:
#                 #     print(*i)
#             total[0]=min(total[0],cnt)
#         else:
#             for y in range(1,l-1):
#                 for x in range(1,l-1):
#                     go(y,x,temp_list,cnt,count,l,cnt_list)
# l = len(n_list)
# for y in range(1,l-1):
#     for x in range(1,l-1):
#         go(y,x,n_list,0,0,l,[])
# print(total[0])

#https://www.acmicpc.net/problem/18429
# l,minus = wow()
# n_list = list(wow())
# state = 500
# total = [0]
# def go(state,index,minus,list_list):
#     temp_list = [i for i in list_list]
#     a = temp_list[index]
#     state-=minus
#     state+=a
#     del temp_list[index]
#     if state >= 500:
#         if len(temp_list)>=1:
#             for i in range(len(temp_list)):
#                 go(state,i,minus,temp_list)
#         else:
#             total[0]+=1    
# for i in range(l):
#     go(state,i,minus,n_list)
# print(total[0])










