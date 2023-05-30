import sys
from collections import deque
inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/13164
# l,k = wow()
# n_list = list(wow())
# m_list = []
# for i in range(1,l):
#     a,b = n_list[i-1],n_list[i]
#     m_list.append(b-a)
# m_list.sort()
# for _ in range(k-1):
#     m_list.pop()
# print(sum(m_list))

#https://www.acmicpc.net/problem/2212
# l = one()
# k = one()
# n_list = list(wow())
# if k>=l:
#     print(0)
# else:
#     n_list.sort()
#     # print(n_list)
#     m_list = []
#     for i in range(1,l):
#         a,b = n_list[i-1],n_list[i]
#         m_list.append(b-a)
#     m_list.sort()
#     # print(m_list)
#     for _ in range(k-1):
#         m_list.pop()
#     print(sum(m_list))


#https://www.acmicpc.net/problem/1461
# l,k = wow()
# n_list = list(wow())
# n_list.sort()
# m_list = deque()
# p_list = deque()
# for i in n_list:
#     if i>0:
#         p_list.append(i)
#     else:
#         m_list.append(i)
# move = 0
# if m_list and p_list:
#     # print("1",m_list,p_list)
#     a,b = abs(m_list[0]),p_list[-1]
#     if a>=b:
#         move+=a
#         for _ in range(min(k,len(m_list))):
#             m_list.popleft()
#     else:
#         move+=b
#         for _ in range(min(k,len(p_list))):
#             p_list.pop()
# elif m_list and len(p_list) == 0:
#     # print("2",m_list,p_list)
#     move+=abs(m_list[0])
#     for _ in range(k):
#         m_list.popleft()
# else:
#     # print("3",m_list,p_list)
#     move+=p_list[-1]
#     for _ in range(min(k,len(p_list))):
#         p_list.pop()
# while len(m_list)>=k:
#     m = abs(m_list[0])
#     move+=m*2
#     for _ in range(k):
#         m_list.popleft()
# if len(m_list)>0:
#     m = abs(m_list[0])
#     move+=m*2
# while len(p_list)>=k:
#     m = p_list[-1]
#     move+=m*2
#     for _ in range(k):
#         p_list.pop()
# if len(p_list)>0:
#     m = p_list[-1]
#     move+=m*2
# print(move)    
        
#https://www.acmicpc.net/problem/2036
# n = one()
# n_list = [one() for _ in range(n)]
# n_list.sort()
# m_list = deque()
# p_list = deque()
# for i in n_list:
#     if i >0:
#         p_list.append(i)
#     else:
#         m_list.append(i)
# cnt = 0
# while len(p_list)>=2:
#     a,b = p_list[-1],p_list[-2]
#     if a*b >a+b:
#         cnt+=a*b
#         for _ in range(2):
#             p_list.pop()
#     else:
#         cnt+=a
#         p_list.pop()
# if len(p_list)>0:
#     cnt+=p_list.pop()
# while len(m_list)>=2:
#     a,b = m_list[0],m_list[1]
#     cnt+=a*b
#     for _ in range(2):
#         m_list.popleft()
# if len(m_list)>0:
#     cnt+=m_list.popleft()
# print(cnt)      

#https://www.acmicpc.net/problem/1455
# r,c = wow()
# n_list = [list(map(int,list(inputing()))) for _ in range(r)]
# time = 0
# while True:
#     y,x = "none","none"
#     for yy in range(r):
#         for xx in range(c):
#             if n_list[yy][xx]:
#                 y,x = yy,xx
#     # print(y,x,time)
#     if y==x=="none":
#         break
#     time+=1
#     for y_index in range(y+1):
#         for x_index in range(x+1):
#             n_list[y_index][x_index]= not n_list[y_index][x_index]
#     # print(time)
#     # for i in n_list:
#     #     print(*i)
# print(time)

import string
n_dict = {}
index = 0
for i in string.ascii_uppercase:
    n_dict[i]=index
    index+=1
x = list(inputing())
now = False
def dfs(index,str_str):
    if 


















