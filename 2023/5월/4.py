import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/21317
# r = one()
# n_list = [list(wow()) for _ in range(r-1)]
# long = one()
# count = 100000000000001
# # print(n_list)
# def check(index,cnt,state):
#     global r,count,long
#     if index >= r-1:
#         if index == r-1:
#             count = min(count,cnt)
#         return
#     if count <cnt:
#         return
#     # print("start!",index)
#     small,big = n_list[index]
#     index1 = index+1
#     index2 = index+2
#     index3 = index+3
#     # print(index,small,big)
#     if index1<=r:
#         check(index1,cnt+small,state)
#     if index2 <= r:
#         check(index2,cnt+big,state)
#     if index3<=r:
#         if state == 1:
#             check(index3,cnt+long,0)
# check(0,0,1)
# print(count)

# r= one()
# n_list = [list(wow()) for _ in range(r-1)]
# total = [[1000000001,1000000001] for _ in range(r+1)] 
# total[1][0]=0
# total[1][1]=0
# loong = one()
# for i in range(2,r+1):
#     if i>=2:
#         total[i][0]=min(total[i-1][0]+n_list[i-2][0],total[i][0])
#         total[i][1]=min(total[i-1][1]+n_list[i-2][0],total[i][1])
#     if i>=3:
#         total[i][0]=min(total[i-2][0]+n_list[i-3][1],total[i][0])
#         total[i][1]=min(total[i-2][1]+n_list[i-3][1],total[i][1])
#     if i>= 4:
#         total[i][1]=min(total[i-3][0]+loong,total[i-2][1]+n_list[i-3][1],total[i-1][1]+n_list[i-2][0])
#     # print(i)
#     # print(total)
# print(min(total[-1]))











