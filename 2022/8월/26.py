import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# r = one()
# for i in range(1,r+1):
#     l = one()
#     n_list = list(wow())
#     n_dict = {}
#     for index in range(0,l*2,2):
#         list_list = [ii for ii in range(n_list[index],n_list[index+1]+1)]
#         for iii in list_list:
#             if iii not in n_dict:
#                 n_dict[iii]=1
#             else:
#                 n_dict[iii]+=1
#     answer = []
#     for _ in range(one()):
#         a = one()
#         if a in n_dict:
#             answer.append(n_dict[a])
#         else:
#             answer.append(0)
#     print(f"Case #{i}:",*answer)
#     if i != r:
#         inputing()

# import itertools
# n_list = inputing().split()
# new_list = list(itertools.permutations(n_list,r=4))
# new_list = [int("".join(i)) for i in new_list]
# new_list.sort(reverse=True)
# print(new_list[0])

# a = list(inputing())
# check = "yes"
# for i in set(a):
#     if a.count(i) >= 2:
#         check ="no"
# print("0" if check == "no" else "1")

# n_list = [list(wow()) for _ in range(one())]
# for _ in range(one()):
#     index,d = wow()
#     a = n_list[index-1]
#     cnt = 0
#     for i in range(len(n_list)):
#         if i != index-1:
#             b = n_list[i]
#             gap = abs(b[0]-a[0])**2+abs(b[1]-a[1])**2
#             if gap <= d**2:
#                 cnt+=1
#     print(cnt)

# for _ in range(one()):
#     x,y,a,b = wow()
#     if (y-x)%(a+b) == 0:
#         print((y-x)//(a+b))
#     else:
#         print(-1)

# while True:
#     a,b,c,d = inputing().split()
#     if a==b==c==d=="0":
#         break
#     x = a+b
#     y = c+d
#     a,b,c,d= int(a),int(b),int(c),int(d)
#     if x == "12" or x=="21":
#         if y == "12" or y=="21":
#             print("Tie.")
#         else:
#             print("Player 1 wins.")
#     elif y == "12" or y=="21":
#         if x == "12" or x=="21":
#             print("Tie.")
#         else:
#             print("Player 2 wins.")
#     else:
#         if a==b and c!=d:
#             print("Player 1 wins.")
#         elif c==d and a!=b:
#             print("Player 2 wins.")
#         else:
#             if a==b and c==d:
#                 if a>c:
#                     print("Player 1 wins.")
#                 elif a==c:
#                     print("Tie.")
#                 else:
#                     print("Player 2 wins.")
#             else:
#                 x =  int(str(max(a,b))+str(min(a,b)))
#                 y =  int(str(max(c,d))+str(min(c,d)))
#                 if x>y:
#                     print("Player 1 wins.")
#                 elif x==y:
#                     print("Tie.")
#                 else:
#                     print("Player 2 wins.")
    
# a = list(inputing())
# x = ord(a[0])
# y = ord("C")
# gap = x^y
# for i in a:
#     print(chr(ord(i)^gap),end="")


