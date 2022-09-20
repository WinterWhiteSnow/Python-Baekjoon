import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# n_dict = {}
# for _ in range(one()):
#     a,b = wow()
#     for i in range(a,b):
#         if i not in n_dict:
#             n_dict[i]=1
#         else:
#             n_dict[i]+=1
# total = one()
# max_max = max(n_dict.values())
# print("0" if max_max > total else 1)

# for _ in range(one()):
#     cnt = 0
#     a,b =wow()
#     for x in range(1,a+b):
#         cnt+=x
#     cnt*=(a+b)
#     print(cnt)
# index = 1
# while True:
#     r = one()
#     if r==0:
#         break
#     cnt=0
#     for i in range(r):
#         if i == 0:
#             cnt+=one()
#         elif i == r-1:
#             n_list=list(wow())
#             cnt+=sum(n_list)
#         else:
#             n_list=list(wow())
#             cnt+=n_list[0]+n_list[-1]
#     print(f"Case #{index}:{cnt} ")
#     index+=1

# n_list = inputing().split()
# n_dict = {}
# for i in n_list:
#     a,b=list(i)
#     # print(a,b)
#     if a not in n_dict:
#         n_dict[a]=1
#     else:
#         n_dict[a]+=1     
# print(max(n_dict.values()))
# index = 1
# while True:
#     a,b = inputing().split()
#     if a==b=="#":
#         break
#     if index != 1:
#         print()
#     print(f"Case {index}")
#     for _ in range(one()):
#         x = list(inputing())
#         for xx in x:
#             if xx == " ":
#                 print(xx,end="")
#             elif xx.lower() in [a,b]:
#                 print("_",end="")
#             else:
#                 print(xx,end="")
#         print()
#     index+=1

# a,b = inputing().split()
# n_dict = {"A":[11,11],"K":[4,4],"Q":[3,3],"J":[20,2],"T":[10,10],"9":[14,0],"8":[0,0],"7":[0,0]}
# cnt = 0
# for i in sys.stdin.readlines():
#     x,y = list(i.rstrip())
#     if y==b:
#        cnt+=n_dict[x][0]
#     else:
#         cnt+=n_dict[x][1]
# print(cnt) 

# from datetime import datetime
# import calendar
# index = 1
# while True:
#     r = one()
#     if r== 0:
#         break
#     n_dict = {}
#     for i in range(1,13):
#         n_dict[calendar.month_name[i][:3]]=""
#     for _ in range(r):
#         day,month,year = wow()
#         m = calendar.month_name[month][:3]
#         n_dict[m]+="*"
#     print(f"Case #{index}:")
#     for a,b in n_dict.items():
#         print(f"{a}:{b}")
#     index+=1

# a,b = inputing().split()
# if a == "E":
#     state = "none"
#     cnt = 0
#     for i in list(b):
#         if state == "none":
#             state = i
#             cnt=1
#         else:
#             if state == i:
#                 cnt+=1
#             else:
#                 print(state+str(cnt),end="")
#                 state = i
#                 cnt = 1
#     print(state+str(cnt)) 
        
# else:
#     b= list(b)
#     for index in range(len(b)):
#         if index%2 == 0:
#             print(b[index]*int(b[index+1]),end="")

# l = one()
# n_list = list(wow())
# max_l = 0
# for i in range(l):
#     new_list = [n_list[i]]
#     for a in range(i+1,l):
#         b = n_list[a]
#         if new_list[-1]<=b:
#             new_list.append(b)
#         else:
#             break
        
#     max_l=max(max_l,len(new_list))
# print(max_l)

# for index in range(1,one()+1):
#     total = one()
#     l = one()
#     n_list = list(wow())
#     check = "no"
#     for a in range(l):
#         for b in range(a+1,l):
#             if n_list[a]+n_list[b] == total:
#                 print(f"Case #{index}: {a+1} {b+1}")
#                 check = "yes"
#                 break
#         if check == "yes":
#             break
# n_list = [inputing().split() for _ in range(one())]
# cnt = 0        
# for num in range(1,101):
#     for order,number in n_list:
#         number = int(number)
#         if order == "ADD":
#             num+=number
#         if order == "SUBTRACT":
#             num-=number
#             if num < 0:
#                 break
#         if order == "MULTIPLY":
#             num*=number
#         if order == "DIVIDE":
#             num/=number
#             if num != int(num):
#                 break
#     if num < 0 or int(num) != num:
#         cnt+=1
# print(cnt)

while True:
    a = inputing()
    if a == "#":
        break
    check = "no"
    for i in range(len(a)):
        b = list(a)
        del b[i]
        if b == b[::-1]:
            print("".join(b))
            check = "yes"
            break
    if check == "no":
        print("not possible")












