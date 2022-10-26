import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/16969
# n_list = list(inputing())
# n_dict = {"d":10,"c":26}
# state = "none"
# cnt = 1
# for i in n_list:
#     if state == "none":
#         cnt*=n_dict[i]
#     else:
#         if state == i:
#             cnt*=(n_dict[i]-1)
#         else:
#             cnt*=n_dict[i]
#     state = i
#     cnt%=1000000009
# print(cnt)

#https://www.acmicpc.net/problem/25644
# l = one()
# n_list = list(wow())
# min_min = "none"
# max_max = "none"
# cnt = 0
# state = 0
# for i in n_list:
#     if min_min =="none":
#         min_min=i
#     else:
#         if i < min_min:
#             cnt = max(state,cnt)
#             min_min=i
#             max_max="none"
#         else:
#             if max_max == "none":
#                 max_max=i
#                 state = max(state,max_max-min_min)
#             else:
#                 if max_max < i:
#                     max_max=i
#                     state = max(state,max_max-min_min)
#     # print(min_min,max_max,state,cnt)
# cnt=max(cnt,state)
# # print(min_min,max_max,state,cnt)
# print(cnt)

l = one()
n_list = list(wow())
n_list.sort()
cnt = 0
while len(n_list) > 3:
    a = n_list.pop()
    b = n_list.pop()
    cnt+=a-b
    cnt+=a-n_list[-1]
    cnt+=b-n_list[-2]
    # print(a,b,cnt)
if len(n_list) == 3:
    cnt+=n_list[-1]-n_list[0]
    cnt+=n_list[-2]-n_list[0]
elif len(n_list)==2:
    cnt+=n_list[-1]-n_list[-2]
print(cnt)







