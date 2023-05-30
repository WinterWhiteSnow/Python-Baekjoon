import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/25194
sys.setrecursionlimit(10**7)
l = one()
n_list = list(wow())
n_list = [i%7 for i in n_list if i%7 > 0]
l = len(n_list)
visit = [0]*l
def check(count,v):
    count%=7
    if count == 4:
        print("YES")
        exit()
    v = [i for i in v]
    for i in range(l):
        if v[i]==True:
            continue
        v[i]=True
        check(count+n_list[i],v)
        v[i]=False
check(0,visit)
print("NO")


















