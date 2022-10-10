import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# https://www.acmicpc.net/problem/25641
# l = one()
# n_list = list(inputing())[::-1]
# while n_list.count("s") != n_list.count("t"):
#     n_list.pop()
# print("".join(n_list)[::-1])

#https://www.acmicpc.net/problem/25630
# l = one()
# n_list = list(inputing())
# start = l//2
# cnt=0
# if l%2:
#     a = n_list[:start]
#     b = n_list[start+1:][::-1]
# else:
#     a = n_list[:start]
#     b = n_list[start:][::-1]
# for x,y in zip(a,b):
#     if x!=y:
#         cnt+=1
# print(cnt)

#https://www.acmicpc.net/problem/25642
# a,b = wow()
# state = 0
# while a < 5 and b < 5:
#     if state == 0:
#         b+=a
#     else:
#         a+=b
#     state+=1
#     state%=2
# print("yt" if a<5 else "yj")

#https://www.acmicpc.net/problem/13322
# a = inputing()
# # list_list = []
# # for i in range(len(a)):
# #     list_list.append(a[:i+1])
# # n_list = sorted(list_list)
# # print(list_list)
# # print(n_list)
# for i in range(len(a)):
#     print(i)

#https://www.acmicpc.net/problem/25177
# l,ll = wow()
# n_list = list(wow())
# m_list = list(wow())
# n_list+=[0]*(abs(l-ll))
# m_list+=[0]*(abs(ll-l))
# max_max = 0
# for x,y in zip(n_list,m_list):
#     if y>x:
#         max_max=max(max_max,y-x)
# print(max_max)

#https://www.acmicpc.net/problem/11726
#https://yabmoons.tistory.com/506
# n = one()
# n_list = [0,1,2]
# for i in range(n-3+1):
#     n_list.append(n_list[i+2]+n_list[i+1]%10007)
# print(n_list[n]%10007)

r = one()
n_list = [list(wow()) for _ in range(r)]
new_list = n_list[0]
for index in range(len(new_list)):
    state = index
    for i in range(r-1):
        x = (state+1)%len(new_list)
        y = state-1
        first = n_list[i+1][x]
        second = n_list[i+1][y]
        if first >= second:
            new_list[index]+=second
            state=y%len(new_list)
        else:
            new_list[index]+=first
            state=x
    print(new_list)
print(min(new_list))







