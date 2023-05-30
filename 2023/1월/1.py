import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/2520
# r = one()
# for _ in range(r):
#     inputing()
#     a,b,c,d,e= wow()
#     x,y,z,v = wow()
#     cnt = int(min(a*(16/8),b*(16/8),c*(16/4),d*(16/1),e*(16/9)))
#     count = x+y//30+z//25+v//10
#     print(min(cnt,count))

l,k = wow()
n_list = list(wow())
zero_list = []
n_dict = {}
for i in n_list:
    if i not in n_dict:
        n_dict[i]=














