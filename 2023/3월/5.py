import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/10219
# for _ in range(one()):
#     r,c = wow()
#     n_list = [list(inputing()) for _ in range(r)]
#     n_list = n_list[::-1]
#     for i in n_list:
#         print(*i,sep="")                  

#https://www.acmicpc.net/problem/2546
# for _ in range(one()):
#     inputing()
#     n,m = wow()
#     n_list = list(wow())
#     m_list = list(wow())
#     n_cnt = sum(n_list)
#     m_cnt = sum(m_list)
#     count = 0
#     for i in range(n):
#         a = n_list[i]*n
#         if a < n_cnt:
#             b = m_cnt+n_list[i]
#             if n_list[i]*(m+1)>b:
#                 count+=1
#     print(count)

#https://www.acmicpc.net/problem/2897
# r,l= wow()
# n_list = [list(inputing()) for _ in range(r)]
# total = [0]*5
# def check(y,x):
#     cnt = 0
#     c = True
#     for yy in range(y,y+2):
#         for xx in range(x,x+2):
#             if n_list[yy][xx] == "#":
#                 c = 0
#                 break
#             if n_list[yy][xx]=="X":
#                 cnt+=1
#         if c == False:
#             break
#     if c:
#         total[cnt]+=1
    
# for y in range(r-1):
#     for x in range(l-1):
#         if n_list[y][x] != "#":
#             check(y,x)
# print(*total,sep="\n")

#https://www.acmicpc.net/problem/15463
# n_list = [[0]*(2001) for _ in range(2001)]
# a_list = list(wow())
# b_list = list(wow())
# c_list = list(wow())
# index = 1
# cnt = 0
# for list_list in [a_list,b_list]:
#     x,y,xx,yy = list_list
#     for yyy in range(y,yy):
#         for xxx in range(x,xx):
#             if n_list[yyy][xxx]==0:
#                 n_list[yyy][xxx]=index
#                 cnt+=1
#     index+=1
# x,y,xx,yy = c_list
# for yyy in range(y,yy):
#     for xxx in range(x,xx):
#         if n_list[yyy][xxx]!=0:
#             n_list[yyy][xxx]=0
#             cnt-=1

# print(cnt)

#https://www.acmicpc.net/problem/17520  
# n = one()
# if n%2:
#     n+=1
# index = 2**(n//2)%16769023
# print(index)

#https://www.acmicpc.net/problem/18868
# r,l = wow()
# n_list= [list(wow()) for _ in range(r)]
# cnt = 0
# for start in range(r-1):
#     for end in range(start+1,r):
#         a = n_list[start]
#         b = n_list[end]
#         state = True
#         for index1 in range(l-1):
#             for index2 in range(index1+1,l):
#                 if a[index1]>a[index2] and b[index1]>b[index2]:
#                     pass
#                 elif a[index1]<a[index2] and b[index1]<b[index2]:
#                     pass
#                 elif a[index1]==a[index2] and b[index1]==b[index2]:
#                     pass
#                 else:
#                     state = False
#                     break
#             if state == False:
#                 break
#         if state:
#             cnt+=1
# print(cnt)
        
#https://www.acmicpc.net/problem/20650        
# n_list = sorted(list(wow()))
# # print(n_list)
# for start in range(7):
#     for mid in range(start+1,7):
#         for end in range(mid+1,7):
#             a,b,c = n_list[start],n_list[mid],n_list[end]
#             if a+b+c == n_list[-1]:
#                 print(a,b,c)
#                 exit()

#https://www.acmicpc.net/problem/18229
# r,c,k = wow()
# n_list = [list(wow()) for _ in range(r)]
# total = [0]*r
# cnt = [0]*r
# for x in range(c):
#     for y in range(r):
#         # print(x,y)
#         total[y]+=n_list[y][x]
#         cnt[y]+=1
#         if total[y]>=k:
#             print(y+1,cnt[y])
#             exit()
#             # print()
#             # exit()

#https://www.acmicpc.net/problem/27065
# total = ["X"]*5001
# for _ in range(one()):
#     num = one()
#     n_list = []
#     for index in range(1,int(num**(1/2))+1):
#         if num%index == 0:
#             if index != num//index:
#                 n_list.append(index)
#                 n_list.append(num//index)
#             else:
#                 n_list.append(index)
#     n_list.sort()
#     # print(n_list)
#     if sum(n_list[:-1])>num:
#         # print("one step",num)
#         check = True
#         for number in n_list[:-1]:
#             if total[number] == "X":        
#                 b_list = []
#                 for i in range(1,int(number**(1/2))+1):
#                     if number%i == 0:
#                         if i != number//i:
#                             b_list.append(i)
#                             b_list.append(number//i)
#                         else:
#                             b_list.append(i)
#                 b_list.sort()
#                 if sum(b_list[:-1])<=number:
#                     total[number]=True
#                 else:
#                     total[number]=False
#             # print(number,total[number])
#             if total[number]:
#                 pass
#             else:
#                 check=False
#                 break
#         if check:
#             print("Good Bye") 
#         else:
#             print("BOJ 2022")    
#     else:
#         print("BOJ 2022")        

#https://www.acmicpc.net/problem/25643
# r,c = wow()
# n_list = [inputing() for _ in range(r)]
# if r == 1:
#     print(1)
# else:
#     state = True
#     start = 0
#     end = 1
#     while True:
#         # print(start,end)
#         check = False
#         a,b = n_list[start],n_list[end]
#         # print("a,b",a,b)
#         for i in range(1,c+1):
#             x,y = a[-i:],b[:i]
#             xx,yy = a[:i],b[-i:]
#             # print("x,y",x,y)
#             # print("xx,yy",xx,yy)
#             if x == y or xx == yy:
#                 check=True
#                 break
#         if check:
#             start+=1
#             end+=1
#             if end == r:
#                 break
#         else:
#             state = False
#             break
#     print(1 if state else 0)










