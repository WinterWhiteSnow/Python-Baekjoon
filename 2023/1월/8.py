import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/26489
# cnt = 0
# for i in sys.stdin.readlines():
#     i = i.rstrip()
#     if i =="gum gum for jay jay":
#         cnt+=1
# print(cnt)

#https://www.acmicpc.net/problem/26545
# cnt = 0
# for _ in range(one()):
#     cnt+=one()
# print(cnt)

#https://www.acmicpc.net/problem/26574
# for _ in range(one()):
#     a = one()
#     print(a,a)

#https://www.acmicpc.net/problem/26575
# for _ in range(one()):
#     a,b,c = map(float,inputing().split())
#     answer = a*b*c
#     print(f"${answer:.2f}")

#https://www.acmicpc.net/problem/26766
# str_str = """ @@@   @@@ 
# @   @ @   @
# @    @    @
# @         @
#  @       @ 
#   @     @  
#    @   @   
#     @ @    
#      @     """
# for _ in range(one()):
#     print(str_str)

#https://www.acmicpc.net/problem/26307
# time = 9*60*60
# a,b = wow()
# total = a*60*60+b*60
# total = abs(time-total)
# print(total//60)

#https://www.acmicpc.net/problem/26209
# a = inputing()
# print("S" if "9" not in a else "F")

#https://www.acmicpc.net/problem/16099
# for _ in range(one()):
#     a,b,c,d = wow()
#     x = a*b
#     y = c*d
#     if x>y:
#         print("TelecomParisTech")
#     elif x==y:
#         print("Tie")
#     else:
#         print("Eurecom")

#https://www.acmicpc.net/problem/10189
# str_str = """#  # #### #### #  #
# #### #  # #  # # #
# #### #  # #  # # #
# #  # #### #### #  #"""
# print(str_str)

#https://www.acmicpc.net/problem/5341
# while True:
#     a = one()
#     if a == 0:
#         break
#     print(a*(a+1)//2)

#https://www.acmicpc.net/problem/3765
# for i in sys.stdin.readlines():
#     print(i.rstrip())

#https://www.acmicpc.net/problem/5300
# n_list = [i for i in range(1,one()+1)]
# index = 0
# for i in range(6,len(n_list),6):
#     n_list.insert(i+index,"Go!")
#     index+=1
# n_list.append("Go!")
# print(*n_list)

#https://www.acmicpc.net/problem/5357
# for _ in range(one()):
#     a = inputing()
#     str_str= ""
#     for i in a:
#         if len(str_str) == 0:
#             str_str+=i
#         else:
#             if str_str[-1] != i:
#                 str_str+=i
#     print(str_str)


#https://www.acmicpc.net/problem/5358
# n_dict = {"i":"e","e":"i","I":"E","E":"I"}
# for i in sys.stdin.readlines():
#     i = list(i.rstrip())
#     for index in range(len(i)):
#         # print(i[index],i)
#         if i[index]=="i":
#             # print(i[index],index)
#             i[index]="e"
#         elif i[index]=="e":
#             i[index]="i"
#         elif i[index]=="I":
#             i[index]="E"
#         elif i[index]=="E":
#             i[index]="I"
#         # print("end",i)
#     print("".join(i))

#https://www.acmicpc.net/problem/6825
# weight = float(inputing())
# height = float(inputing())
# answer = weight/(height**2)
# if answer > 25:
#     print("Overweight")
# elif answer < 18.5:
#     print("Underweight")
# else:
#     print("Normal weight")

#https://www.acmicpc.net/problem/6841
# for i in sys.stdin.readlines():
#     i = i.rstrip()
#     if i == "CU":
#         print("see you")
#     elif i == ":-)":
#         print("I’m happy")
#     elif i == ":-(":
#         print("I’m unhappy")
#     elif i == ";-)":
#         print("wink")
#     elif i == ":-P":
#         print("stick out my tongue")
#     elif i == "(~.~)":
#         print("sleepy")
#     elif i == "TA":
#         print("totally awesome")
#     elif i == "CCC":
#         print("Canadian Computing Competition")
#     elif i == "TY":
#         print("thank-you")
#     elif i == "YW":
#         print("you’re welcome")
#     elif i == "TTYL":
#         print("talk to you later")
#     else:
#         print(i)

#https://www.acmicpc.net/problem/6887
# a = one()
# a = int(a**(1/2))
# print(f"The largest square has side length {a}.")

#https://www.acmicpc.net/problem/10188
# for i in range(one()):
#     a,b = wow()
#     if i != 0:
#         print()
#     for _ in range(b):
#         print("X"*a)

#https://www.acmicpc.net/problem/25784
# n_list = list(wow())
# n_list.sort()
# a,b,c = n_list
# if a+b == c:
#     print(1)
# elif a*b ==c:
#     print(2)
# else:
#     print(3)

r,total = wow()
n_list = [one() for _ in range(3)]
s = sum(n_list)






