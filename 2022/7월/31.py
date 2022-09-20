import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

n = one()
l = inputing()
for i in range(1,n+1):
    num = str(i)
    if l[0:len(num)] == num:
        l = l[len(num):]
    else:
        print(num)








