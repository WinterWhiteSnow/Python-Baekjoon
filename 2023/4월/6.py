import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/2293
# r,k = wow()
# n_list = [one() for _ in range(r)]
# zero_list = [0]*10001
# n_list.sort()
# while n_list[-1]>k:
#     n_list.pop()
# for i in n_list:
#     zero_list[i]+=1
#     for value in range(i+1,k+1):
#         zero_list[value]+=zero_list[value-i]
# print(zero_list[k])


r,k = wow()
n_list = []
for _ in range(r):
    a,b = wow()
    if a>k:
        continue
    n_list.append((a,b))
m_list = [0]*(k+1)
# print(m_list)

for a,b in n_list:
    for value in range(a,k+1):
        m_list[value]=max(m_list[value],m_list[value-a]+b)
    print(a,"!!!!!")
    print(m_list)
print(m_list[k])


















