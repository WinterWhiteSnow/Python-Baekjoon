import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# 35문제

# for index in range(1,1+one()):
#     num = one()
#     new_num = int("1"*len(str(num)))
#     if new_num > num:
#         new_num = int("9"*(len(str(num))-1))
#         print(f"Case #{index}:",new_num)
#     else:
#         max_max = new_num
#         for i in range(max_max+1,num+1):
#             if list(str(i)) == sorted(list(str(i))):
#                 max_max=max(max_max,i)
#                 # print(max_max)
#         print(f"Case #{index}:",max_max)

# r,k = wow()
# n_list = [one() for _ in range(r)]
# start = 0
# end = (sum(n_list)+k)//len(n_list)
# while start<=end:
#     mid = (start+end)//2
#     cnt = 0
#     for i in n_list:
#         if i<mid:
#             cnt+=mid-i
#     if cnt == k:
#         end= mid
#         break
#     else:
#         if cnt <k:
#             start=mid+1
#         else:
#             end=mid-1
# print(end)
# while True:
#     a,b= wow()
#     if a==b==0:
#         break
#     max_max = 0
#     n_list = list(wow())
#     for x in range(a-1):
#         for y in range(x+1,a):
#             if n_list[x]+n_list[y] <= b:
#                 max_max=max(max_max,n_list[x]+n_list[y])
#     print(max_max if max_max != 0 else "NONE")

# l = one()
# n_list = list(wow())
# total = one()
# gap = total
# now = 0
# for i in n_list:
#     if total%i < gap:
#         gap = total%i
#         now = i
# print(now)

# a = one()
# b = a+1
# while "0" in str(b):
#     b+=1
# print(b) 

# l,limit = wow()
# n_list= list(wow())
# cnt = 1
# now = 0
# for i in n_list:
#     if i+now <=limit:
#         now+=i
#     else:
#         now=i
#         cnt+=1
# print(cnt)

# a = list(inputing().upper())
# x = 0
# y = 0
# for i in a:
#     x+="KANGAROO".count(i)
#     y+="KIWIBIRD".count(i)
# if x > y:
#     print("Kangaroos")
# elif x == y:
#     print("Feud continues")
# else:
#     print("Kiwis")
# import string
# a_list = list(string.ascii_uppercase)
# n_dict = {}
# a = inputing().replace(" ","").upper()
# for i in a_list:
#     n_dict[i]=a.count(i)
# for x,y in n_dict.items():
#     print(f"{x} |","*"*y)
# r = one()
# for index in range(1,r+1):
#     a,b = wow()
#     c_list = list(wow())
#     list_list = list(wow())
#     for i in list_list:
#         c_list[i-1]-=1
#     print(f"Data Set {index}:")
#     print(max(c_list))
#     if index != r:
#         print()

a = inputing()
if "ss" in a:
    print("hiss")
else:print("no hiss")
    








