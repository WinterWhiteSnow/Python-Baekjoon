# import sys

# inputing = lambda : sys.stdin.readline().rstrip()
# wow = lambda : map(int,inputing().split())
# one = lambda : int(inputing())

#https://www.acmicpc.net/problem/2240
# r,m = wow()
# n_list = [[0,0] for _ in range(r+1)]
# for d in range(1,r+1):
#     a = one()
#     n_list[d][a-1]=1
# # print(n_list)
# cnt = 0
# total = [[[0]*(r+1) for _ in range(m+1)] for _ in range(2)]
# total[0][0][1]=n_list[1][0]    
# total[1][1][1]=n_list[1][1]
# # print(total)
# # total[0][0][2]=n_list[2][0]+n_list[1][0]    
# # total[0][1][2]=n_list[2][0]+total[1][0][1]
# # total[1][1][2]=max(total[0][1][1]+n_list[2][1],total[1][1][1]+n_list[2][1]) 
# # total[0][2][2]=max(total[0][2][1]+n_list[2][0],total[1][1][1]+n_list[2][0])  
# # total[1][2][2]=max(total[1][2][1]+n_list[2][1],total[0][2][1]+n_list[2][1])  
# # print(total)    
# for t in range(2,r+1):
#     total[0][0][t]=total[0][0][t-1]+n_list[t][0]
#     for index in range(1,m+1):
#         total[0][index][t]=max(total[0][index][t-1],total[1][index-1][t-1])+n_list[t][0]
#         total[1][index][t]=max(total[0][index-1][t-1],total[1][index][t-1])+n_list[t][1]
        
#         # total[1][index][t]=max(total[1][1][t-1],total[0][0][t-1])+n_list[t][1]
#         # total[0][2][t]=max(total[0][2][t-1],total[1][1][t-1])+n_list[t][0]
#         # total[1][2][t]=max(total[0][1][t-1],total[1][2][t-1])+n_list[t][1]
# for i in range(2):
#     # print(total[i])
#     for mm in range(m+1):
#         # print(total[i][mm])
#         cnt = max(max(total[i][mm]),cnt)
# print(cnt)

# for t in range(int(input())):
#     t=t+1
#     r,k = map(int,input().split())
#     re = r//10
#     n_list = []
#     score = 0
#     for i in range(r):
#         list_list = list(map(int,input().split()))
#         total = 0
#         total+=list_list[0]*0.35+list_list[1]*0.45+list_list[2]*0.2
#         n_list.append(total)
#         if i == k-1:
#             score = total
#     n_list.sort(reverse=True)
#     # print(n_list)
#     check = ["A+","A0","A-","B+","B0","B-","C+","C0","C-","D0"]
#     print("#"+str(t),check[n_list.index(score)//re])
   
# for t in range(int(input())):
#     t=t+1
#     a,b = map(int,input().split())
#     a_list = list(map(int,input().split()))
#     b_list = list(map(int,input().split()))
#     if a>b:
#         a,b = b,a
#         a_list,b_list = b_list,a_list
#     max_max = 0
#     for i in range(b-a+1):
#         total = 0
#         for k in range(a):
#             total+=a_list[k]*b_list[i+k]
#         max_max = max(max_max,total)
#     print("#"+str(t),max_max)

# for t in range(int(input())):
#     t=t+1
#     r = int(input())
#     n_list = [list(map(int,input().split())) for _ in range(r)]
#     total_dict = {}
#     for _ in range(3):
#         n_dict = {}
#         for y in range(r):
#             for x in range(r):
#                 if x not in n_dict:
#                     n_dict[x]=[n_list[y][x]]
#                 else:
#                     n_dict[x]+=[n_list[y][x]]
#         for key in n_dict.keys():
#             n_list[key]=n_dict[key][::-1]
#             if key not in total_dict:
#                 total_dict[key]=[n_dict[key][::-1]]
#             else:
#                 total_dict[key]+=[n_dict[key][::-1]]
#     print("#"+str(t))
#     for key in range(r):
#         for a in total_dict[key]:
#             print(*a,sep="",end=" ")
#         print()

# for t in range(int(input())):
#     t=t+1
#     n = int(input())
#     total = 0
#     for i in range(1,n+1):
#         if i%2:
#             total+=i
#         else:
#             total-=i
#     print("#"+str(t),total)

