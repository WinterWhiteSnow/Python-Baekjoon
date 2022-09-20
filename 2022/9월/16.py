import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# total = one()
# n_list = [0]*101
# for _ in range(one()):
#     a,b = inputing().split()
#     a = int(a)
#     if b == "R":
#         n_list[a+1:]=[(n_list[i]+1)%3 for i in range(a+1,101)]
#     else:
#         n_list[:a]=[(n_list[i]+1)%3 for i in range(a)]
# n_list = n_list[1:]
# for i in range(3):
#     answer = n_list.count(i)/100*total
#     print(f"{answer:.2f}")

# cnt = 1
# r,m = wow()
# for _ in range(r):
#     a = one()
#     if a == 0:
#         a = 1
#     cnt*=a
#     cnt%=m
# print(cnt%m)

# a,b,c = wow()
# if abs(a)+abs(b) <= c:
#     if c%2:
#         if (abs(a)+abs(b))%2:
#             print("YES")
#         else:
#             print("NO")
#     elif c%2 == 0:
#         if (abs(a)+abs(b))%2 == 0:
#             print("YES")
#         else:
#             print("NO")
# else:
#     print("NO")

# l = one()
# n_dict = {}
# for i in inputing():
#     if i not in n_dict:
#         n_dict[i]=1
#     else:
#         n_dict[i]+=1
# if len(n_dict.keys()) == 4:
#     n_list = list(n_dict.values())
#     cnt = 1
#     for i in n_list:
#         cnt*=i
#         cnt%=1000000007
#     print(cnt)
# else:
#     print(0)

# for _ in range(one()):
#     a,b,c,d = inputing().split()
#     a = float(a)
#     if b == "R":
#         r = 45
#     elif b == "G":
#         r = 30
#     elif b == "B":
#         r = 20
#     elif b == "Y":
#         r = 15
#     elif b == "O":
#         r = 10
#     else:
#         r = 5
#     if c == "C":
#         rr = 5
#     else:
#         rr = 0
#     cnt = (a*((100-r)/100))*((100-rr)/100)
#     if d == "C":
#         gap = cnt - int(cnt)
#         gap = f"{gap:.2f}"
#         gapgap = int(gap[-1])
#         gap = gap[:-1]
#         gap +="0"
#         if gapgap >= 6:
#             gap = float(gap)+0.1
#         gap = float(gap)
#         answer = int(cnt)+gap
#         print(f"${answer:.2f}")
#     else:
#         print(f"${cnt:.2f}")

# print(-1)

# r,time = wow()
# n_list = []
# index=1
# for _ in range(r):
#     p,k,c = wow()
#     x = time/k
#     if x == int(x):
#         x = int(x)-1
#     else:
#         x = int(x)
#     total = p+(x*(x+1)//2)*c
#     n_list.append([index,total])
#     index+=1
# n_list.sort(key=lambda x : x[1])
# print(*n_list[0])

# l = one()
# n_list = list(wow())
# cnt = 100
# state = "123"
# count = 2
# for i in n_list:
#     if state != i:
#         count = 2
#         cnt-=count
#         state = i
#     else:
#         count*=2
#         cnt-=count
#     if cnt <= 0:
#         count=2
#         state = "123"
#         cnt = 100
# print(100-cnt)
# r,l= wow()
# start,d = wow()
# y,x = wow()
# if d == 0:
#     d = "left"
# else:
#     d = "right"
# if r%2:
#     dd = d
# else:#마지막줄 방향
#     if d == "left":
#         dd="right"
#     else:
#         dd ="left"
# if 0<y<r:
#     print("NO...")
# else:
#     cnt = 0
#     if d == "left":
#         if y == 0:
#             if x<=start:
#                 cnt+=1
#         else:
#             if dd == "left":   
#                 if x ==l:
#                     cnt+=1
#             else: # dd == "right"
#                 cnt+=1
#     else:
#         if y == 0:
#             if start<=x:
#                 cnt+=1
#         else:
#             if dd == "left":
#                 if x ==l:
#                     cnt+=1
#             else:
#                 cnt+=1
#     print("YES!" if cnt == 0 else "NO...")
                
# for _ in range(one()):
#     n_list = list(wow())
#     l = n_list[0]
#     n_list =n_list[1:]
#     for i in range(l-1):
#         if n_list[i+1]-n_list[i] != 1:
#             print(i+2)
#             break   

     
    



            
    
    



