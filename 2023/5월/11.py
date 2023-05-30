import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/17291
# n_list = [0]*21
# n_list[1]=1
# n_list[2]=2
# n_list[3]=4
# n_list[4]=7
# for i in range(5,21):
#     n_list[i]=n_list[i-1]+n_list[i-2]+n_list[i-3]
#     if i%2:
#         n_list[i]+=n_list[i-4]
# print(n_list[one()])

new_list = []
def check(n_list,n):
    if sum(n_list) == n:
        if sorted(n_list) not in new_list:
            new_list.append(sorted(n_list))
        return
    if sum(n_list) < n:
        for i in range(1,n+1):
            if i not in n_list:
                check(n_list+[i],n)
for num in range(1,21):
    check([0],num)
    print(num,len(new_list))
    new_list = []
















