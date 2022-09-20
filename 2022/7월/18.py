
import sys


inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# minus = "no"
# r = one()
# now = one()
# max_max = now
# for _ in range(r):
#     a,b = wow()
#     now+=a
#     now-=b
#     max_max = max(max_max,now)
#     if now <0:
#         minus="yes"
# if minus=="yes":
#     print(0)
# else:
#     print(max_max)

# n_list = ["A","B","C","D"]
# str_str = ""
# for index in range(4):
#     for i in range(index,index+3):
#         i = i%4
#         str_str+=n_list[i]
# for _ in range(one()):
#     num = one()
#     num%=12
#     print(str_str[num-1])

# for x in range(100,1000):
#     for y in range(100,1000):
#         if str(x)[-1] == str(y)[0]:
#             a = int(str(x)[:-1])
#             b = int(str(y)[1:])
#             if a != 0 and b != 0:
#                 if x/y == a/b and x != y and a != b:
#                     print(f"{x} / {y} = {a} / {b}")

# for ind in range(1,one()+1):
#     n_list = list(wow())
#     num = n_list[0]
#     n_list = n_list[1:-1]
#     index = 0
#     for i in range(num,0,-1):
#         n_list[index]*=i
#         index+=1
#     print(f"Case {ind}:",num-1,*n_list)

# while True:
#     a = one()
#     if a == 0:
#         break
#     n_list = list(wow())
#     if n_list[2]/n_list[1] == n_list[1]/n_list[0]:
#         r = n_list[1]//n_list[0]
#         if r != 1:
#             print(int((n_list[0]*(r**a-1))/(r-1)))
#         else:
#             print(n_list[0]*a)
#     else:
#         d = n_list[1]-n_list[0]
#         print((a*(2*n_list[0]+(a-1)*d))//2)

# while True:
#     d,x,y = map(float,inputing().split())
#     if d==x==y==0:
#         break
#     width = (16*d)/337**(1/2)
#     height = 9*width/16
#     a = x/width
#     b = y/height
#     print(f"Horizontal DPI: {a:.2f}")
#     print(f"Vertical DPI: {b:.2f}")

# while True:
#     a,b,c = wow()
#     if a==b==c==0:
#         break
#     x = a/b
#     y = a/c
#     gap = round(abs(x*60*60-y*60*60))        
#     h = gap//3600
#     m = gap%3600//60
#     s = gap%60
#     print(f"{h}:{m:0>2}:{s:0>2}")

# num = one()
# print(num*num)
# print(2)

# num = one()
# print((num-1)*(num)//2)
# print(2)

# num = one()
# print(num**3)
# print(3)

# num = one()
# index = 0
# cnt = 0
# for i in range(1,num-1):
#     index+=i
#     cnt+=index
# print(cnt)
# print(3)

# num = one()
# if len(str(num)) <= 2:
#     print(99)
# else:
#     a = str(num)
#     min = num-100
#     min = str(min)[:-2]+"99"
#     now = a[:-2]+"99"
#     max = num+100
#     max = str(max)[:-2]+"99"
#     n_list = [int(min),int(now),int(max)]
#     n_list.sort(key= lambda x : x, reverse=True)
#     n_list.sort(key= lambda x : abs(x-num))
#     print(n_list[0])

# l = one()
# cnt = 0
# for i in inputing().split():
#     if i in ["he", "him", "she", "her"]:
#        cnt+=1
# print(cnt) 

# while True:
#     n_list = inputing().split()
#     if n_list[0] == "#":
#         break
#     a,b,c,d = n_list
#     b,c,d = int(b),int(c),int(d)
#     if b<=31:
#         if b ==31:
#             if c >=5:
#                 print("?",b-30,c,d)
#             else:
#                 print(a,b,c,d)
#         else:
#             print(a,b,c,d)
#     else:
#         print("?",b-30,c,d)

# for _ in range(one()):
#     a = inputing()
#     if 6<=len(a)<=9:
#         print("yes")
#     else:
#         print("no")

# num = one()
# print("long "*(num//4)+"int")

# total = one()
# cnt = 0
# for _ in range(one()):
#     a,b=wow()
#     cnt+=a*b
# if cnt == total:
#     print("Yes")
# else:
#     print("No")


