# money = [50000,10000,5000,1000,500,100,50,10]
# for t in range(int(input())):
#     t=t+1
#     num = int(input())
#     total = [0]*len(money)
#     for i in range(len(money)):
#         total[i]=num//money[i]
#         num%=money[i]
#     print("#"+str(t))
#     print(*total)   

# for t in range(int(input())):
#     t=t+1
#     r = int(input())
#     str_str = ""
#     for _ in range(r):
#         a,b = input().split()
#         b = int(b)
#         str_str+=a*b
#     print("#"+str(t))
#     for i in range(0,len(str_str),10):
#         print(str_str[i:i+10])

# import datetime
# for t in range(int(input())):
#     t=t+1
#     a,b,c,d = map(int,input().split())
#     x = datetime.datetime(2023,a,b)
#     y = datetime.datetime(2023,c,d)
#     print("#"+str(t),end=" ")
#     print((y-x).days+1)

# for t in range(int(input())):
#     t=t+1
#     l = int(input())
#     n_list = list(map(int,input().split()))
#     print("#"+str(t),*sorted(n_list))

# for t in range(int(input())):
#     t=t+1
#     p1,nomal,limit,p2,total = map(int,input().split())
#     x = p1*total
#     y = nomal
#     total-=limit
#     if total > 0:
#         y+=total*p2
#     print("#"+str(t),min(x,y))

# for t in range(int(input())):
#     t=t+1
#     n_list = list(map(int,input().split()))
#     n_list.sort()
#     n_list = n_list[1:-1]
#     print("#"+str(t),round(sum(n_list)/8))

# for t in range(int(input())):
#     t=t+1
#     n = int(input())
#     start = n
#     step=1
#     visit = [0]*10
#     while True:
#         n_list = list(map(int,list(str(n*step))))
#         # print(n_list,visit)
#         check = True
#         for nn in n_list:
#             visit[nn]=1
#         for i in range(10):
#             if visit[i] == False:
#                 check = False
#                 break
#         if check == False:
#             step+=1
#         else:
#             break
#     print("#"+str(t),start*step)
    
# for t in range(int(input())):
#     t=t+1
#     h,m,hh,mm = map(int,input().split())
#     hhh = h+hh
#     mmm = m+mm
#     hhh+=mmm//60
#     mmm%=60
#     while hhh > 12:
#         hhh-=12
#     print("#"+str(t),hhh,mmm)
# num = [11,7,5,3,2]
# for t in range(int(input())):
#     t=t+1
#     n = int(input())
#     n_list = []
#     for i in range(5):
#         f = num[i]
#         cnt = 0
#         while n%f == 0:
#             cnt+=1
#             n//=f
#         n_list.append(cnt)
#     print("#"+str(t),*n_list[::-1])

# for t in range(int(input())):
#     t=t+1
#     r = int(input())
#     total = 0
#     state = 0
#     for _ in range(r):
#         n_list = input().split()
#         if len(n_list) == 1:
#             total+=state
#         else:
#             a,b = map(int,n_list)
#             if a == 1:
#                 state+=b
#             elif a==2:
#                 state-=b
#                 state=max(0,state)
#             total+=state
#     print("#"+str(t),total)
    
# for t in range(int(input())):
#     t=t+1
#     n = int(input())
#     print("#"+str(t),n//3)

# for t in range(int(input())):
#     t=t+1
#     a,b = map(int,input().split())
#     print("#"+str(t),(a+b)%24)

# for t in range(int(input())):
#     t=t+1
#     a,b,c = map(int,input().split())
#     print("#"+str(t),end=" ")
#     if b<c:
#         print(-1)
#     elif a<=c<=b:
#         print(0)
#     else:
#         print(a-c)

# for t in range(int(input())):
#     t=t+1
#     l = int(input())
#     n_list = list(map(int,input().split()))
#     average= sum(n_list)/l
#     cnt = 0
#     for n in n_list:
#         if n <= average:
#             cnt+=1
#     print("#"+str(t),cnt)


# for t in range(int(input())):
#     t=t+1
#     a = input()
#     for i in ["a","e","i","o","u"]:
#         a=a.replace(i,"")
    # print("#"+str(t),a)


# for t in range(int(input())):
#     t=t+1
#     a = list(input())
#     l = len(a)
#     b = list("0"*l)
#     cnt = 0
#     # print(a,b)
#     for i in range(l):
#         if a[i] != b[i]:
#             cnt+=1
#             for k in range(i,l):
#                 if b[k] == "1":
#                     b[k]="0"
#                 else:
#                     b[k]="1"
#     print("#"+str(t),cnt)

