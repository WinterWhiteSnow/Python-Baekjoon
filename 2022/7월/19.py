import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# num = one()
# if num == 0:
#     print(1)
# elif num == 1:
#     print(0)
# else:
#     if num%2 == 0:
#         print("8"*(num//2))
#     else:
#         print("4"+"8"*((num-1)//2))

# n,l,repeat = wow()
# n_list = []
# for i in range(n):
#     n_list.extend([index for index in range(l*i+5*i,l*i+5*i+l+1)])
# index = 1
# while repeat*index+1 in n_list:
#     if repeat*index not in n_list:
#         break
#     index+=1
# print(repeat*index)

# r,q = wow()
# index = 0
# n_str = []
# for i in range(1,r+1):
#     l = one()
#     n_str+=[str(i)]*l
# for _ in range(q):
#     print(n_str[one()])

# def why(num,number):
#     n_list = []
#     if num%number == 0:
#         # print(num,number)
#         while num != 0:
#             n_list.append(num%number)
#             num//=number
#         cnt = 0
#         for i in range(len(n_list)):
#             if n_list[i] == 0:
#                 cnt+=1
#             else:
#                 break
#         return cnt
#     else:
#         return 0

# for _ in range(one()):
#     a = one()
#     cnt = 0
#     for i in range(2,a+1):
#         cnt+=why(a,i)
#     print(cnt)

# for _ in range(one()):
#     a = inputing()
#     index = len(a)
#     a = int(a)
#     aa = str(a**2)
#     if aa[-index:] == str(a):
#         print("YES")
#     else:
#         print("NO")

# import decimal
# num = one()
# a = 1
# b = 2**num
# c = decimal.Decimal(str(a))/decimal.Decimal(str(b))
# c = float(c)
# c = f"{c:.300f}"
# print(c.rstrip("0"))

# l = one()
# n_list = list(wow())
# cnt = 0
# for i in range(l):
#     for b in range(l):
#         if i != b:
#             cnt+=abs(n_list[i]-n_list[b]) 
# print(cnt)

# a,b = wow()
# x= str(a)
# c = x*a
# print(c[:b])

for _ in range(one()):
    a,b= inputing().split()
    a = sorted(list(a))
    b = sorted(list(b))
    if a==b:
        print("Possible")
    else:
        print("Impossible")




