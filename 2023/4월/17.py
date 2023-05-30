# import sys

# inputing = lambda : sys.stdin.readline().rstrip()
# wow = lambda : map(int,inputing().split())
# one = lambda : int(inputing())

# for t in range(10):
#     t = t+1
#     l = int(input())
#     n_list = input().split()
#     r = int(input())
#     order = input().split()
#     for i in range(len(order)):
#         o = order[i]
#         if o == "I":
#             x,y = order[i+1],order[i+2]
#             x,y = int(x),int(y)
#             # new_list = order[i+3:i+3+y]
#             for index in range(y):
#                 n_list.insert(x+index,order[i+3+index])
#         elif o == "D":
#             x,y = order[i+1],order[i+2]
#             x,y = int(x),int(y)
#             for k in range(y):
#                 if len(n_list)>x:
#                     n_list.pop(x)
#                 else:
#                     break
#         elif o == "A":
#             x = order[i+1]
#             x = int(x)
#             # new_list = order[i+2:i+2:x]
#             for index in range(i+2,i+2+x):
#                 n_list.append(order[index])
#     print("#"+str(t),*n_list[:10])

#https://www.acmicpc.net/problem/4883
# index = 1
# while True:
#     r = one()
#     if r == 0:
#         break
#     n_list = [list(wow()) for _ in range(r)]
#     zero_list = [[0]*3 for _ in range(r)]
#     zero_list[0]=n_list[0]
#     zero_list[0][2]=n_list[0][2]+n_list[0][1]
#     for x in range(3):
#         if x == 0:
#             zero_list[1][x] += n_list[0][1]+n_list[1][0]
#         if x == 1:
#             zero_list[1][x]=min(zero_list[1][0]+n_list[1][1],n_list[0][1]+n_list[1][1],zero_list[0][2]+n_list[1][1])
#         if x == 2:
#             zero_list[1][x]+=min(zero_list[0][2]+n_list[1][x],zero_list[1][1]+n_list[1][2],zero_list[0][1]+n_list[1][2])
#     for y in range(2,r):
#         for x in range(3):
#             if x == 0:
#                 zero_list[y][x]=min(zero_list[y-1][0],zero_list[y-1][1])+n_list[y][x]
#             if x == 1:
#                 zero_list[y][x]=min(zero_list[y-1][0]+n_list[y][x],zero_list[y-1][1]+n_list[y][x],zero_list[y-1][2]+n_list[y][x],zero_list[y][0]+n_list[y][x])
#             if x == 2:
#                 zero_list[y][x]=min(zero_list[y-1][1]+n_list[y][x],zero_list[y-1][2]+n_list[y][x],zero_list[y][1]+n_list[y][x])
#     # answer= max(zero_list[-1][1],0)
#     answer= min(zero_list[-1][1],1000000)
#     print(str(index)+".",answer)
#     index+=1

# for t in range(int(input())):
#     t = t+1
#     l,k = map(int,input().split())
#     n_list = list(map(int,input().split()))
#     n_list.sort()
#     print("#"+str(t),sum(n_list[-k:]))   


# for t in range(int(input())):
#     t = t+1 
#     total,k = map(int,input().split())
#     a,b=0,0
#     b = total-k
#     a = k-b
#     print("#"+str(t),a,b)

# for _ in range(10):
#     t = int(input())
#     n_list = [list(map(int,input().split())) for _ in range(100)]
#     n_dict = {}
#     for y in range(100):
#         for x in range(100):
#             if x not in n_dict:
#                 n_dict[x]=[n_list[y][x]]
#             else:
#                 n_dict[x]+=[n_list[y][x]]
#     a_list = list(n_dict.values())
#     max_max = 0
#     cnt1 = 0
#     cnt2 = 0
#     for y in range(100):
#         max_max = max(max_max,sum(n_list[y]),sum(a_list[y]))
#         cnt1+=n_list[y][y]
#         cnt2+=n_list[y][99-y]
#     max_max = max(cnt1,cnt2,max_max)
#     print("#"+str(t),max_max)

# for t in range(int(input())):
#     t = t+1
#     a = list(input())
#     cnt = 0
#     index = 0
#     l = len(a)
#     while index < l:
#         x = a[index]
#         if x == "(":
#             cnt+=1
#             a[index],a[index+1]="X","X"
#         if x == ")":
#             cnt+=1
#             a[index],a[index-1]="X","X"
#         index+=1
#     print("#"+str(t),cnt)

# for t in range(10):
#     t = t+1
#     repeat = int(input())
#     n_list = sorted(list(map(int,input().split())))
#     for _ in range(repeat):
#         n_list[0],n_list[-1]=n_list[0]+1,n_list[-1]-1
#         n_list.sort()
#     print("#"+str(t),n_list[-1]-n_list[0])

# for t in range(int(input())):
#     t = t+1
#     total,a,b = map(int,input().split())
#     min_min = min(a,b)
#     max_max = (a+b)-total
#     if max_max < 0:
#         max_max = 0
#     print("#"+str(t),min_min,max_max)

# for t in range(int(input())):
#     t = t+1
#     a = int(input())
#     answer = "Alice" if a%2==0 else "Bob"
#     print("#"+str(t),answer)

# import math
# for t in range(int(input())):
#     t = t+1
#     a,b = map(int,input().split())
#     cover = b*2+1
#     print("#"+str(t),math.ceil(a/cover)) 

# for t in range(int(input())):
#     t = t+1
#     r = int(input())
#     total = 0
#     for _ in range(r):
#         a,b = map(float,input().split())   
#         total+=a*b
#     print("#"+str(t),f"{total:.6f}")

# for t in range(int(input())):
#     t = t+1
#     a,b,c = map(int,input().split())
#     total = c//min(a,b)
#     print("#"+str(t),total)

# for t in range(int(input())):
#     t = t+1
#     a = list(input())
#     f = set(a)
#     answer = "Yes" if len(f)==2 else "No"
#     print("#"+str(t),answer)

# import datetime
# for t in range(int(input())):
#     t = t+1
#     m,d = map(int,input().split())
#     f = datetime.date(year=2016,month=m,day=d).weekday()
#     print("#"+str(t),f)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
       