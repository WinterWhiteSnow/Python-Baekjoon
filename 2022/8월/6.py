
import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#드디어 37


# for _ in range(one()):
#     a,b=  wow()
#     b = b-1
#     print(min(a,b))
import string

# a_list = list(string.ascii_lowercase)

# for _ in range(one()):
#     l = one()
#     a = list(inputing())
#     b = inputing()
#     gap = a_list.index(b)-a_list.index(a[0])
#     # print(gap)
#     new_str = ""
#     if gap > 0:
#         for i in a:
#             index = (a_list.index(i)+gap)%26
#             new_str+=a_list[index]
#     else:
#         for i in a:
#             index = a_list.index(i)+gap
#             new_str+=a_list[index]
#     print(new_str)


# for _ in range(one()):
#     l = one()
#     x = 0
#     y = 0
#     list_list = list(inputing())
#     for i in list_list:
#         if i == "E":
#             x+=1
#         if i == "S":
#             y-=1
#         if i == "N":
#             y+=1
#         if i == "W":
#             x-=1
#     print(abs(x)+abs(y))

# l = one()
# a_list = inputing().split(".")
# temp_list = []
# for i in a_list:
#     temp_list+=i.split("!")
# a_list = temp_list
# temp_list = []
# for i in a_list:
#     temp_list+=i.split("?")
# a_list = [i.rstrip().lstrip() for i in temp_list if i != ""]
# n_list = [str(i) for i in range(10)]
# for a in a_list:
#     new_list = a.split()
#     cnt = 0
#     for index in new_list:
#         if index[0].isupper():
#             list_list = list(index)
#             is_digit = "no"
#             for i in list_list:
#                 if i.isdigit():
#                     is_digit = "yes"
#                     break
#             if is_digit == "no":
#                 cnt+=1
#     print(cnt)

# a = list(inputing())
# b = list(inputing())
# a_dict = {}
# gap = b.count("*")
# b = [i for i in b if i != "*"]
# for i in set(a):
#     a_dict[i]=a.count(i)
# check = "yes"
# for i in set(b):
#     if i in a:
#         if a_dict[i] >= b.count(i):
#             pass
#         else:
#             check = "no"
#             break
#     else:
#         check ="no"
#         break
# print("A" if check =="yes" else "N")

# while True:
#     a,b= wow()
#     if a==b==0:
#         break
#     n_list = list(wow())
#     cnt = 0
#     for _ in range(b):
#         count = 0
#         for x,y in zip(n_list,list(wow())):
#             if x>=y:
#                 count+=1
#         if count == a:
#             cnt+=1
#     print(cnt)
# cnt = 0
# for _ in range(one()):
#     a = inputing()
#     cnt+=a.count("A")*4
#     cnt+=a.count("K")*3
#     cnt+=a.count("Q")*2
#     cnt+=a.count("J")
# print(cnt)
    
# for index in range(1, one()+1):
#     a = inputing()
#     x,y = wow()
#     while max(x,y)>len(a):
#         a+=a
#     print(f"Case #{index}:",a[x-1:y].count("B"))
        
# for index in range(1,one()+1):
#     r = one()
#     n_dict = {}
#     for _ in range(r):
#         answer = inputing()
#         n_dict[answer]=len(set(answer.replace(" ","")))
#     list_list = sorted(list(n_dict.items()),key=lambda x : x[0])
#     list_list.sort(key=lambda x : x[1],reverse=True)
#     print(f"Case #{index}:",list_list[0][0])
         
    



