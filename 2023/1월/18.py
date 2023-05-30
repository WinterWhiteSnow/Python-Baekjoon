import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1459
# a,b,time1,time2 =wow()
# gap = min(a,b)
# total = time1*(a+b)
# cnt = 0
# state = 0
# cnt+=min((time2)*gap,(time1*2)*gap)
# gap = a+b-(2*gap)
# # print(gap)
# x = gap//2
# # print(x)
# cnt+=min(time1*2*x,time2*x*2)
# if gap%2:
#     cnt+=time1
# # cnt+=time1*gap
# print(min(cnt,total))

n = inputing()
a = n.count("a")
if a == 1:
    print(0)
else:
    n+=n[:a]
    # print(n)
    cnt = n[:a].count("b")
    # print("cnt",cnt)
    min_min = cnt
    for i in range(1,len(n)-a):
        y=n[i+a-1]
        print(i,i+a-1,n[i:i+a],y)
        xx= n[i-1]
        if xx == "b":
            cnt-=1
        # print(n[i:i+a])
        # cnt = max(cnt,0)
        if y == "b":
            cnt+=1
        min_min=min(min_min,cnt)
        # print(min_min)
    print(min_min)
        
    

















