import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# 오늘도 38문제 내일도..

# l = one()
# n_list = inputing().split("0")
# cnt = 0
# for i in n_list:
#     cnt = max(cnt,i.count("1"))
# print(cnt)

# num = one()
# n_list = [i for i in range(1,num*num+1)]
# for i in range(num):
#     if i%2 == 0:
#         print(*n_list[num*i:num*i+num])
#     else:
#         print(*n_list[num*i:num*i+num][::-1])

# a_list = ["a","e","u","i","o"]
# for index in range(1,one()+1):
#     x = inputing()
#     check = x[-1].lower()
#     if check == "y":
#         print(f"Case #{index}: {x} is ruled by nobody.")
#     else:
#         if check not in a_list:
#             print(f"Case #{index}: {x} is ruled by a king.")
#         else:
#             print(f"Case #{index}: {x} is ruled by a queen.")

# for index in range(1,one()+1):
#     n_list = inputing().split()[::-1]
#     print(f"Case #{index}: ",end="")
#     print(*n_list)
# import math
# for _ in range(one()):
#     a,b,c = wow()
#     total = math.ceil((a*b)/(c**2))
#     if total == 1:
#         print(c**2*total)
#     else:
#         if abs((a*b)-c**2*total)<=abs(a*b-c**2*(total-1)):
#             print(c**2*total)
#         else:
#             print(c**2*(total-1))
# import string
# a_list = list(string.ascii_uppercase)
# for _ in range(one()):
#     a = inputing()
#     b = list(a)
#     n_list = "123456789"
#     if b[0] in n_list:
#         if b[0]==b[1]:
#             if b[2] in n_list and b[3] in n_list:
#                 if b[4] in a_list:
#                     if b[5] in n_list and b[6] in n_list and b[7] in n_list:
#                         print(a)

# A=str(input())
# A=A.lower()
# for i in range(len(A)):
#     if A[i]=='a':print('@',end="")
#     elif A[i]=='b':print(8,end="")
#     elif A[i]=='c':print('(',end="")
#     elif A[i]=='d':print('|)',end="")
#     elif A[i]=='e':print(3,end="")
#     elif A[i]=='f':print('#',end="")
#     elif A[i]=='g':print(6,end="")
#     elif A[i]=='h':print('[-]',end="")
#     elif A[i]=='i':print('|',end="")
#     elif A[i]=='j':print('_|',end="")
#     elif A[i]=='k':print('|<',end="")
#     elif A[i]=='l':print(1,end="")
#     elif A[i]=='m':print('[]\\/[]',end="")
#     elif A[i]=='n':print('[]\\[]',end="")
#     elif A[i]=='o':print(0,end="")
#     elif A[i]=='p':print('|D',end="")
#     elif A[i]=='q':print('(,)',end="")
#     elif A[i]=='r':print('|Z',end="")
#     elif A[i]=='s':print('$',end="")
#     elif A[i]=='t':print('\'][\'',end="")
#     elif A[i]=='u':print('|_|',end="")
#     elif A[i]=='v':print('\\/',end='')
#     elif A[i]=='w':print('\\/\\/',end="")
#     elif A[i]=='x':print('}{',end="")
#     elif A[i]=='y':print("`/",end="")
#     elif A[i]=='z':print(2,end="")
#     else:print(A[i],end="")

# for _ in range(one()):
#     a = inputing()
#     print(len(a))
# for _ in range(one()):
#     l = one()
#     n_list = inputing().split()
#     a_list = inputing().split()
#     cnt = 0
#     for a,b in zip(n_list,a_list):
#         if a != b:
#             cnt+=1
#     print(cnt)
    
    
    
    
    
    
    
    
    
    