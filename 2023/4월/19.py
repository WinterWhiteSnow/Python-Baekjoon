# import sys

# inputing = lambda : sys.stdin.readline().rstrip()
# wow = lambda : map(int,inputing().split())
# one = lambda : int(inputing())

# l = one()
# n_list = inputing().split()
# zero_list = [[0]*(l+1) for _ in range(l+1)]
# for i in range(1,l+1):
#     zero_list[i][i]=1
# for i in range(1,l):
#     a,b = n_list[i-1],n_list[i]
#     if a==b:
#         zero_list[i][i+1]=1
#         zero_list[i+1][i]=1
# for gap in range(2,l+1):
#     for y in range(1,l-gap+1):
#         # print(y,gap+y)
#         a,b = n_list[y-1],n_list[y+gap-1]
#         if a==b  and zero_list[y+1][gap+y-1]:
#             zero_list[y][y+gap]=1
#             zero_list[y+gap][y]=1
# # print(*zero_list,sep="\n")
# for _ in range(one()):
#     a,b = wow()
#     print(zero_list[a][b])

# cnt = 1
# n_dict = {}
# n_list = [[0]*284 for _ in range(284)]
# for y in range(1,284):
#     total = y+1
#     for x in range(1,y+1):
#         # print(total-x,x,cnt)
#         n_dict[cnt]=[total-x,x]
#         n_list[total-x][x]=cnt
#         cnt+=1
# # print(cnt)
# for t in range(int(input())):
#     t = t+1
#     a,b = map(int,input().split())
#     y,x = n_dict[a]
#     yy,xx = n_dict[b]
#     print("#"+str(t),n_list[yy+y][xx+x])
#     # print(n_dict[a],n_dict[b])

# def go(l):
#     cnt = 0
#     new_list = []
#     for y in range(l-2):
#         for x in range(y+1,l-1):
#             for z in range(x+1,l):
#                 # print(y,x,z)
#                 new_list.append(n_list[y]+n_list[x]+n_list[z])
#     # new_list.sort(reverse=True)
#     new_list = sorted(list(set(new_list)),reverse=True)
#     return new_list[4]
    
# for t in range(int(input())):
#     t = t+1
#     n_list = list(map(int,input().split()))
#     cnt = 0
#     l = len(n_list)
#     # print(n_list)
#     print("#"+str(t),go(l))
    
# for t in range(int(input())):
#     t = t+1
#     d,h,m = map(int,input().split())
#     total = 11*24*60*60+11*60*60+11*60
#     n = d*24*60*60+h*60*60+m*60
#     print("#"+str(t),end=" ")
#     if n-total < 0:
#         print(-1)
#     else:
#         print((n-total)//60)
# def check(n):
#     for y in range(1,10):
#         for x in range(1,10):
#             if y*x == n:
#                 return "Yes"
#     return "No"
# n_dict = {}
# for i in range(2,101):
#     if i not in n_dict:
#         for x in range(i,101,i):
#             n_dict[x]=0
#         n_dict[i]=1
# n_list = [a for a,b in n_dict.items() if b == 1][4:]
# for t in range(int(input())):
#     t = t+1
#     n = int(input())
#     print("#"+str(t),end=" ")
#     if n in n_list:
#         print("No")
#     else:
#         print(check(n))
        
# for t in range(int(input())):
#     t = t+1
#     a,b = map(int,input().split())
#     print("#"+str(t),a+b)

# n_dict = {}
# for i in range(2,1000001):
#     if i not in n_dict:
#         for a in range(i,1000001,i):
#             n_dict[a]=0
#         print(i,end=" ")
# for t in range(int(input())):
#     key_dict = {}
#     t = t+1
#     n_dict = {}
#     for str_str in ["S","D","H","C"]:
#         key_dict[str_str]=13
#         for num in range(1,14):
#             num = str(num)
#             key = str_str+num.zfill(2)
#             n_dict[key]=1
#     # S,D,H,C = 13,13,13,13
    
#     n_list = input()
#     state= True
#     for i in range(0,len(n_list),3):
#         a = n_list[i:i+3]
#         b = a[0]
#         if n_dict[a]==1:
#             n_dict[a]=0
#             key_dict[b]-=1
#         else:
#             state = False
#             break
#     print("#"+str(t),end=" ")
#     if state:
#         print(*list(key_dict.values()))
#     else:
#         print("ERROR")

for t in range(int(input())):
    t = t+1
    d,l,n = map(int,input().split())
    total = 0
    for i in range(n):
        total+=d*(1+i*l*1/100)

    print("#"+str(t),int(total))
    













