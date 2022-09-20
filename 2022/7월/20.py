import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())


# print("n e")
# print("- -----------")
# for i in range(10):
#     if i==0:
#         print(0,1)
#     elif i == 1:
#         print(i,2)
#     elif i == 2:
#         print(i,2.5)
#     else:
#         cnt =1
#         n_list = []
#         count = 1
#         for index in range(1,i+1):
#             count*=1/index
#             cnt+=count
#         print(f"{i} {cnt:.9f}")

# for _ in range(one()):
#     a = one()
#     if a == 1:
#         print(1)
#     else:
#         cnt = 1
#         for _ in range(a-1):
#             cnt+=0.5
#             cnt*=2
#         print(int(cnt))

# import string
# n_list = list(string.ascii_uppercase)
# n_dict = {}
# dict_n = {}
# for i in range(len(n_list)):
#     n_dict[n_list[i]]=i
#     dict_n[i]=n_list[i]
# for _ in range(one()):
#     a,b = wow()
#     list_list = list(inputing())
#     str_str = ""
#     for i in list_list:
#         calculate = (a*n_dict[i]+b)%26
#         str_str+=dict_n[calculate]
#     print(str_str)

# import string
# n_list = list(string.ascii_uppercase)
# n_dict = {}
# for i in range(len(n_list)):
#     n_dict[str(i+1)]=n_list[i]
# for _ in range(one()):
#     l,q = inputing().split()
#     list_list = inputing().split()
#     if q == "C":
#         for i in list_list:
#             print(n_list.index(i)+1,end=" ")
#         print()
#     else:
#         for i in list_list:
#             print(n_dict[i],end=" ")
#         print()    

# x,a = wow()
# y,b = wow()
# z,c = wow()
# for state in range(100):
#     state = state%3
#     if state == 0:
#         b = a+b
#         if b >=y:
#             a = b-y
#             b = y
#         else:
#             a = 0
#     if state == 1:
#         c = b+c
#         if c >=z:
#             b = c-z
#             c = z
#         else:
#             b = 0
#     if state == 2:
#         a = a+c
#         if a>=x:
#             c = a-x
#             a =x
#         else:
#             c = 0
# print(a)
# print(b)
# print(c)

# num = one()
# first_num = num
# while True:
#     number = list(map(int,list(str(num))))
#     cnt = 0
#     for i in number:
#         cnt+=i**2
#     if cnt == 1:
#         print("HAPPY")
#         break
#     if cnt == 4:
#         print("UNHAPPY")
#         break
#     num = cnt



# a = one()
# if a <= 10:
#     print(1)
# else:
#     b = 11
#     cnt = 1
#     while a > int(b):
#         c = int(str(b)+"1")
#         if c > a:
#             break
#         else:
#             b=c
#         cnt+=1
#     print(str(b).count("1"))

# r,rr,ll = wow()
# garo_dict = {}
# sero_dict = {}
# for i in range(r):
#     i=i+1
#     n_list = list(wow())
#     garo_dict[i]=n_list
#     for index in range(r):
#         index+=1
#         if index not in sero_dict:
#             sero_dict[index]=[n_list[index-1]]
#         else:
#             sero_dict[index]+=[n_list[index-1]]
# max_max = garo_dict[rr][ll-1]
# if max(garo_dict[rr]) == max_max and max(sero_dict[ll]) == max_max:
#     print("HAPPY")
# else:
#     print("ANGRY")

# a = list(inputing())
# index = 0
# if set(a).intersection({'0', '2', '1', '8'}) == set(a):
#     index = 1
#     if set(a) == {'0', '2', '1', '8'}:
#         index =2
#         if a.count("0")==a.count("1")==a.count("8")==a.count("2"):
#             index=8
# print(index)

for _ in range(one()):
    a,b=inputing().split()
    b = int(b)
    if 97<=b<=100:
        print(a,"A+")
    if 90<=b<=96:
        print(a,"A")
    if 87<=b<=89:
        print(a,"B+")
    if 80<=b<=86:
        print(a,"B")
    if 77<=b<=79:
        print(a,"C+")
    if 70<=b<=76:
        print(a,"C")
    if 67<=b<=69:
        print(a,"D+")
    if 60<=b<=66:
        print(a,"D")
    if 0<=b<=59:
        print(a,"F")
    










