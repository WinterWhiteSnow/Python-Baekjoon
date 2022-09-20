import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# for _ in range(one()):
#     n_list = inputing().split(",")
#     for i in n_list:
#         if int(i)%4 == 0:
#             print(int(i),end=" ")
#     print()

# a = one()
# b = one()
# c = one()
# n_list = sorted([a,b,c])
# cnt = n_list[-1]-n_list[0]+(n_list[1]-n_list[0])
# print(cnt)

# r,l = wow()
# n_list = list(wow())
# n_dict = {}
# for i in range(r):
#     n_dict[i]=0
# for i in range(0,len(n_list),r):
#     list_list = n_list[i:i+r]
#     for index in range(r):
#         n_dict[index]+=list_list[index]
# list_list = sorted(n_dict.items(),key=lambda x : x[0],reverse=True)
# list_list.sort(key=lambda x : x[1],reverse=True)
# print(list_list[0][0]+1)

# while True:
#     a,b,c,d = wow()
#     if a==b==c==d==0:
#         break
#     now_time = a*3600+b*60
#     time = c*3600+d*60
#     print(((time-now_time)%(60*60*24))//60)
# index = 1
# for _ in range(one()):
#     r,c,w,h = wow()
#     print(f"Case #{index}:")
#     for _ in range(r):
#         garo = ("+"+"-"*w)*c+"+"
#         print(garo)
#         for _ in range(h):
#             sero = ("|"+"*"*w)*c+"|"
#             print(sero)
#     print(("+"+"-"*w)*c+"+")
#     index+=1

a,b = wow()
index = 0
list_list = ["+","-"]
n_list = []
gap = 1

    












    

