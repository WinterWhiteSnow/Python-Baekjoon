import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# import datetime

# a = datetime.datetime(year=2023,month=4,day=29,hour=13)
# b = datetime.datetime.now()
# print(b-a)

#https://www.acmicpc.net/problem/17087
# import math
# l,x = wow()
# n_list = sorted(list(wow()))
# gap_list = []
# for n in n_list:
#     gap_list.append(abs(n-x))
# while len(gap_list)>=2:
#     a,b = gap_list.pop(),gap_list.pop()
#     gap_list.append(math.gcd(a,b))
# print(gap_list[0])
















