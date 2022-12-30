import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

https://www.acmicpc.net/problem/11060
l = one()
n_list = list(wow())
index = 0
cnt = 0
while index < l-1:
    cnt+=1
    if index+n_list[index]>=l-1:
        index+=n_list[index]
        break
    step = n_list[index+1:index+1+n_list[index]]
    move = 0
    index_index = 0
    for i in range(len(step)):
        if move <= step[i]+i:
            move = step[i]+i+1
            index_index=index+i+1
    if move == 0:
        break
    # print("move",move)
    # print("index",index_index)
    index=index_index
# print(cnt,index)
print(cnt if index >= l-1 else -1)

















