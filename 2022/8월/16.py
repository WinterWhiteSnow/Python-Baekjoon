import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#52

# n_dict = {}
# for index in range(1,1+one()):
#     n_dict[index] = inputing()
# for _ in range(one()):
#     order = one()
#     if order in n_dict:
#         rule = n_dict[order]
#         print(f"Rule {order}: {rule}")
#     else:
#         print(f"Rule {order}: No such rule")

# for _ in range(one()):
#     a,b,c = wow()
#     n_list = []
#     for _ in range(a):
#         n_list.append(c)
#         c+=1
#         if c>b:
#             c-=b
#     print(n_list.count(1))
# cnt = 0
# for _ in range(one()):
#     a,b,c,d = map(float,inputing().split())
#     if (a<=56 and b<=45 and c<=25) or (a+b+c <= 125):
#         if d<=7:
#             print(1)
#             cnt+=1
#         else:
#             print(0)
#     else:
#         print(0)
# print(cnt) 

# for _ in range(one()):
#     a,b,c = map(float,inputing().split())
#     x,y,z = map(float,inputing().split())
#     a_point = a*y+b*z+c*x
#     b_point = x*b+y*c+z*a
#     if a_point == b_point:
#         print("=")
#     else:
#         if a_point>b_point:
#             print("ADAM") 
#         else:
#             print("GOSIA")  
# limit = 2020
# no_game = [1914,1918,1939,1945]
# while True:
#     year = one()
#     if year == 0:
#         break
    
#     if limit < year:
#         if (year-2016)%4 == 0:
#             print(year,"No city yet chosen")
#         else:
#             print(year,"No summer games")
#     else:
#         if 1896<=year:
#             if 1914<=year<=1918 or 1939<=year<=1945:
#                 if year%4 == 0:
#                     print(year,"Games cancelled")
#                 else:
#                     print(year,"No summer games")
#             elif year%4 == 0:
#                 print(year,"Summer Olympics")
#             else:
#                 print(year,"No summer games")
#         else:
#             print(year,"No summer games")
    
    
