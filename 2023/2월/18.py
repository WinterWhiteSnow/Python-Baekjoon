import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/20055
# n,k = wow()
# n_list = list(wow())
# front = n_list[:n]
# back = n_list[n:][::-1]
# # print(front,back)
# front_vistied = [False]*n
# back_visited = [False]*n
# cnt = 0
# for i in front:
#     if i == 0:
#         cnt+=1
# for i in back:
#     if i == 0:
#         cnt+=1
# time = 0
# while cnt < k:
#     if front_vistied[-1]== True:
#         front_vistied[-1]=False
#     time+=1
#     front,back = [back[0]]+front[:-1],back[1:]+[front[-1]]
#     front_vistied,back_visited = [back_visited[0]]+front_vistied[:-1],back_visited[1:]+[front_vistied[-1]]
#     # print("start!!!",front,back)
#     # print(front_vistied,back_visited)
#     if front_vistied[-1]== True:
#         front_vistied[-1]=False
#     for i in range(n-2,-1,-1):
#         # print(i)
#         # print("now",i)
#         start = i
#         # while True:
#             # print("step!!",start)
#         if start+1 < n:
#             if front_vistied[start+1] == False and front[start+1] > 0:
#                 if front_vistied[start]==True:
#                     front_vistied[start]=False
#                     front_vistied[start+1]=True 
#                     front[start+1]-=1
#                     if front[start+1]==0:
#                         cnt+=1
#                     if front_vistied[-1] == True:
#                         front_vistied[-1]=False
#             #         else:
#             #             break
#             #     else:
#             #         break
#             # else:
#             #     break
#             start+=1
#     if front_vistied[-1]== True:
#         front_vistied[-1]=False
#         # front[-1]-=1
#         # if front[-1]<=0:
#         #     cnt+=1
#         #     front[-1]=0
        
#     if front[0]> 0 and front_vistied[0] == False:
#         front_vistied[0]=True
#         front[0]-=1
#         if front[0]==0:
#             cnt+=1
#     # print("end!!!",front,back)
#     # print(front_vistied,back_visited)
#     # print("time!!!",time,"cnt!!",cnt)
#     if cnt == k:
#         break
# print(time)












