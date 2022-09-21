import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#14683

# a,b = wow()
# x,y = wow()
# s = one()
# gap = abs(x-a)+abs(y-b)
# if gap <= s and s%2 == gap%2:
#     print("Y")
# else:
#     print("N")

# r = one()
# cnt = 0
# for _ in range(r):
#     n_list = list(wow())
#     max_max = max(n_list)
#     cnt = max(cnt,cnt+max_max)
# print(cnt)

# import string
# cnt = 0
# str_str = list(string.ascii_uppercase)
# index = 0
# count = 0
# n_list = [inputing() for _ in range(one())]
# n_list.sort()
# for i in n_list:
#     a = i
#     if a[0] == str_str[index]:
#         index+=1
#         index%=26
#         count+=1
#     else:
#         cnt = max(cnt,count)
# cnt = max(cnt,count)
# print(cnt)

#23397
# goal,time,r = wow()
# if r != 0:
#     n_list = sorted([one() for _ in range(r)])
#     max_max = n_list[0]
#     n_list.append(time)
#     for i in range(1,r+1):
#         a = n_list[i]
#         b = n_list[i-1]
#         max_max = max(max_max,a-b)
#     print("Y" if max_max >=goal else "N")
# else:
#     print("Y" if goal <= time else "N")

#24871    
# import string
# d,m,w = wow()
# day,month,year = wow()
# str_str = list(string.ascii_lowercase)[:w]
# total = (d*m*(year-1)+d*(month-1)+(day))%w
# print(str_str[total-1])
    
for index in range(1,one()+1):
    a,b = wow()
    c = a-1
    print(f"Case {index}:",b-min(b,c))
    
    
    
    
    
    
    
    
    