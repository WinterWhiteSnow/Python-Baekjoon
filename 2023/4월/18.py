# import sys

# inputing = lambda : sys.stdin.readline().rstrip()
# wow = lambda : map(int,inputing().split())
# one = lambda : int(inputing())

#https://www.acmicpc.net/problem/2011
# num_list = [str(i) for i in range(1,27)]
# num = inputing()
# l = len(num)
# n_list = [0]*(l)
# if num[0]=="0":
#     print(0)
# elif "00" in num:
#     print(0)
# else:
#     if num[0] in num_list:
#         n_list[0]=1
#     if len(num)>1:
#         if num[0:2] in num_list:
#             n_list[1]+=1
#         else:
#             n_list[1]+=0
#         if num[1] in num_list:
#             n_list[1]+=1
#         else:
#             n_list[1]+=0
#     for i in range(2,l):
#         a,b = num[i-1:i+1],num[i]
#         # print(a,b,i)
#         if b in num_list:
#             n_list[i]+=n_list[i-1]
#         if a in num_list:
#             n_list[i]+=n_list[i-2]
#         # n_list[i]+=n_list[i-1]
#         n_list[i]%=1000000
#         # print(i,a,b,n_list)
#     print(n_list[-1])


# for t in range(10):
#     t = t+1
#     l = int(input())
#     n_list = list(map(int,input().split()))
#     cnt = 0
#     for i in range(l):
#         left,right = n_list[max(i-2,0):i],n_list[i+1:i+1+2]
#         # if i == 1:
#             # left = n_list[0]
#         standard = n_list[i]
#         left,right = max(left) if len(left)>0 else 0, max(right) if len(right)>0 else 0 
#         total = standard - max(left,right)
#         if total > 0:
#             cnt+=total
#     print("#"+str(t),cnt)

# for t in range(int(input())):
#     t = t+1
#     l = int(input())
#     n_list = input().split()
#     if l%2:
#         a,b = n_list[:l//2+1],n_list[l//2+1:]
#     else:
#         a,b = n_list[:l//2],n_list[l//2:]
#     new_list = []
#     for i in range(l//2):
#         new_list.append(a[i])
#         new_list.append(b[i])
#     if l%2:
#         new_list.append(a[-1])
#     print("#"+str(t),*new_list)

# for t in range(10):
#     t = t+1
#     l = int(input())
#     n_list = input().split()
#     ll = int(input())
#     a_list = input().split()
#     for i in range(len(a_list)):
#         order = a_list[i]
#         if order == "I":
#             x,y = a_list[i+1],a_list[i+2]
#             x,y = int(x),int(y)
#             for index in range(y):
#                 n_list.insert(x+index,a_list[i+3+index])
#         if order == "D":
#             x = int(a_list[i+1])
#             y = int(a_list[i+2])
#             for _ in range(y):
#                 if len(n_list)>x:
#                     n_list.pop(x)
#                 else:
#                     break
#     print("#"+str(t),*n_list[:10])

# for t in range(int(input())):
#     t = t+1
#     a = list(input())
#     x,o = 0,0
#     check = "none"
#     for i in range(len(a)):
#         if a[i] == "x":
#             x+=1
#         else:
#             o+=1
#         if x == 8:
#             if check == "none":
#                 check = False
#         if o == 8:
#             if check == "none":
#                 check = True
#     if check == "none":
#         check = True
#     if check == True:
#         a = "YES"
#     else:
#         a = "NO"
#     print("#"+str(t),a)
# from collections import deque
# for t in range(int(input())):
#     t = t+1
#     n_list = []
#     for _ in range(5):
#         n_list.append(deque(list(input())))
#     str_str = ""
#     while True:
#         state = False
#         for i in range(5):
#             if len(n_list[i]) > 0:
#                 str_str+=n_list[i].popleft()
#                 state= True
#         if state == False:
#             break
#         # print(n_list)
#     print("#"+str(t),str_str)

# str_str = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
# n_dict= {}
# m_dict= {}
# for i in range(10):
#     n_dict[i]=str_str[i]
#     m_dict[str_str[i]]=i
# for t in range(int(input())):
#     a,b = input().split()
#     b = int(b)
#     n_list = input().split()
#     for i in range(b):
#         n_list[i]=m_dict[n_list[i]]
#     n_list.sort()
#     print(a)
#     for i in range(b):
#         print(n_dict[n_list[i]],end=" ")
#     print()    

# for t in range(int(input())):
#     t = t+1
#     l = int(input())
#     n_list = list(map(int,input().split()))
#     cnt = 0
#     for i in range(1,l-1):
#         a,b,c = n_list[i-1],n_list[i],n_list[i+1]
#         if min(a,b,c) != b and max(a,b,c) != b:
#             cnt+=1
#     print("#"+str(t),cnt)

# for t in range(int(input())):
#     t = t+1
#     n,r = map(int,input().split())
#     n_list = [0]*n
#     # print("start!",n_list)
#     for index in range(r):
#         a,b = map(int,input().split())
#         index+=1
#         # n_list[0:3]=[index]*3
#         n_list[a-1:a-1+(b-a+1)]=[index]*(b-a+1)
#         # print(n_list,a-1,a-1+b,b-a+1)        
#     print("#"+str(t),*n_list)

# from collections import deque
# for t in range(int(input())):
#     t = t+1
#     n_list = deque(sorted(list(input())))
#     str_str = ""
#     while len(n_list)>1:
#         a,b = n_list[0],n_list[1]
#         if a==b:
#             for _ in range(2):
#                 n_list.popleft()
#         else:
#             str_str+=a
#             n_list.popleft()
#         # print(n_list)
#         # print(str_str)
#     while len(n_list)>0:
#         str_str+=n_list.popleft()
#     str_str = "".join(sorted(list(str_str)))
#     if str_str == "":
#         str_str = "Good"
#     print("#"+str(t),str_str)

# for t in range(int(input())):
#     t = t+1
#     str_str = list(input())
#     l = int(input())
#     location = list(map(int,input().split()))
#     plus = 0
#     for i in range(l):
#         num = location[i]
#         str_str.insert(num,"-")
#         plus+=1
#         for index in range(i+1,l):
#             if location[index]>num:
#                 location[index]+=1
#         # print(str_str)
#     print("#"+str(t),"".join(str_str))

# n_dict = {}
# def check(x):
#     for i in range(x):
#         if visit[i]==visit[x] or abs(x-i) == abs(visit[x]-visit[i]):
#             return False
#     return True
# def go(x):
#     global n,cnt
#     # print(x,cnt)
#     if x == n:
#         cnt+=1
#         return
#     for i in range(n):
#         visit[x]=i
#         if check(x):
#             go(x+1)      
# for t in range(int(input())):
#     t = t+1
#     n = int(input())
#     cnt = 0
#     visit = [0]*n 
#     if n not in n_dict:
#         go(0)
#         n_dict[n]=cnt
#     answer = n_dict[n]
#     print("#"+str(t),answer)
       
# for t in range(int(input())):
#     t = t+1
#     r = int(input())
#     cnt = 0
#     n_list = [int(input()) for _ in range(r)]
#     s = sum(n_list)//r 
#     for n in n_list:
#         if n>s:
#             cnt+=n-s 
#     print("#"+str(t),cnt) 


       
       
       
       
       
       


