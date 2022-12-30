import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/2422
import itertools
n,r = wow()
n_list = [i for i in range(1,n+1)]
n_list = list(itertools.combinations(n_list,r=3))
n_dict = {}
for _ in range(r):
    a,b = sorted(wow())
    if a not in n_dict:
        n_dict[a]=[b]
    else:
        n_dict[a]+=[b]
cnt=0
for i in n_list:
    a,b,c = i
    if a in n_dict:
        if b in n_dict[a] or c in n_dict[a]:
            continue
    if b in n_dict:
        if c in n_dict[b]:
            continue
    cnt+=1
    # print(i,cnt)
print(cnt)
            


        












