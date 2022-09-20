import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# for _ in range(one()):
#     a = inputing()
#     n_list = list(map(float,inputing().split()))
#     b = inputing()
#     m_list = list(map(float,inputing().split()))
#     cnt = 0
#     for x,y in zip(m_list,n_list):
#         cnt+=(x-y)**2
#     cnt = cnt**(1/2)
#     print(f"{a} to {b}: {cnt:.2f}")

# for _ in range(one()):
#     a = inputing()
#     b = a
#     list_list = [a]
#     while True:
#         c =a[1:]+a[0]
#         if c not in list_list:
#             list_list.append(c)
#         else:
#             break
#         a=c
#     print(sorted(list_list)[0])

# a,b,c = wow()
# n_list = [0]*(a+1)
# n_dict = {}
# for _ in range(b):
#     x,y,z = inputing().split()
#     n_dict[x]=[int(y),int(z)]
# for _ in range(c):
#     name = inputing()
#     start = n_dict[name][0]
#     step = n_dict[name][1]
#     for i in range((a-start)//step+1):
#         n_list[start+step*i]= not n_list[start+step*i]
# print(n_list[1:].count(True))

# for _ in range(one()):
#     a = inputing().split()
#     l = int(a[0])
#     cnt = 0
#     count = 0
#     for i in a[1:]:
#         if i == "X":
#             count+=1
#         else:
#             cnt = max(cnt,count)
#             count=0
#     cnt = max(cnt,count)
#     print(f"The longest contiguous subsequence of X's is of length {cnt}")

# a = inputing()
# set_list = set(list(a))
# n_dict = {}
# for i in set_list:
#     n_dict[i]=a.count(i)
# n_list = sorted([b for a,b in list(n_dict.items()) if b%2])
# if len(n_list) > 0:
#     print(len(n_list)-1)
# else:
#     print(0)

# a = list(inputing())
# b = ["p","e","r"]
# index = 0
# cnt = 0
# for i in a:
#     if i.lower() == b[index]:
#         pass
#     else:
#         cnt+=1
#     index+=1
#     index%=3
# print(cnt)

# import string
# str_str = list(string.ascii_lowercase)
# while True:
#     a,b,c = wow()
#     if a==b==c==0:
#         break
#     n_list = list(inputing())
#     index = (a+b+c)%25+1
#     for i in n_list:
#         if i in str_str:
#             print(str_str[(str_str.index(i)-index)],end="")
#         else:
#             print(i,end="")
#     print()

# r = one()
# for i in range(r):
#     if i == 0:
#         pass
#     else:
#         input()
#     l = one()
#     n_list = list(wow())
#     n_dict= {}
#     for index in range(0,len(n_list),2):
#         nn_list = [a for a in range(n_list[index],n_list[index+1]+1)]
#         for x in nn_list:
#             if x not in n_dict:
#                 n_dict[x]=1
#             else:
#                 n_dict[x]+=1
#     i = i+1
#     print(f"Case #{i}: ",end="")
#     for _ in range(one()):
#         x = one()
#         if x in n_dict:
#             print(n_dict[x],end=" ")
#         else:
#             print(0,end=" ")
#     print()
import string
str_str = list(string.ascii_lowercase)
a = list(inputing())
b = list(inputing())
for x,y in zip(a,b):
    if x in str_str:
        print(str_str.index(x)-str_str.index(y))
        
