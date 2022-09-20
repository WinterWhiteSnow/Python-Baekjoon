import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# for _ in range(one()):
#     r = one()
#     n_list = [list(wow()) for _ in range(r)]
#     cnt = 0
#     while True:
#         count = cnt
#         check = "yes"
#         for i in n_list:
#             count+=i[0]-i[1]
#             if count <0:
#                 check ="no"
#                 break
#             # print(check,cnt)
#         if check == "yes":
#             break
#         cnt+=1
#     print(cnt)

# a,b,c,d = wow()
# check = "no"
# for x in range(50):
#     for y in range(50):
#         for z in range(50):
#             if a*x+b*y+c*z == d:
#                 check = "yes"
# print("1" if check =="yes" else 0)
        
# a,b,c = wow()
# n_dict = {}
# for _ in range(3):
#     x,y = wow()
#     for index in range(x,y):
#         if index not in n_dict:
#             n_dict[index]=1
#         else:
#             n_dict[index]+=1
# cnt = 0
# for i in list(n_dict.values()):
#     if i == 1:
#         cnt+=a
#     if i == 2:
#         cnt+=b*2
#     if i == 3:
#         cnt+=c*3
# print(cnt)

# a = inputing()
# b = inputing()
# print("1" if b in a else 0)

# a = inputing()
# aa = ""
# for i in list(a):
#     if i.isdigit():
#         pass
#     else:
#         aa+=i
# b = inputing()
# print("1" if b in aa else 0)  

# for _ in range(one()):
#     a = list(inputing())*10              
#     x = ""
#     y = ""
#     for i in range(len(a)):
#         if i%2:
#             if a[i] not in y:
#                 y+=a[i]
#         else:
#             if a[i] not in x:
#                 x+=a[i]
#     print(x,y,sep="\n")

# a = one()
# b = a
# while b >= 0:
#     if b == 3:
#         print("""3 bottles of beer on the wall, 3 bottles of beer.
# Take one down and pass it around, 2 bottles of beer on the wall.""")
#     elif b == 2:
#         print("""2 bottles of beer on the wall, 2 bottles of beer.
# Take one down and pass it around, 1 bottle of beer on the wall.""")
#     elif b == 1:   
#         print("""1 bottle of beer on the wall, 1 bottle of beer.
# Take one down and pass it around, no more bottles of beer on the wall.""")
#     elif b == 0:
#         if a>=2:
#             print(f"""No more bottles of beer on the wall, no more bottles of beer.
# Go to the store and buy some more, {a} bottles of beer on the wall.""")
#         else:
#             print(f"""No more bottles of beer on the wall, no more bottles of beer.
# Go to the store and buy some more, {a} bottle of beer on the wall.""")
#         break
#     else:
#         c = b-1
#         print(f"""{b} bottles of beer on the wall, {b} bottles of beer.
# Take one down and pass it around, {c} bottles of beer on the wall.""")
#     if b != 0:
#         print()
#     b-=1

# a = inputing()
# b = inputing()
# c = inputing()
# print("YES" if c in a and c in b else "NO")


        