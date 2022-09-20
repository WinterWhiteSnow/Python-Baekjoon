import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# a,b,x,y = inputing().split()
# check = "none"
# if a == "S":
#     if x == "P" or y == "P":
#         if x==y:
#             check="A"
# if a == "R":
#     if x == "S" or y == "S":
#         if x==y:
#             check="A"
# if a == "P":
#     if x == "R" or y == "R":
#         if x==y:
#             check="A"
# if b == "S":
#     if x == "P" or y == "P":
#         if x==y:
#             check="A"
# if b == "R":
#     if x == "S" or y == "S":
#         if x==y:
#             check="A"
# if b == "P":
#     if x == "R" or y == "R":
#         if x==y:
#             check="A"
# if x == "S":
#     if a == "P" or b == "P":
#         if a==b:
#             check="B"
# if x == "R":
#     if a == "S" or b == "S":
#         if a==b:
#             check="B"
# if x == "P":
#     if a == "R" or b == "R":
#         if a==b:
#             check="B"

# if y == "S":
#     if a == "P" or b == "P":
#         if a==b:
#             check="B"
# if y == "R":
#     if a == "S" or b == "S":
#         if a==b:
#             check="B"
# if y == "P":
#     if a == "R" or b == "R":
#         if a==b:
#             check="B"
# print("?" if check == "none" else "MS" if check == "A" else "TK")

# while True:
#     a = inputing().lower()
#     if a == "*":
#         break
#     a = a.split()
#     a = set([i[0] for i in a])
#     print("Y" if len(list(a)) == 1 else "N")

# r,num = wow()
# n_list = [one() for _ in range(r)]
# for i in range(1,num+1):
#     for index in range(r-1):
#         if n_list[index]%i > n_list[index+1]%i:
#             n_list[index],n_list[index+1]=n_list[index+1],n_list[index]
# for i in n_list:
#     print(i)

# n_list = [i for i in range(1,one()+1)]
# for _ in range(one()):
#     new_list = []
#     index = one()
#     mm = 1
#     for i in range(len(n_list)):
#         if i != index*mm-1:
#             new_list.append(n_list[i])
#         else:
#             mm+=1
#     n_list = new_list
# for i in n_list:
#     print(i)
# for i in sys.stdin.readlines():
#     print("yes" if "problem" in i.lower() else "no")

# cnt = 0
# for i in sys.stdin.readlines():
#     cnt+=i.count("joke")
# print(cnt)

# x,y = 0,0
# cnt = 0
# for i in range(one()):
#     a,b = wow()
#     if a==b==0:
#         pass
#     else:
#         time = a-x
#         distance = b-y
#         # print(time,distance)
#         cnt = max(distance//time,cnt)
#         x,y = a,b
# print(cnt)


            
            

