import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://school.programmers.co.kr/learn/courses/30/lessons/120956?language=python3
# def solution(babbling):
#     answer = 0
#     n_dict = {}
#     for str_str in babbling:
#         for i in ["aya", "ye", "woo", "ma" ]:
#             if i in str_str:
#                 str_str = str_str.replace(i,"x")
#         if set(list(str_str)) == {"x"}:
#             answer+=1
#     return answer

#https://www.acmicpc.net/problem/26082
# a,b,c = wow()
# x = (b//a)*3
# print(x*c)

import math
# n = one()
# print(6*n//math.gcd(6,n))
# my_string = inputing()

import collections

import string
answer = []
index=1
while len(answer)<=100:
    if index%3 == 0:
        index+=1
        continue
    answer.append(index)
    index+=1
    print(answer)
print(answer)
    










