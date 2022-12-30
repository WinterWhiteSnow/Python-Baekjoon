import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1189
# r,l,k = wow()
# n_list = [list(inputing()) for _ in range(r)]
# total = [0]
# def go(list_list,y,x,r,l,k,cnt):
#     temp_list = []
#     for i in list_list:
#         b = []
#         for a in i:
#             b.append(a)
#         temp_list.append(b)
#     # print(cnt,"xy",y,x,cnt)
#     # for i in temp_list:
#     #     print(*i)
#     if 0<=y<=r-1 and 0<=x<=l-1:
#         if temp_list[y][x] == ".":
#             temp_list[y][x]="X"
#             cnt+=1
#             if y==0 and x==l-1 and cnt == k:
#                 total[0]+=1
#             else:
#                 go(temp_list,y-1,x,r,l,k,cnt)
#                 go(temp_list,y+1,x,r,l,k,cnt)
#                 go(temp_list,y,x+1,r,l,k,cnt)
#                 go(temp_list,y,x-1,r,l,k,cnt)
# go(n_list,r-1,0,r,l,k,0)                    
# print(total[0])

l = one()
n_list = list(wow())
n_dict = {}
def go(list_list,cnt):
    x,y = list_list.pop(),list_list.pop()
    if x-y > 0:
        

                


        




























