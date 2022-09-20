import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# for index in range(1,one()+1):
#     l = one()
#     n_list = list(wow())
#     for i in range(1,l-1):
#         average = (n_list[i-1]+n_list[i+1])/2
#         n_list[i] = min(n_list[i],average)
#     answer = n_list[-2]
#     print(f"Case #{index}: {answer:.6f}")
# n_dict = {}
# l,order,goal = wow()
# n_list = list(wow())
# n_dict[1] = 1
# state = 1
# for i in n_list:
#     if i == 1:
#         state +=1
#         if state > l:
#             state -=l
#         if state not in n_dict:
#             n_dict[state]=1
#         else:
#             n_dict[state]+=1
#     else:
#         state -=1
#         if state <= 0:
#             state = l
#         if state not in n_dict:
#             n_dict[state]=1
#         else:
#             n_dict[state]+=1
#     # print(i,state)
# print(n_dict[goal] if goal in n_dict else 0)

# time = one()
# a,b = wow()
# x,y = wow()
# cnt = 0
# count = (time-x)*y
# if a+x <time:
#     count+=(time-x-a)*b
# cnt = max(cnt,count)
# count = (time-a)*b
# if a+x <time:
#     count+=(time-x-a)*y 
# cnt = max(cnt,count)  
# print(cnt)

# n,a,b = wow()
# s = list(inputing())
# s[a-1:b]=s[a-1:b][::-1]
# print("".join(s))






