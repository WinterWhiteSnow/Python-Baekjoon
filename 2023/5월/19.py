import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1812
# r=one()
# n_list=[one() for _ in range(r)]
# total = 0
# for i in range(r):
#     if i%2 == 0:
#         total+=n_list[i]
#     else:
#         total-=n_list[i]
# total//=2
# print(total)
# for i in range(r-1):
#     a = abs(total-n_list[i])
#     print(a)
#     total=a

#https://www.acmicpc.net/problem/25179
# n,k = wow()
# if n==k==1:
#     print("Can't win")
# else:
#     if (n-1)%(k+1) > k or (n-1)%(k+1) == 0:
#         print("Can't win")
#     else:
#         print("Can win")

#https://www.acmicpc.net/problem/20004
# n = one()
# for k in range(1,n+1):
#     if 30%(k+1) == 0 or 30%(k+1)>n:
#         print(k)

def check(a,b,*c):
    print(a,b)
    print(c)
check(1,2,10,70,80,80,90)















