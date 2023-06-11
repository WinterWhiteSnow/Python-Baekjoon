import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# https://school.programmers.co.kr/learn/courses/30/lessons/42746#qna
# def solution(numbers):
#     numbers = [str(i) for i in numbers]
#     answer = ''
#     numbers.sort(reverse=True, key= lambda x: (x*4))
#     return str(int("".join(numbers)))

#https://www.acmicpc.net/problem/27522
# n_list = [10,8,6,5,4,3,2,1]
# m_list = []
# b = []
# r = []
# for _ in range(8):
#     x,y = inputing().split()
#     x = x.replace(":","")
#     m_list.append(x)
#     if y == "B":
#         b.append(x)
#     else:
#         r.append(x)
# m_list.sort()
# cnt1 = 0
# cnt2 = 0
# for bb in b:
#     cnt1+=n_list[m_list.index(bb)]
#     # print("why",cnt1,cnt2)
# for cc in r:
#     cnt2+=n_list[m_list.index(cc)]
# if cnt1 > cnt2:
#     print("Blue")
# else:
#     print("Red")


    











