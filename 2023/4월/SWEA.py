

# for d in range(int(input())):
#     d = d+1
#     l = int(input())
#     list_list = list(map(int,input().split()))
#     total = 0
#     sell = 0
#     for i in range(l-1,-1,-1):
#         if sell == 0:
#             sell = list_list[i]
#         else:
#             if list_list[i] < sell:
#                 total+=sell-list_list[i]
#             else:
#                 sell = list_list[i]
#     # print(total)
#     print("#"+str(d),total)

# for d in range(int(input())):
#     a,b = map(int,input().split())
#     x,y = a//b,a%b
#     print("#"+str(d+1),end=" ")
#     print(x,y)

# n = int(input())
# index = n//2
# list_list = sorted(list(map(int,input().split())))
# print(list_list[index])

# a,b = map(int,input().split())
# print(a-b+1)

# for dd in range(int(input())):
#     dd = dd+1
#     a = input()
#     y=a[:4]
#     m=a[4:6]
#     int_m = int(m)
#     d=a[-2:]
#     int_d = int(d)
#     check = False
#     if 1>int_m or int_m>12:
#         pass
#     else:
#         if int_m in [1,3,5,7,8,10,12]:
#             if 1<=int_d<=31:
#                 check = True
#         elif int_m  in [9,11,4,6]:
#             if 1<=int_d<=30:
#                 check = True
#         else:
#             if 1<=int_d<=28:
#                 check = True
#     print("#"+str(dd),end=" ")
#     if check == True:
#         print(y+"/"+m+"/"+d)
#     else:
#         print(-1)

# import string
# str_str = list(string.ascii_uppercase)
# a = list(input())
# b = []
# for aa in a:
#     b.append(str_str.index(aa)+1)
# print(*b)

# import string
# str_str = list(string.ascii_lowercase)
# a = list(input())
# b = ""
# for aa in a:
#     if aa in str_str:
#         b+=aa.upper()
#     else:
#         b+=aa
# print(b)

# a = int(input())
# print("#"*a)

# a = """#++++
# +#+++
# ++#++
# +++#+
# ++++#"""
# print(a)

# a = int(input())
# total = 0
# for i in range(1,a+1):
#     total+=i
# print(total)

# n = int(input())
# for i in range(n+1):
#     print(2**i,end=" ")

# a,b = map(int,input().split())
# if a==1:
#     if b == 2:
#         print("B")
#     else:
#         print("A")
# if a==2:
#     if b == 3:
#         print("B")
#     else:
#         print("A")
# if a==3:
#     if b == 1:
#         print("B")
#     else:
#         print("A")

# a = int(input())
# n_list = []
# for num in range(1,int(a**(1/2))+1):
#     if a%num == 0:
#         n_list.append(num)
#         n_list.append(a//num)
# n_list = list(set(n_list))
# print(*sorted(n_list))

# a,b = map(int,input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)

# move = [(0,1),(1,0),(0,-1),(-1,0)]
# for d in range(int(input())):
#     d =d+1
#     n = int(input())
#     n_list = [[0]*n for _ in range(n)]
#     m_index = 0
#     num = 1
#     y,x = 0,0
#     while num <= n*n:
#         if 0<=y< n and 0<=x<n:
#             if n_list[y][x] == 0 :
#                 n_list[y][x]=num
#                 num+=1
#             else:
#                 my,mx = move[m_index]
#                 y-=my
#                 x-=mx
#                 m_index+=1
#                 m_index%=4
#                 # my,mx = move[m_index]
#                 # y+=my
#                 # x+=mx
#         else:
#             my,mx = move[m_index]
#             y-=my
#             x-=mx
#             m_index+=1
#             m_index%=4
#         my,mx = move[m_index]
#         y+=my
#         x+=mx
#         # print(num)
#         # for i in n_list:
#         #     print(i)
#     print("#"+str(d))
#     for i in n_list:
#         print(*i)
        
# for _ in range(int(input())):
#     n = int(input())
#     n_dict = {}
#     n_list = list(map(int,input().split()))
#     for i in n_list:
#         if i not in n_dict:
#             n_dict[i]=1
#         else:
#             n_dict[i]+=1
#     list_list = list(n_dict.items())
#     list_list.sort(key=lambda x: (x[1],x[0]),reverse=True)
#     print("#"+str(n),list_list[0][0])

# import string
# str_str = list(string.ascii_uppercase)+list(string.ascii_lowercase)+[str(i) for i in range(10)]+["+","/"]

# for d in range(int(input())):
#     d = d+1
#     a = list(input())
#     s = ""
#     new_s = ""
#     for i in a:
#         s+=bin(str_str.index(i))[2:].zfill(6)
#     for i in range(0,len(s),8):
#         new_s+=chr(int(s[i:i+8],2))
#     print("#"+str(d),end=" ")
#     print(new_s)

