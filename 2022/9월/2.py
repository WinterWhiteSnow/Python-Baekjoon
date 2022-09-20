from re import L
import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# while True:
#     test = one()
#     if test < 0:
#         break   
#     n_list = []   
#     for _ in range(test):
#         a,b,c,d = inputing().split()
#         a,b,c = int(a),int(b),int(c)
#         n_list.append([d,a*b*c])
#     n_list.sort(key=lambda x : x[1])
#     a = n_list[-1][0]
#     b = n_list[0][0]
#     print(f"{a} took clay from {b}.")

# r = one()
# for i in range(r):
#     if i != 0:
#         print()
#     l = one()
#     n_list =list(wow())
#     m_list = list(wow())
#     d = 0
#     for a in range(l):
#         for b in range(l):
#             if b>=a and n_list[a]<=m_list[b]:
#                 d = max(d,b-a)
#     print(f"The maximum distance is {d}")

# for i in range(1,one()+1):
#     r,l = wow()
#     n_list = [one() for _ in range(r)]
#     cnt = 0
#     for _ in range(l):
#         a,b,c,d = wow()
#         cnt+=a*b*c*n_list[d-1]
#     print(f"Data Set {i}:")
#     print(cnt)

# for i in range(1,1+one()):
#     n_list = [list(wow()) for _ in range(one())]
#     gap_dict = {}
#     max_max = 0
#     for a in range(len(n_list)-1):
#         for b in range(a+1,len(n_list)):
#             x = n_list[a]
#             y = n_list[b]
#             gap = 0
#             for xx,yy in zip(x,y):
#                 gap+=(yy-xx)**2
#             if gap not in gap_dict:
#                 gap_dict[gap] = [[a+1,b+1]]
#             else:
#                 gap_dict[gap]+=[[a+1,b+1]]
#             max_max=max(max_max,gap)
#     print(f"Data Set {i}:")
#     for i in gap_dict[max_max]:
#         print(*i)

# n_list = [list(wow()) for _ in range(one())]
# gap_max = 0
# n_dict = {}
# for a in range(len(n_list)-1):
#     for b in range(a+1,len(n_list)):
#         x = n_list[a]
#         y = n_list[b]
#         gap = 0
#         for xx,yy in zip(x,y):
#             gap+=(yy-xx)**2
#         if gap not in n_dict:
#             n_dict[gap]=[[a+1,b+1]]
#         else:
#             n_dict[gap]+=[[a+1,b+1]]
#         gap_max= max(gap,gap_max)
# print(*n_dict[gap_max][0]) 

# r,y,b = wow()
# n_list = [one() for _ in range(6)]
# y-=n_list[0]+n_list[1]/2+n_list[-1]/2
# b-=n_list[1]/2+n_list[2]+n_list[3]/2
# r-=n_list[-2]+n_list[-1]/2+n_list[-3]/2
# if r>=0:
#     r= 0
# else:
#     r*=-1
# if y>=0:
#     y= 0
# else:
#     y*=-1
# if b>=0:
#     b= 0
# else:
#     b*=-1
# print(int(r) if int(r) == r else r,int(y) if int(y) == y else y,int(b) if int(b) == b else b)

# a = inputing()
# index = 0
# for i in range(len(a)):
#     if a[i] in "aeiou":
#         index=i
# print(a[:index+1]+"ntry")
# import math
# total = one()
# if total >= 28:
#     gap = (total-28)//7
#     gap+= 1 if (total-28)%7 >0 else 0
#     print(gap+7)
# else:
#     cnt = 0
#     index = 0
#     while cnt < total:
#         index+=1
#         cnt+=index
#     print(index)

# for _ in range(one()):
#     n_list = list(wow())
#     cnt = 0
#     for i in range(1,len(n_list)-1):
#         if n_list[i-1]*2<n_list[i]:
#             cnt+=n_list[i]-n_list[i-1]*2
#     print(cnt)

# for i in range(one()):
#     i = i+1
#     a,b = inputing().split()
#     b = list(map(int,list(b)))
#     gap=0
#     for index in range(1,int(a)+1):
#         gap=max(gap,index-sum(b[:index]))
#     print(f"Case #{i}: {gap}")
import math

for ind in range(1,1+one()):
    l,min_min,max_max = wow()
    n_list = list(wow())
    state = n_list[0]*n_list[1]//math.gcd(n_list[0],n_list[1])
    for i in range(2,l):
        state = state*n_list[]
    




