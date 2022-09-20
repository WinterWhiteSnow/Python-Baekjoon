import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# n_dict = {}
# n_dict["oxygen"]=0
# n_dict["temperature"]=-30
# n_dict["ocean"]=0
# for _ in range(one()):
#     a,b = inputing().split()
#     if "+" in b:
#         b = int(b[1:])
#     else:
#         b = -int(b[1:])
#     n_dict[a]+=b
# print("liveable" if n_dict["oxygen"]>=14 and n_dict["ocean"]>=9 and n_dict["temperature"]>=8 else 'not liveable')

# n_dict = {}
# for i in ['1', '3', '5', '7', '8', '10', '12']:
#     n_dict[int(i)]=31
# for i in ['4', '6', '9', '11']:
#     n_dict[int(i)]=30
# n_dict[int("2")]=29
# for _ in range(one()):
#     a,b = wow()
#     if 0<=a<=23 and 0<=b<=59:
#         time = "Yes"
#     else:
#         time = "No"
#     if a in n_dict:
#         if n_dict[a]>=b>=1:
#             calendar = "Yes"
#         else:
#             calendar = "No"
#     else:
#         calendar = "No"       
#     print(time,calendar)
# a,b = wow()
# if b == 1:
#     print(-1)
# else:
#     answer = a*b//(b-1)
#     if (answer-a)*b >= answer:
#         print(answer)
#     else:
#         print(answer+1)

# a,b,c = wow()
# n_list = set([i for i in range(1,a+1)])
# a_list = set(list(wow())+list(wow()))
# print(len(list(n_list-a_list)))
# print(*n_list-a_list)
# import string
# list_list = list(string.ascii_uppercase)
# r,index = wow()
# cnt = 0
# list_list=list_list[:index]
# for _ in range(r):
#     a = list(inputing())
#     if len(list(set(a)))==len(a):
#         if sorted(a)[-1] in list_list:
#             cnt+=1
# print(cnt)
# cnt = 0
# for _ in range(one()):
#     a,b = map(float,inputing().split())
#     cnt+=a*b
# print(f"{cnt:.3f}")

# while True:
#     n,m = wow()
#     if n==m==0:
#         break
#     goal = m//n
#     n_list = list(wow())
#     cnt = 0
#     for i in n_list:
#         cnt+=min(goal,i)
#     print(cnt)

# while True:
#     d,e = wow()
#     distance = 10001
#     if d==e==0:
#         break
#     for x in range(d+1):
#         for y in range(d-x+1):
#             if x+y == d:
#                 distance = min(distance,abs((x**2+y**2)**(1/2)-e))
#     print(distance)  

a = one()
if a%2 == 0:
    print("Alice")  
    print(1)
else:
    print("Bob")
            
            