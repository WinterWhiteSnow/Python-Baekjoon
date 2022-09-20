import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# n,r = wow()
# x = n
# y = n
# for _ in range(r):
#     a,b = wow()
#     if a>n and b>n:
#         pass
#     else:
#         xx,yy = min(x,a),y#가로
#         aa,bb = x,min(b,y)#세로
#         if xx*yy >= aa*bb:
#             x = xx
#             y = yy
#         else:
#             x = aa
#             y = bb
#     # print(xx*yy,aa*bb,x,y)
# print(x*y)

# max_max = 0
# for _ in range(one()):
#     a = inputing()
#     max_max=max(max_max,a.count("for")+a.count("while"))
# print(max_max)

# a,b=wow()
# n_list = sorted(list(wow()))
# print(n_list[-b])

# a = one()
# b = inputing()
# if b[-1] in ["q","w","e","r","t","a","s","d","f","g","z","x","c","v"]:
#     print(1)
# else:
#     print(0)

# l = one()
# n_list = list(wow())
# for i in range(l):
#     n = n_list[i]
#     a = (n//3)
#     b = (n//7)
#     c = (n//21)
#     aa = (a*(6+(a-1)*3))//2
#     bb = (b*(14+(b-1)*7))//2
#     cc = (c*(21*2+(c-1)*21))//2
#     print(aa+bb-cc)

# for _ in range(one()):
#     a,b = inputing().split()
#     a = a[::-1]
#     b = b[::-1]
#     c =int(str(int(a)+int(b))[::-1])
#     print(c)

# for _ in range(one()):
#     a = inputing().replace(" ","")
#     total = len(a)
#     cnt = 0
#     for i in list(a):
#         if i in ['A','E','I','O','U','a','e','i','o','u']:
#             cnt+=1
            
#     print(total-cnt,cnt)   

# import string
# n_dict = {}
# index = 1
# for i in list(string.ascii_uppercase):     
#     n_dict[i]=index
#     index+=1
# while True:
#     a = list(inputing())
#     if a[0] =="#":
#         break
    
#     cnt = 0
#     for i in range(len(a)):
#         if a[i] in n_dict:
#             cnt+=n_dict[a[i]]*(i+1)
#     print(cnt)

# import string
# n_dict = {}
# a_list = list(string.ascii_uppercase)
# for _ in range(one()):
#     str_str = list(inputing())
#     aa_list = list(inputing())
#     for a,b in zip(a_list,aa_list):
#         n_dict[a]=b
#     for i in range(len(str_str)):
#         if str_str[i] in n_dict:
#             str_str[i] = n_dict[str_str[i]]
#     print("".join(str_str))

n_list = [i for i in range(1,one()+1)]
while len(n_list) != 1:
    a_list = [n_list[i] for i in range(len(n_list)) if i%2 == 1]
    n_list = a_list
print(n_list[0])