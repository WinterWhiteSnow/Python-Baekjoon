import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#양도소득세 실화냐 진짜 마음이 찌ㅉ어진다ㅏㅏ
# 37문제

# for _ in range(one()):
#     y,m,d = wow()
#     cnt = 0
#     for year in range(y+1,1000):
#         if year%3 == 0:
#             cnt+=200
#         else:
#             cnt+=195
#     if y%3 == 0:
#         cnt+=20-d+(10-m)*20
#     else:
#         if m%2:
#             cnt+=20-d
#         else:
#             cnt+=19-d
#         for i in range(m+1,11):
#             if i%2:
#                 cnt+=20
#             else:
#                 cnt+=19
#     print(cnt+1)
# import string
# a_list = list(string.ascii_uppercase)
# for _ in range(one()):
#     list_list = []
#     for _ in range(one()):
#         a,b,c = inputing().split()
#         b,c = int(b),int(c)
#         n_list = [i for i in range(b,c)]
#         list_list+=n_list
#     set_list = set(list_list)
#     for index in set_list:
#         index = list_list.count(index)-1
#         print(a_list[index],end="")
#     print()
# index = 0
# while True:
#     l = one()
#     if l == 0:
#         break
#     if index != 0:
#         print()
#     a_list = list(wow())
#     b_list = list(wow())
#     a_point=0
#     b_point= 0
#     for a,b in zip(a_list,b_list):
#         if abs(a-b)>1:
#             if a>b:
#                 a_point+=a
#             else:
#                 b_point+=b
#         else:
#             if a==b:
#                 pass
#             else:
#                 if a==1 and b == 2:
#                     a_point+=6
#                 elif a==2 and b==1:
#                     b_point+=6
#                 else:
#                     if a>b:
#                         b_point+=a+b
#                     else:
#                         a_point+=a+b
#     print(f"A has {a_point} points. B has {b_point} points.")
#     index+=1 
# name = "none"
# state = 0
# while True:
#     a,b = inputing().split()
#     if a == "X" and b=="0":
#         print(name,state)
#         name="none"
#         state=0
#     elif a=="#" and b=="0":
#         exit()
#     else:
#         b = int(b)
#         if name == "none":
#             name=a
#             state=b
#         else:
#             if a == "B":
#                 if state+b>68:
#                     pass
#                 else:
#                     state+=b
#             elif a=="C":
#                 if state < b:
#                     pass
#                 else:
#                     state-=b
# name="none"
# num = 0
# while True:
#     a,b = inputing().split()
#     if a=="#" and b =="0":
#         break
#     if name=="none":
#         b = int(b)
#         name=a
#         num=b
#         print(name,"Library")
#     for index in range(1,1+one()):
#         x,y = inputing().split()
#         x = int(x)
#         if len(y)*num>x-2:
#             print(f"Book {index} vertical")
#         else:
#             print(f"Book {index} horizontal")
#         name = "none"
#     num = 0

# for _ in range(one()):
#     a = one()
#     if a == 0:
#         print(0)
#     else:
#         n_list = []
#         while a != 0:
#             n_list.append(str(a%3))
#             a//=3
#         print("".join(n_list[::-1]).lstrip("0"))

# for _ in range(one()):
#     a = inputing()
#     n_dict = {}
#     if "." in a:
#         a = a.split(".")
#         for i in range(3):
#             if i == 2:
#                 n_dict["y"]=a[i].zfill(4)
#             else:
#                 if "d" not in n_dict:
#                     n_dict["d"]=a[i].zfill(2)  
#                 else:
#                     n_dict["m"]=a[i].zfill(2)           
#     else:
#         a = a.split("/")
#         for i in range(3):
#             if i == 2:
#                 n_dict["y"]=a[i].zfill(4)
#             else:
#                 if "m" not in n_dict:
#                     n_dict["m"]=a[i].zfill(2)  
#                 else:
#                     n_dict["d"]=a[i].zfill(2)

#     d = n_dict["d"]
#     m = n_dict["m"]
#     y = n_dict["y"]
#     print(f"{d}.{m}.{y} {m}/{d}/{y}")

# a = one()
# cnt = 1
# for i in range(2,a+1):
#     cnt*=i
# print(str(cnt).count("0"))
# import string
# a = list(map(int,list(inputing())))
# cnt = 0
# list_list = [2,7,6,5,4,3,2]
# for x,y in zip(a,list_list):
#     cnt+=x*y
# cnt%=11
# n_dict = {}
# s_list =  list(string.ascii_uppercase)[:9]
# for i in range(1,10):
#     n_dict[i]=s_list[i-1]
# n_dict[0]="J"
# n_dict[10]="Z"
# print(n_dict[cnt])
# l = one()
# n_list = list(map(int,list(inputing())))
# a_list =str(n_list[0])
# for i in range(l-1):
#     a_list+=str((n_list[i]+n_list[i+1])%2)
# print(a_list)

# while True:
#     a,b= inputing().split()
#     if a==b=="#":
#         break
#     n_dict={}
#     n_dict[a]=0
#     n_dict[b]=0
#     for _ in range(one()):
#         x,y = inputing().split()
#         if x==y:
#             n_dict[a]+=1
#         else:
#             n_dict[b]+=1
#     print(a,n_dict[a],b,n_dict[b])
# from datetime import datetime
# import calendar
# month_list = []
# for i in range(1,13):
#     date = datetime(year=2022,month=i,day=1)
#     month_list.append(calendar.month_name[date.month])
# index = month_list.index("August")
# while True:
#     a,b=inputing().split()
#     if a=="0" and b =="#":
#         break
#     a = int(a)
#     if a == 4 and b == "August":
#         print("Happy birthday")
#     elif a == 29 and b == "February":
#         print("Unlucky")
#     else:
#         if month_list.index(b) > index:
#             print("No")
#         else:
#             if month_list.index(b) == index:
#                 if a > 4:
#                     print("No")
#                 else:
#                     print("Yes")
#             else:
#                 print("Yes")
case = 1
while True:
    a,b = inputing().split()
    if a==b=="#":
        break
    print("Case",case)
    list_list = [a,b]
    for _ in range(one()):
        c = list(inputing())
        for index in c:
            if index in list_list:
                print("_",end="")
            else:
                print(index,end="")
        print()
    case+=1
    




