import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/3183
# import datetime
# while True:
#     d,m,y = wow()
#     if y==m==d==0:
#         break
#     try:
#         a = datetime.date(year=y,month=m,day=d)
#         print("Valid")
#     except:
#         print("Invalid")

#https://www.acmicpc.net/problem/4383
# for i in sys.stdin.readlines():
#     n_list = list(map(int,i.split()))
#     l = n_list[0]
#     n_list =n_list[1:]
#     if l == 1:
#         print("Jolly")
#     else:
#         new_list = []
#         for i in range(l-1):
#             new_list.append(abs(n_list[i]-n_list[i+1]))
#         new_list.sort()
#         a_list = [i for i in range(1,l)]
#         if new_list == a_list:
#             print("Jolly")
#         else:
#             print("Not jolly")

#https://www.acmicpc.net/problem/9184
# n_list = [[[0]*(21) for _ in range(21)] for _ in range(21)]
# def re(a,b,c):
#     # print(a,b,c)
#     if a <= 0 or b <= 0 or c <= 0:
#         return 1
#     if a > 20 or b > 20 or c > 20:
#         return re(20, 20, 20)
#     if n_list[a][b][c] != 0:
#         return n_list[a][b][c]
#     if a < b and b < c:
#         n_list[a][b][c]=re(a, b, c-1) + re(a, b-1, c-1) - re(a, b-1, c)
#         return n_list[a][b][c]
#     n_list[a][b][c]=re(a-1, b, c) + re(a-1, b-1, c) + re(a-1, b, c-1) - re(a-1, b-1, c-1)
#     return n_list[a][b][c]
# while True:
#     a,b,c =wow()
#     if a==b==c==-1:
#         break
#     d = re(a,b,c)
#     print(f"w({a}, {b}, {c}) = {d}")

#https://www.acmicpc.net/problem/14425
# a,b = wow()
# n_dict = {}
# cnt = 0
# for _ in range(a):
#     n_dict[inputing()]=1
# for _ in range(b):
#     c = inputing()
#     if c in n_dict:
#        cnt+=1
# print(cnt) 

#https://www.acmicpc.net/problem/1269
# a,b = wow()
# a_list = set(list(wow()))
# b_list = set(list(wow()))
# print(len(a_list^b_list))

#https://www.acmicpc.net/problem/11478
# n = inputing()
# n_dict = {}
# cnt = len(n)
# for i in range(1,len(n)+1):
#     for x in range(len(n)-i+1):
#         n_dict[n[x:x+i]]=1
# print(len(n_dict))











