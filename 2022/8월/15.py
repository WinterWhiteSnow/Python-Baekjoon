import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#52

# n = one()
# print(n%3)

# n = one()
# n_list = [0]*(n+1)
# n_list[1]=1
# if n>=2:
#     n_list[2]=2
#     for i in range(3,n+1):
#         n_list[i]=min(n_list[i-3]+1,n_list[i-1]+1)
# print("SK" if n_list[n]%2 else "CY")    

# n = one()
# n_list = [0]*(n+1)
# n_list[1]=1
# if n>=2:
#     n_list[2]=2
# for i in range(3,n+1):
#     n_list[i] = min(n_list[i-1]+1,n_list[i-3]+1)
# print("CY" if n_list[n]%2 else "SK")

# n = one()
# n_list = [0]*(n+1)
# n_list[1]=1
# if n>=2:
#     n_list[2]=2
# if n>=3:
#     n_list[3]=1
# for i in range(4,n+1):
#     if n_list[i-1]%2 == 1:
#         n_list[i]=n_list[i-1]+1
#     elif n_list[i-3]%2 == 1:
#         n_list[i]=n_list[i-3]+1
#     elif n_list[i-4]%2 == 1:
#         n_list[i]=n_list[i-4]+1
#     else:
#         n_list[i] = min(n_list[i-1]+1,n_list[i-3]+1,n_list[i-4]+1)
#     # print(n_list)
# print("SK" if n_list[n]%2 == 0 else "CY")

# n = one()
# print("SK" if n%4%2 else "CY")


# n = one()
# n_list = list(wow())
# cnt=-1
# if min(n_list) > 0:
#     cnt= 0
# for i in set(n_list):
#     if n_list.count(i) ==i:
#         cnt = i
# print(cnt)

# for _ in range(one()):
#     cm,kg= map(float,inputing().split())
#     m = cm/100
#     bmi = kg/(m**2)
#     if cm < 140.1:
#         print(6)
#     elif 140.1<=cm<146:
#         print(5)
#     elif 146<=cm<159:
#         print(4)
#     elif 159<=cm<161:
#         if 16<=bmi<35:
#             print(3)
#         else:
#             print(4)
#     elif 161<=cm<204:
#         if 20<=bmi<25:
#             print(1)
#         elif 18.5<=bmi<20 or 25<=bmi<30:
#             print(2)
#         elif 16<=bmi<18.5 or 30<=bmi<35:
#             print(3)
#         elif bmi<16 or 35<=bmi:
#             print(4)
#     elif 204<=cm:
#         print(4)


# l = one()
# num = int(inputing(),2)
# if num%2**one()==0:
#     print("YES")
# else:
#     print("NO") 
# import string
# n_list = [list(inputing()) for _ in range(4)]
# a_list = list(string.ascii_uppercase)[:15]
# a_dict = {}
# index = 0
# cnt = 0
# for i in range(15):
#     a_dict[a_list[i]]=[i%4,i//4]
# a_list+=["."]
# right_list = []
# for i in range(4):
#     right_list.append(a_list[i*4:i*4+4])
# for index in range(4):
#     for a,b in zip(n_list[index],right_list[index]):
#         if a != b:
#             if a == ".": pass
#             else:
#                 x = n_list[index].index(a)
#                 y = index
#                 # print(x,y,a_dict[a])
#                 cnt+=abs(a_dict[a][0]-x)+abs(a_dict[a][1]-y)
# print(cnt)         
# n = one()
# five = n//5
# while (n-5*five)%2 != 0:
#     five-=1
#     if five < 0:
#         break
# if five < 0:
#     if n%2 == 0:
#         print(n//2)
#     else:
#         print(-1)
# else:
#     two = (n-5*five)//2
#     print(five+two)






