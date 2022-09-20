
import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# a,b= wow()
# cnt = 1
# for i in range(2,a+1):
#     cnt*=i
#     cnt%=b
# print(cnt)
# r,l,times = wow()
# for _ in range(r):
#     a = inputing()
#     a_list = list(a)
#     for _ in range(times):
#         for i in a_list:
#             print(i*times,end="")
#         print()

# l,r = wow()
# a = list(inputing())
# for _ in range(r):
#     index = 0
#     b = list(inputing())
#     for i in b:
#         if index == l:
#             break
#         if i == a[index]:
#             index+=1
#     if index == l:
#         print("true")
#     else:
#         print("false")
# import math
# r = one()
# cnt = 0
# for _ in range(r):
#     a = inputing().replace("0","9").replace("6","9")
#     a = int(a)
#     if a >= 100:
#         a = 100
#     cnt+=a
# answer = cnt/r
# if answer-int(answer)>=0.5:
#     print(int(answer)+1)
# else:
#     print(int(answer))

# l = one()
# a = inputing()
# for i in ["J", "A", "V"]:
#     a = a.replace(i,"")
# if a == "":
#     print("nojava")
# else:
#     print(a)

# n = one()
# cnt = 0
# while True:
#     if n%2 == 0:
#         n//=2
#         cnt+=1
#     else:
#         break
# a = n+1
# count = 0
# while a > 2:
#     count+=1
#     a//=2
# print(count+1)

# a = inputing()
# l = len("driip")
# if a[-l:] == "driip":
#     print("cute")
# else:
#     print("not cute")

# n_list = [float(inputing()) for _ in range(one())]
# n_list.sort()
# a = n_list[1]
# print(f"{a:.2f}")

# r = one()
# n_list = [one() for _ in range(r)]
# total = sum(n_list)
# average = total//r
# cnt = 0
# for i in n_list:
#     if i > average:
#         cnt+=i-average
# print(cnt)

# import string
# n_dict = {}
# a = list(string.ascii_uppercase)
# aa = list("V W X Y Z A B C D E F G H I J K L M N O P Q R S T U".replace(" ",""))

# for x,y in zip(a,aa):
#     n_dict[x]=y
# while True:
#     order = inputing()
#     if order == "ENDOFINPUT":
#         break
    
#     if order == "START":
#         while True:
#             answer = inputing()
#             if answer == "END":
#                 break
#             answer= list(answer)
#             for i in answer:
#                 if i in n_dict:
#                     print(n_dict[i],end="")
#                 else:
#                     print(i,end="")
#             print()


    
    






