import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/25706
# l = one()
# n_list = list(wow())
# n_list = [0]+[i+1 for i in n_list]
# total = [1]*(l+1)
# for i in range(l-1,0,-1):
#     index = i
#     step = n_list[i]
#     if index+step<=l:
#         total[i]=total[i+step]+1
#     else:
#         total[i]=1
# print(*total[1:])

# n = one()
# n_list = [1000001]*(n+1)
# n_list[3]=1
# if n>=5:
#     n_list[5]=1
# for i in range(6,n+1):
#     n_list[i]=min(n_list[i-3]+1,n_list[i-5]+1,n_list[i])
# print(n_list[-1] if n_list[-1] != 1000001 else -1)

# r = one()
# n_list = [0]+[one() for _ in range(r)]
# m_list = [0]*(r+1)
# m_list[1]=n_list[1]
# if r>=2:
#     m_list[2]=n_list[1]+n_list[2]
# for i in range(3,r+1):
#     m_list[i] = max(max(m_list[i-3]+n_list[i-1],m_list[i-2])+n_list[i],m_list[i-1])
# print(max(m_list))

# n,k = wow()
# n_list = sorted(list(wow()))
# plus_list = [0]
# minus_list = [0]
# for a in n_list:
#     if a>0:
#         plus_list.append(a)
#     else:
#         minus_list.append(a)
# minus_list.sort(reverse=True)
# cnt = 0
# if plus_list[-1] < abs(minus_list[-1]):
#     cnt+=abs(minus_list.pop())
#     for _ in range(min(k-1,len(minus_list))):
#         minus_list.pop()
# else:
#     cnt+=abs(plus_list.pop())
#     for _ in range(min(k-1,len(plus_list))):
#         plus_list.pop()
# def go(list_list):
#     global cnt,k
#     while len(list_list)>=k:
#         cnt+=abs(list_list.pop())*2
#         for _ in range(k-1):
#             list_list.pop()
#     if len(list_list) != 0:
#         cnt+=abs(list_list.pop())*2
# go(plus_list)
# go(minus_list)
# print(cnt)

# n = one()
# k = one()
# n_list = sorted(list(wow()))
# new_list = [0]
# for i in range(1,n):
#     new_list.append(n_list[i]-n_list[i-1])
# new_list.sort()
# for _ in range(min(k-1,len(new_list))):
#     new_list.pop()
# print(sum(new_list))

# n,k = wow()
# n_list = list(wow())
# new_list = []
# for i in range(1,n):
#     new_list.append(n_list[i]-n_list[i-1])
# new_list.sort()
# for _ in range(min(k-1,len(new_list))):
#     new_list.pop()
# print(sum(new_list))

# for _ in range(one()):
#     r = one()
#     n_list = []
#     standard = 0
#     for i in range(r):
#         a,b = wow()
#         if a==1:
#             standard = b
#         n_list.append([a,b])
#     cnt = 0
#     n_list.sort(key=lambda x:x[0])
#     for i in range(r):
#         a,b = n_list[i]
#         if standard>=b:
#             cnt+=1
#             standard=b
#         # print(a,b,cnt)
#     print(cnt)

# r = one()
# n_list = [list(wow()) for _ in range(r)]
# n_list.sort(key=lambda x: (x[0],x[1]))
# new_list = []
# for i in range(r):
#     if len(new_list) == 0:
#         new_list.append(n_list[i][1])
#     else:
#         a,b = n_list[i]
#         if new_list[-1]<=a:
#             new_list.append(b)
#         else:
#             if new_list[-1]>b:
#                 new_list.pop()
#                 new_list.append(b)
# print(len(new_list))
    
# l = one()
# n_list = list(wow())
# n_list.sort()
# m_list = [0]*(l+1)
# m_list[1]=n_list[0]
# for i in range(1,l):
#     num = n_list[i]
#     m_list[i+1]+=num+m_list[i]
# print(sum(m_list))

r = one()
n_list = [0]+[one() for _ in range(r)]
m_list = [0]*(r+1)
m_list[1]=n_list[1]
if r>=2:
    m_list[2]=n_list[1]+n_list[2]

for i in range(3,r+1):
    m_list[i] = max(max(m_list[i-3]+n_list[i-1],m_list[i-2])+n_list[i],m_list[i-1])
print(max(m_list))




    
    
    
    
    
    
        








