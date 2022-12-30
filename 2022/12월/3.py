import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1474
import math
import string
str_str = list(string.ascii_uppercase)+["_"]+list(string.ascii_lowercase)
r,l = wow()
cnt = 0
n_list = []
for _ in range(r):
    b = inputing()
    cnt+=len(b)
    n_list.append(b)
# print(n_list)
plus = l-cnt
under_list = []
while plus != 0:
    r-=1
    index = math.ceil(plus/r)
    plus-=index
    under_list.append("_"*index)
under_list.sort()
# print(under_list)
answer = ""
ind = str_str.index("_")
for i in range(len(n_list)):
    list_list = n_list[i]
    if i == 0:
        answer+=list_list
    else:
        index = str_str.index(list_list[0])
        if index < ind:
            front = under_list[0]
            under_list=under_list[1:]
        else:
            front = under_list.pop()
        answer+=front+list_list
print(answer)































