import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#35

# r,price = wow()
# total = 0
# balcony = 0
# bedroom = 0
# for _ in range(r):
#     a,b = inputing().split()
#     a = int(a)
#     total+=a
#     if b == "bedroom":
#         bedroom+=a
#     if b == "balcony":
#         balcony+=a
# print(total)
# print(bedroom)
# print((total-balcony+(balcony/2))*price)

# r,limit,x,y = wow()
# cnt = 0
# for _ in range(r):
#     a,b = wow()
#     gap = ((x-a)**2+(y-b)**2)**(1/2)
#     if gap > limit:
#         cnt+=1
# print(cnt)

# x,y = wow()
# gap = 10001
# now = []
# for _ in range(one()):
#     a,b = wow()
#     if abs(x-a)+abs(y-b) < gap:
#         now = [a,b]
#         gap = abs(x-a)+abs(y-b)
# print(*now)
for index in range(1,one()+1):
    l = one()
    n_list = list(wow())
    for i in range(1,len(n_list)-1):
        