# n = int(input())
# for i in range(1,n+1):
#     str_str = str(i)
#     for n in ["3","6","9"]:
#         str_str = str_str.replace(n,"-")
#     if "-" in str_str:
#         for s in str_str:
#             if s.isdigit():
#                 str_str = str_str.replace(s,"")
#     print(str_str,end=" ")

# for d in range(int(input())):
#     d = d+1
#     r,n = map(int,input().split())
#     n_list = [list(map(int,input().split())) for _ in range(r)]
#     max_max = 0
#     for y in range(r-n+1):
#         for x in range(r-n+1):
#             total = 0
#             for y_index in range(y,y+n):
#                 total+=sum(n_list[y_index][x:x+n])
#             max_max = max(max_max,total)
#     print("#"+str(d),end=" ")
#     print(max_max)

# def check(y,x):
#     visit = [0]*10
#     for a in range(9):
#         num = n_list[y][a]
#         if visit[num]==0:
#             visit[num]=1
#         else:
#             return False
#     visit = [0]*10
#     for a in range(9):
#         num = n_list[a][x]
#         if visit[num]==0:
#             visit[num]=1
#         else:
#             return False
#     visit = [0]*10
#     for yy in range(y,y+3):
#         for xx in range(x,x+3):
#             num = n_list[yy][xx]
#             if visit[num] == 0:
#                 visit[num]=1
#             else:
#                 return False
#     return True
    
# for d in range(int(input())):
#     d= d+1
#     n_list = [list(map(int,input().split())) for _ in range(9)]
#     state = True
#     for y in range(0,9,3):
#         for x in range(0,9,3):
#             state = check(y,x)
#             if state == False:
#                 # print(y,x)
#                 break
#         if state == False:
#             break
#     print("#"+str(d),1 if state == True else 0)
    
    
# for d in range(int(input())):
#     d = d+1
#     r,k = map(int,input().split())
#     total = 0
#     n_list = [list(map(int,(input().split()))) for _ in range(r)]
#     for y in range(r):
#         x = 0
#         cnt = 0
#         # print(y,n_list[y])
#         while x<r:
#             if n_list[y][x] == 0:
#                 if cnt == k:
#                     total+=1
#                 cnt = 0
#             else:
#                 cnt+=1
#             x+=1
#         if cnt == k:
#             total+=1
#     n_dict = {}
#     for y in range(r):
#         for x in range(r):
#             if x not in n_dict:
#                 n_dict[x]=[n_list[y][x]]
#             else:
#                 n_dict[x]+=[n_list[y][x]]
#     n_list = list(n_dict.values())
#     for y in range(r):
#         x = 0
#         cnt = 0
#         # print(y,n_list[y])
#         while x<r:
#             if n_list[y][x] == 0:
#                 if cnt == k:
#                     total+=1
#                 cnt = 0
#             else:
#                 cnt+=1
#             # print(x,cnt)
#             x+=1
#         if cnt == k:
#             total+=1
#         # print("end",cnt,n_list[y],total)
#     print("#"+str(d),total)

# for d in range(int(input())):
#     d = d+1
#     a = input()
#     str_str = ""
#     index=  0
#     l = len(a)
#     while index<l:
#         if str_str == "":
#             str_str+=a[index]
#         else:
#             if a[len(str_str):len(str_str)+len(str_str)]==str_str:
#                 break
#             else:
#                 str_str+=a[index]
#         index+=1
#     print("#"+str(d),len(str_str))
# memory = [[1],[1,1]]
# for t in range(int(input())):
#     t=t+1
#     n = int(input())
#     if len(memory) < n:
#         while len(memory)<n:
#             new_list = [1]
#             front_list = memory[-1]
#             for i in range(len(front_list)-1):
#                 new_list.append(front_list[i]+front_list[i+1])
#             new_list.append(1)
#             memory.append(new_list)
#     print("#"+str(t))
#     for i in range(n):
#         print(*memory[i])

# for t in range(int(input())):
#     t=t+1
#     a = input().rstrip()
#     print("#"+str(t),end=" ")
#     # print(a,a[::-1])
#     if a==a[::-1]:
#         print(1)
#     else:
#         print(0)    

for t in range(int(input())):
    t=t+1
    r,k = map(int,input().split())
    n_list = []
    for i in range(r):
        list_list = list(map(int,input().split()))
        total = 0
        total+=list_list[0]*0.35+list_list[1]*0.45+list_list[2]*0.2
        n_list.append([total,i+1])
    n_list.sort(key=lambda x: x[0],reverse=True)
    # print(n_list)
    n_dict = {}
    check = ["A+","A0","A-","B+","B0","B-","C+","C0","C-","D0"]
    print("#"+str(t),end=" ")
    for i in range(r):
                 
            
    















