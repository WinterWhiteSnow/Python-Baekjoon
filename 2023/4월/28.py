import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/14650
# n_list = ["0","1","2"]
# l = one()
# cnt = 0
# def check(str_str,count):
#     global l,cnt
#     # print(count,str_str)
#     if count == l:
#         if int(str_str)%3 == 0:
#             cnt+=1
#         return
#     if count == 0:
#         for i in n_list[1:]:
#             check(str_str+i,count+1)
#     else:
#         for i in n_list:
#             check(str_str+i,count+1)
# check("",0)
# print(cnt)

# for t in range(int(input())):
#     t = t+1
#     n,a,b = map(int,input().split())
#     end = int(n**(1/2))
#     # print(end)
#     min_min = 10000000001
#     for x in range(1,end+1):
#         y = n//x
#         # print(n,x,y,a*abs(x-y)+b*(n-x*y),b*(n-x**2))
#         # x,y = min(x,y),max(x,y)
#         min_min= min(min_min,a*abs(y-x)+b*(n-x*y),b*(n-x**2))
#     print("#"+str(t),min_min)

# n_dict = {}
# for i in range(2,1000):
#     if i not in n_dict:
#         for a in range(i,1000,i):
#             n_dict[a]=0
#         n_dict[i]=1
# n_list = [a for a,b in n_dict.items() if b == 1]
# n_list.sort()
# def check(num):
#     start = 0
#     end = len(n_list)-1
#     while start<=end:
#         mid = (start+end)//2
#         if num < n_list[mid]:
#             end=mid-1
#         else:
#             start=mid+1
#     return end
#     print(num)
#     print(start,end,n_list[start],n_list[end])
# for t in range(int(input())):
#     t = t+1
#     n = int(input())
#     end = check(n)
#     cnt = 0
#     n_dict = {}
#     for x in range(end+1):
#         for y in range(x,end+1):
#             for z in range(y,end+1):
#                 a,b,c = n_list[x],n_list[y],n_list[z]
#                 if a+b+c == n:
#                     if a<=b<=c:
#                         cnt+=1
#                         # n_dict[f"{a}{b}{c}"]=1
#     # print(n_dict,cnt)
#     print("#"+str(t),cnt)

# answer_list = []
# for t in range(int(input())):
#     t = t+1
#     a,b,c,d = map(int,input().split())
#     x,y = a/b,c/d
#     if x>y:
#         answer = "ALICE"
#     elif x<y:
#         answer = "BOB"
#     else:
#         answer = "DRAW"
#     answer_list.append(f"#{t} {answer}")
# for i in answer_list:
#     print(i)
# def garo(y,x):
#     global r
#     cnt1 = 0
#     cnt2 = 0
#     for i in range(x,min(r,x+5)):
#         if n_list[y][i]=="o":
#             cnt1+=1
#     # for i in range(x,max(x-5,-1),-1):
#     #     if n_list[y][i]=="o":
#     #         cnt2+=1
#     if cnt1 == 5 or cnt2 == 5:
#         return True
#     return False

# def sero(y,x):
#     global r
#     cnt1 = 0
#     cnt2 = 0
#     for i in range(y,min(r,y+5)):
#         if n_list[i][x]=="o":
#             cnt1+=1
#     # for i in range(x,max(y-5,-1),-1):
#     #     if n_list[i][x]=="o":
#     #         cnt2+=1
#     if cnt1 == 5 or cnt2 == 5:
#         return True
#     return False

# def diagonal(y,x):
#     global r
#     cnt1 = 0
#     cnt2 = 0
    
#     for i in range(5):
#         if y+i <r and x+i < r:
#             if n_list[y+i][x+i] == "o":
#                 cnt1+=1
#         if y+i <r and x-i>=0:
#             # print("next",y+i,x-i)
#             if n_list[y+i][x-i]=="o":
#                 cnt2+=1
#     # print("???",cnt1,cnt2)
#     if cnt1 == 5 or cnt2 == 5:
#         return True
#     return False
    
    
# def check(n):
#     for y in range(n):
#         for x in range(n):
#             if n_list[y][x] == "o":
#                 if garo(y,x) or sero(y,x) or diagonal(y,x):
#                     return True
#     return False
# for t in range(int(input())):
#     t = t+1
#     r = int(input())
#     n_list = [list(input()) for _ in range(r)]
#     state = check(r)
#     print("#"+str(t),"YES" if state else "NO")

# for t in range(int(input())):
#     t = t+1
#     a,b = input().split()
#     a,b = list(a),list(b)
#     a_l,b_l = len(a),len(b)
#     total = [[0]*(a_l+1) for _ in range(b_l+1)]
#     for y in range(1,b_l+1):
#         bb = b[y-1]
#         for x in range(1,a_l+1):
#             aa = a[x-1]
#             if bb== aa:
#                 total[y][x]=total[y-1][x-1]+1
#             else:
#                 total[y][x]=max(total[y-1][x],total[y][x-1])
#     print("#"+str(t),total[b_l][a_l])
# def check(num,cnt):
#     for i in range(1,num+1):
#         if i**3 == cnt:
#             return i
#     return False
# for t in range(int(input())):
#     t = t+1
#     n = int(input())
#     r = int(n**(1/3))+1
#     state  = check(r,n)
#     print("#"+str(t),"-1" if state == False else state)

# import math
# for t in range(int(input())):
#     t = t+1
#     a,b = input().split()
#     # a,b = list(a),list(b)
#     aa,bb = "",""
#     print("#"+str(t),end=" ")
#     l = len(a)*len(b)//math.gcd(len(a),len(b))
#     while len(aa) < l:
#         aa+=a
#     while len(bb)<l:
#         bb+=b
#     if aa==bb:
#         print("yes")
#     else:
#         print("no")
total = [1]*1000001
for i in range(2,1000001):
    total[i]=total[i-1]*i
    total[i]%=1234567891

for t in range(int(input())):
    t = t+1
    a,b = input().split()
    a,b = int(a),int(b)
    # print(cnt,cnt2)
    print("#"+str(t),total[a]%1234567891//((total[a-b]*total[b])%1234567891)%1234567891)

