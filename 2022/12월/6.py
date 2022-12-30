import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1965
# l = one()
# n_list = list(wow())
# m_list = []
# max_max = 0
# for i in n_list:
#     if len(m_list) == 0:
#         m_list.append(i)
#     else:
#         if m_list[-1] < i:
#             m_list.append(i)
#         else:
#             start = 0
#             end = len(m_list)-1
#             if start == end:
#                 m_list[start]=i
#             else:
#                 while start<=end:
#                     mid = (start+end)//2
#                     num = m_list[mid]
#                     if num<i:
#                         end=mid-1
#                     else:
#                         start=mid+1
#                 if end < 0:
#                     end+=len(m_list)
#                 # print(i,start,end)
#                 for index in range(end,-1,-1):
#                     if m_list[index]>=i:
#                         end=index
#                     else:
#                         break
#                 # print("end!!!",end)
#                 if m_list[end] >= i:
#                     m_list[end]=i
#                 else:
#                     m_list.append(i)
#     # print(i,m_list)
# print(len(m_list))


https://www.acmicpc.net/problem/11060
l = int(input())
nlist = list(map(int,input().split()))
index=0
cnt=0
while index < l-1:
    cnt+=1
    maxmax=0
    move = "none"
    if nlist[index]==0:
        break
    for i in range(1,nlist[index]+1):
        print(i,index)
        if maxmax>=nlist[i+index]:
            print(maxmax,nlist[i+index])
            move = i+index
            maxmax= nlist[i+index]
    if move=="none" or maxmax==0:
        break
    index+=move
print(cnt if index >= l-1 else -1)
        




















