import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/17103
# n_dict = {}
# for i in range(2,1000001):
#     if i not in n_dict:
#         for a in range(i,1000001,i):
#             n_dict[a]=0
#         n_dict[i]=1
# for _ in range(one()):
#     num = one()
#     check = {}
#     cnt = 0
#     for i in range(num//2+1):
#         if i in n_dict:
#             if n_dict[i]:
#                 if num-i in n_dict:
#                     if n_dict[num-i]:
#                         cnt+=1
#     print(cnt)

#https://www.acmicpc.net/problem/17358
# n = one()-1
# cnt = 1
# for i in range(n,1,-2):
#     cnt*=i
# print(cnt%(10**9+7))

n,goal,r = wow()
n_list = [list(wow()) for _ in range(r)]
visited = [False]*r
mimi = [2**31]
def go(cnt,happy,list_list,visited,l,total):
    global n
    global goal
    for i in range(l):
        visit = [i for i in visited]
        count = cnt
        h = happy
        if not visit[i]:
            visit[i]=True
            like,level= list_list[i]
            h+=like
            total = max(total,level)
            count+=1
        print(count,total,visit,h)
        if count < n:
            go(count,h,list_list,visit,l,total)
        else:
            # print(total,count,n)
            if happy>=goal:
                mimi[0] = min(mimi[0],total)
go(0,0,n_list,visited,r,0)
print(mimi)
                