# for t in range(int(input())):
#     t=t+1
#     a,b = 1,1
#     order = list(input())
#     for o in order:
#         if o == "L":
#             b+=a
#         else:
#             a+=b
#     print("#"+str(t),a,b)

# for t in range(10):
#     t=int(input())
#     a,b = map(int,input().split())
#     print("#"+str(t),a**b)

# for t in range(10):
#     t=t+1
#     k = int(input())
#     n_list = [list(input()) for _ in range(8)]
#     n_dict = {}
#     for y in range(8):
#         for x in range(8):
#             if x not in n_dict:
#                 n_dict[x]=[n_list[y][x]]
#             else:
#                 n_dict[x]+=[n_list[y][x]]
#     cnt = 0
#     for y in range(8):
#         for x in range(8-k+1):
#             if n_list[y][x:x+k] == n_list[y][x:x+k][::-1]:
#                 cnt+=1
#             if n_dict[y][x:x+k] == n_dict[y][x:x+k][::-1]:
#                 cnt+=1
#     print("#"+str(t),cnt)
    
# for t in range(int(input())):
#     t= t+1
#     cnt = 0
#     a,b = map(int,input().split())
#     for i in range(a,b+1):
#         x = list(str(i))
#         # print(i,x,x[::-1])
#         if x == x[::-1]:
#             y = i**(1/2)
#             # print(i,y)
#             if y == int(y):
#                 z = list(str(int(y)))
#                 if z==z[::-1]:
#                     cnt+=1
#     print("#"+str(t),cnt)

# for t in range(int(input())):
#     t= t+1
#     a = int(input())
#     n_list = [f"1/{a}" for _ in range(a)]
#     print("#"+str(t),*n_list) 

# for t in range(int(input())):
#     t= t+1
#     a,b = input().split()
#     print("#"+str(t),end=" ")
#     if len(a) <= 1 and len(b) <=1:
#         print(int(a)*int(b)) 
#     else:
#         print(-1)   

# from collections import deque
# for _ in range(10):
#     t = int(input())
#     n_list = deque(list(map(int,input().split())))    
#     num = 1
#     while True:
#         a = n_list.popleft()
#         a-=num
#         if a <= 0:
#             n_list.append(0)
#             break
#         else:
#             n_list.append(a)
#         num+=1
#         if num == 6:
#             num = 1
#         # print(n_list)
#     print("#"+str(t),*n_list)

def go():
    global cnt
    for y in range(100):
        for x in range(100):
            if n_list[y][x] == 1:
                if 0<=y+1<100:
                    if n_list[y+1][x] == 2:
                        n_list[y][x]="X"
                        n_list[y+1][x]="X"
                        cnt+=1
            if n_list[y][x] == 2:
                if 0<=y-1<100:
                    if n_list[y-1][x] == 1:
                        n_list[y][x]="X"
                        n_list[y-1][x]="X"  
                        cnt+=1 
    
for t in range(10):
    t=t+1
    l = int(input())
    n_list = [list(map(int,input().split())) for _ in range(100)]
    cnt = 0
    for y in range(100):
        for x in range(100):
            if n_list[y][x] == 1:
                if 0<=y+1<100:
                    if n_list[y+1][x] == 2:
                        n_list[y][x]="X"
                        n_list[y+1][x]="X"
                        cnt+=1
            if n_list[y][x] == 2:
                if 0<=y-1<100:
                    if n_list[y-1][x] == 1:
                        n_list[y][x]="X"
                        n_list[y-1][x]="X"  
                        cnt+=1 
    while True:
        repeat = False
        for y in range(100):
            for x in range(100):
                if n_list[y][x] == 1:
                    if 0<=y+1<100:
                        if n_list[y+1][x]==0:
                            n_list[y][x],n_list[y+1][x]=n_list[y+1][x],n_list[y][x]
                            repeat = True
                    else:
                        n_list[y][x]=0
                        repeat = True
                if n_list[y][x] == 2:
                    if 0<=y-1<100:
                        if n_list[y-1][x]==0:
                            n_list[y][x],n_list[y-1][x]=n_list[y-1][x],n_list[y][x]
                            repeat = True
                    else:
                        n_list[y][x]=0
                        repeat = True
        go()
        if repeat == False:
            break
    print("#"+str(t),cnt)                    
                          



