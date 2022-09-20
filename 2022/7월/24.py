import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# while True:
#     a = inputing().split()
#     if a[0] == "0":
#         break
#     a,b = a
#     b = int(b)
#     n_list = inputing().split()
#     result = []
#     for _ in range(b):
#         list_list = inputing().split()
#         total = list_list[0]
#         check = list_list[1]
#         check = int(check)
#         list_list = list_list[2:]
#         if len(list(set(n_list) & set(list_list)))>=check:
#             result.append("yes")
#         else:
#             result.append("no")
#     if "no" in result:
#         print("no")
#     else:
#         print("yes")
# import string
# str_list = list(string.ascii_lowercase)*2
# while True:
#     llllll = inputing()
#     if llllll == "#":
#         break
#     a,b,c = llllll.split()
#     index_list = []
#     for aa,bb in zip(list(a),list(b)):
#         gap = str_list.index(bb)-str_list.index(aa)
#         index_list.append(gap)
#     c = list(c)
#     print(llllll,"",end="")
#     for cc in range(len(c)):
#         print(str_list[str_list.index(c[cc])+index_list[cc]],end="")
#     print()
# for i in sys.stdin.readlines():
#     n_dict = {}
#     a = int(i)    
#     index_list = []
#     index = 1
#     while True:
#         b = a*index
#         for i in list(str(b)):
#             n_dict[i]=1
#         if len(set(n_dict.keys())) >= 10:
#             break
#         index+=1
#     print(index)

# for index in range(1,one()+1):
#     print(f"Test set {index}:")
#     check_list = [inputing() for _ in range(one())]
#     list_list = []
#     for _ in range(one()):
#         list_list.extend(inputing().split())
#     for i in check_list:
#         if i in list_list:
#             print(i,"is present")
#         else:
#             print(i,"is absent")
#     print()

# for _ in range(one()):
#     list_list =  inputing().split()
#     start = list_list.index(inputing())
#     l = len(list_list)
#     for _ in range(one()-1):
#         start+=1
#         start%=l
#     print(list_list[start])

# while True:
#     a = inputing()
#     if a == "END":
#         break
#     b = list(a.replace(" ",""))
#     n_dict = {}
#     repeat = "no"
#     for i in b:
#         if i not in n_dict:
#             n_dict[i]=0
#         else:
#             repeat="yes"
#             break
#     if repeat == "no":
#         print(a)

# while True:
#     a = inputing()
#     if a == "#":
#         break
#     a = list(a)
#     total = len(a)
#     att = a.count("A")
#     if att>=total/2:
#         print("need quorum")
#     else:
#         y = a.count("Y")
#         n = a.count("N")
#         if y == n:
#             print("tie")
#         else:
#             if y>n:
#                 print("yes")
#             else:
#                 print("no")

# while True:
#     a = inputing()
#     b = inputing()
#     if a==b=="E":
#         break
#     a =list(a)
#     b =list(b)
#     a_point = 0
#     b_point = 0
#     for x,y in zip(a,b):
#         if x == "S":
#             if y =="R":
#                 b_point+=1
#             elif y =="P":
#                 a_point+=1
#         if x =="R":
#             if y =="P":
#                 b_point+=1
#             elif y == "S":
#                 a_point+=1
#         if x =="P":
#             if y =="S":
#                 b_point+=1
#             elif y == "R":
#                 a_point+=1
#     print(f"P1: {a_point}")
#     print(f"P2: {b_point}")
# index = 1
# while True:
#     r = one()
#     if r==0:
#         break
#     n_list = list(wow())
#     cnt = 0
#     check_list = {}
#     repeat = "no"
#     while len(set(n_list)) != 1:
#         new_list = []
#         for i in range(r):
#             new_list.append(abs(n_list[i]-n_list[(i+1)%r]))
#         str_str = "".join(list(map(str,new_list)))
#         if  str_str not in check_list:
#             check_list[str_str]=1
#         else:
#             repeat ="yes"
#             break
#         n_list=new_list
#         cnt+=1
#     if repeat == "no":
#         print(f"Case {index}: {cnt} iterations")
#     else:
#         print(f"Case {index}: not attained")
#     index+=1

a,b = wow()
min_min = min((a-1), (b-1))
a-=min_min
b-=min_min
if a == 1:
    print(min_min*2)
else:
    print(min_min*2+1)

