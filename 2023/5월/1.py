import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/12026
# l = one()
# n_list = list(inputing())
# total = [10000000000000001]*(l)
# total[0]=0
# move = ["B","O","J"]
# for start in range(l):
#     now = n_list[start]
#     for end in range(start+1,l):
#         if now == "B":
#             if n_list[end] == "O":
#                 total[end] = min(total[end],total[start]+(end-start)**2)
#         if now == "O":
#             if n_list[end] == "J":
#                 total[end] = min(total[end],total[start]+(end-start)**2)
#         if now == "J":
#             if n_list[end] == "B":
#                 total[end] = min(total[end],total[start]+(end-start)**2)
# print(total[-1] if total[-1] != 10000000000000001 else  -1)

one = lambda : int(input())
wow = lambda : map(int,input().split())
answer_list = []
for t in range(one()):
    t = t+1
    a,b = wow()
    print(b%a,a%b)
        













