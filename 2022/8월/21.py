import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# for _ in range(one()):
#     a,b = wow()
#     if (a<=1 and b<=2) or (a<=2 and b<=1):
#         print("Yes")
#     else:
#         print("No")

# for _ in range(one()):
#     n_list = list(wow())
#     n = n_list[0]
#     n_list = n_list[1:]
#     total = sum(n_list)
#     if n**2 == total:
#         print("no")
#     else:
#         print("yes")

# for _ in range(one()):
#     q,w,e = inputing().split()
#     a,b,c = map(int,q.split(":"))
#     x,y,z = map(int,w.split(":"))
#     start_time = a*3600+b*60+c
#     end_time = x*3600+y*60+z
#     if end_time<=start_time:
#         end_time+=3600*24
#     solve_time = (start_time+60*int(e))
#     if end_time>=solve_time:
#         print("Perfect")
#     elif end_time+3600>=solve_time:
#         print("Test")
#     else: print("Fail")

# for _ in range(one()):
#     a,b,c = wow()
#     if c%2 == 0:
#         print("YES" if a+2*b>=c else "NO")
#     else:
#         print("YES" if a+2*b>=c and a>=1 else "NO")
# for i in sys.stdin.readlines():
#     a,b = map(float,i.split())
#     answer = round(((a*(b+0.16))/0.067)**(1/2))
#     print(answer)
# import decimal
# cnt = 0
# for i in sys.stdin.readlines():
#     cnt+=decimal.Decimal(i)
# print(cnt)




