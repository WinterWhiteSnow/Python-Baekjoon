
import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())
    

# import math
# while True:
#     a,b,c,d=  wow()
#     if a==b==c==d==0:
#         break
#     f = math.ceil((b*c-a)/d)
#     print(f if f>=0 else 0)

# h,m = wow()
# total = 3600*h+60*m
# total -=600
# wait = one()
# hh,mm = wow()
# person = one()+1
# unpack = one()
# total2 = 60*(wait+mm+person*unpack)+hh*3600
# time = (total-total2)%86400
# hour = time//3600
# minute =(time%3600)//60
# print(f"{hour:0>2} {minute:0>2}") 

# from itertools import combinations
# n_list = list(wow())
# total = sum(n_list)
# gap = total
# for i in range(1,4):
#     list_list = list(combinations(n_list,r=i))
#     for index in list_list:
#         gap = min(abs(total-sum(index)*2),gap)
# print(gap)

# a,b,c,d,e = wow()
# x = max(a,c)
# y = min(b,d)
# list_list = [i for i in range(x,y+1)]
# if e in list_list:
#     print(len(list_list)-1)
# else:
#     print(len(list_list))

# n_list = sorted(list(wow()))
# a,b,c = n_list[0],n_list[1],n_list[2]
# print(max(a+b*c,a-b*c,a+b-c,a-b+c,a*b-c,a*b+c))

# n,k= wow()
# gap = k-1
# gap_total = n-k
# min_min = gap_total//gap
# gap_gap = gap_total%gap
# n_list = [min_min]*gap
# for i in range(gap_gap):
#     n_list[i]+=1
# print(n_list.count(min(n_list)))

# while True:
#     a,b = wow()
#     if a==b==0:
#         break
#     if a+b == 13:
#         print("Never speak again.")
#     else:
#         if a>b :
#             print("To the convention.")
#         elif a==b:
#             print("Undecided.")
#         else:
#             print("Left beehind.")

# for _ in range(one()):
#     a,b,c = wow()
#     if a+b == c or a-b == c or a/b == c or a*b == c or b/a ==c or b-a ==c:
#         print("Possible")
#     else:
#         print("Impossible")

# a,b,c = wow()
# costs = a*3+b*2+c*1
# if costs >= 8:
#     x = "Province"
# elif 8>costs>=5:
#     x = "Duchy"
# elif 5>costs>=2:
#     x = "Estate"
# else:
#     x="none"
    
# if costs>=6:
#     y = "Gold"
# elif 6>costs>=3:
#     y ="Silver"
# else:
#     y = "Copper"

# if x != "none":
#     print(f"{x} or {y}")
# else:
#     print(y)

# a,b,c = wow()
# cnt = 0
# count=0
# while True:
#     if cnt < c:
#         cnt+=a
#         count+=1
#         if cnt >= c:
#             break
#     cnt-=b
# print(count)

# n_list = []
# a,b,c,total = wow()
# for x in range(total//a+1):
#     for y in range(total//b+1):
#         for z in range(total//c+1):
#             if a*x+b*y+c*z == total:
#                 n_list.append([x,y,z])
# if n_list:
#     for i in n_list:
#         print(*i)
# else:
#     print("impossible")
# now = 1
# for _ in range(one()):
#     a,symbol,b = inputing().split()
#     if symbol == "+":
#         now = (int(a)+int(b))-now
#     elif symbol == "-":
#         now = now*(int(a)-int(b))
#     elif symbol == "/":
#         a = int(a)
#         if a%2:
#             a+=1
#         now = int(a)//2
#     else:
#         now = (int(a)*int(b))**2
#     print(now)

x,y = wow()
for _ in range(one()):
    















