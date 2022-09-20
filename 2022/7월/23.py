import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# r = one()
# n_list = [list(wow()) for _ in range(r)]
# max_max = 0
 
# for i in range(3):
#     cnt =0
#     list_list = [0]*3
#     list_list[i]=1
#     for index in range(r):
#         a,b,c = n_list[index]
#         a-=1
#         b-=1
#         list_list[a],list_list[b]=list_list[b],list_list[a]
#         if list_list[c] == 1:
#             cnt+=1
#     max_max=max(max_max,cnt)
# print(max_max)

# for _ in range(one()):
#     n_list = list(map(float,inputing().split()))
#     a_list = []
#     b_list = []
#     for i in range(6):
#         index = 2*i
#         a,b= n_list[index],n_list[index+1]
#         distance = (a**2+b**2)**(1/2)
#         # print(a,b,distance)
#         if distance<=3:
#             answer = 100
#         elif distance<=6:
#             answer = 80
#         elif distance <= 9:
#             answer=60
#         elif distance <= 12:
#             answer=40
#         elif distance <= 15:
#             answer=20
#         else:
#             answer = 0
#         if len(a_list) != 3:
#             a_list.append(answer)
#         else:
#             b_list.append(answer)
#         # print(a_list,b_list)
#     a_score = sum(a_list)
#     b_score = sum(b_list)
#     result = "TIE" if a_score == b_score else "PLAYER 1 WINS" if a_score > b_score else "PLAYER 2 WINS"
#     print(f"SCORE: {a_score} to {b_score}, {result}.")

# min_x = 100
# max_x = 0
# min_y = 100
# max_y = 0
# for _ in range(one()):
#     x,y = wow()
#     min_x = min(x,min_x)
#     max_x = max(x,max_x)
#     min_y = min(y,min_y)
#     max_y = max(y,max_y)
# a = max(max_x-min_x,max_y-min_y)
# print(a*a)

# start = list(inputing())
# point = len(start) - start.count("*")
# total = 0
# a_list = []
# for _ in range(one()):
#     a = list(inputing())
#     cnt = 0
#     for x,y in zip(start,a):
#         if x != "*":
#             if x == y:
#                 cnt+=1
#     if cnt == point:
#         total+=1
#         a_list.append("".join(a))
# print(total)
# for i in a_list:
#     print(i)
# a,b,c = inputing().split()
# if a == "true":
#     a = True
# else:
#     a = False
# if c == "true":
#     c = True
# else:
#     c = False
# if b == "AND":
#     if a == c:
#         print("true" if a == True else "false")
#     else:
#         print("false")
# else:
#     if a == True or c == True:
#         print("true")
#     else:
#         print("false")

# a = list(inputing().lower())
# n_dict = {"b":"v","e":"ye","h":"n","p":"r","c":"s","y":"u","x":"h"}
# for i in a:
#     if i in n_dict:
#         print(n_dict[i],end="")
#     else:
#         print(i,end="")

# n_list = [1,0,0]
# for i in list(inputing()):
#     if i == "A":
#         n_list[0],n_list[1]=n_list[1],n_list[0]
#     elif i == "B":
#         n_list[1],n_list[2]=n_list[2],n_list[1]
#     else:
#         n_list[0],n_list[2]=n_list[2],n_list[0]
# print(n_list.index(1)+1)

# for index in range(1,one()+1):
#     l = one()
#     n_list = list(inputing())
#     a_list = list(inputing())
#     cnt = 0
#     for a,b in zip(n_list,a_list):
#         if a != b:
#             cnt+=1
#     print(f"Case {index}: {cnt}")

# while True:
#     a = list(inputing())
#     if a[0] == "#":
#         break
#     for i in a:
#         if i ==" ":
#             print("%20",end="")
#         elif i == "!":
#             print("%21",end="")
#         elif i == "$":
#             print("%24",end="")
#         elif i == "%":
#             print("%25",end="")
#         elif i == "(":
#             print("%28",end="")
#         elif i == ")":
#             print("%29",end="")
#         elif i == "*":
#             print("%2"+"a",end="")
#         else:
#             print(i,end="")
#     print()
l = one()
a_list = list(wow())
b_list = list(wow())
print(sum(a_list))
cnt = 0
for a,b in zip(a_list,b_list):
    if b == 0:
        cnt+=a
print(cnt)




