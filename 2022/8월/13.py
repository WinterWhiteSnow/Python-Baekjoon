import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# 49

# for _ in range(one()):
#     a,b=wow()
#     print(a+b)

# r,l = wow()
# n_list = [list(inputing()) for _ in range(r)]
# a_list = []
# for i in n_list:
#     new_list = []
#     for ii in i:
#         if ii == "W":
#             new_list.append("B")
#         else:
#             new_list.append("W")
#     a_list.append(new_list)
# inputing()
# b_list = [list(inputing()) for _ in range(r)]
# cnt = 0
# for a,b in zip(a_list,b_list):
#     for aa,bb in zip(a,b):
#         if aa!=bb:
#             cnt+=1
# print(cnt)
# for i in sys.stdin.readlines():
#     a,b = map(int,i.split())
#     a+=1
#     print(int(b/a))


# a,b = wow()
# x,y = wow()
# n_list = list(wow())
# cnt = 1
# for n in n_list:
#     cnt*=n
# print(cnt*a*b+cnt*x*y)
# for _ in range(one()):
#     a,b = inputing().split()
#     print("OK" if a==b else "ERROR")

# n_list = list(inputing())
# A = 0
# B = 0
# check = "no"
# for i in range(0,len(n_list),2):
#     if n_list[i] == "A":
#         A+=int(n_list[i+1])
#     else:
#         B+=int(n_list[i+1])
        
#     if check == "yes":
#         if abs(A-B)>=2:
#             break
#         else:
#             pass
#     else: # check == "no"
#         if A == 11 or B == 11:
#             break
#         else:
#             if A == B == 10:
#                 check = "yes"
# print("A" if A>B else "B")

# for _ in range(one()):
#     n_list = inputing().split()
#     name = n_list[0]
#     n_list = list(map(int,n_list[1:]))
#     total = sum(n_list)
#     if total >= 55:
#         num = 100/total
#         a = n_list[0]/35
#         b = n_list[1]/25
#         c = n_list[2]/40
#         if min(a,b,c)>=0.3:
#             print(name,total,"PASS")
#         else:
#             print(name,total,"FAIL")
#     else:
#         print(name,total,"FAIL")

# for _ in range(one()):
#     a = inputing()
#     if "D" in a:
#         index = a.index("D")
#         print(a[:index].count("U"))
#     else:
#         print(a.count("U"))

a,b = wow()
x,y = wow()
check = "no"
if x<0 and y>=10:
    print("A storm warning for tomorrow! Be careful and stay home if possible!")
else:
    if a>x:
        print("MCHS warns! Low temperature")
        check ="yes"
    elif a<=x and y>b:
        print("MCHS warns! Strong wind")
        check = "yes"
    else:
        print("No message")
if check =="yes":
    print("is expected tomorrow.")