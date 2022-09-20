import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())


# for _ in range(one()):
#     n_list = list(inputing())
#     state = "none"
#     cnt = 0
#     for i in n_list:
#         if state == "none":
#             state = i
#             cnt = 1
#         else:
#             if state == i:
#                 cnt+=1
#             else:
#                 print(cnt,state,end=" ")
#                 state = i
#                 cnt=1
#     print(cnt,state)

# n_list = "aeiou"
# for _ in range(one()):
#     a = inputing()
#     b = list(a)
#     cnt = 0
#     for i in a:
#         if i in n_list:
#             cnt+=1
#     print(f"The number of vowels in {a} is {cnt}.")

# while True:
#     a,b = inputing().split()
#     if a==b=="0":
#         break
#     b = b.replace(a,"")
#     if b == "":
#         b = 0
#     print(int(b))

# l = one()
# n_list = inputing().split()
# cnt = 0
# for i in n_list:
#     if i == i[::-1]:
#         cnt+=int(i)
# print(cnt)

# l = one()
# n_list = list(wow())
# print("yes" if n_list == sorted(n_list) else "no")

# a,b = wow()
# for i in range(a,b+1):
#     x = str(i)
#     if x == x[::-1]:
#         print("Palindrome!")
#     else:
#         print(x)

# n_list = inputing()
# print("Canadian!" if n_list[-len("eh?"):] == "eh?" else "Imposter!")

# import string
# str_str = list(string.ascii_lowercase)
# a = inputing()
# for i in str_str:
#     a=a.replace(i," ")
# print(len(list(set(a.split()))))

# a = inputing()
# if len(a)>=2:
#     b = int(a)
#     print(round(b,-(len(a)-1)))
# else:
#     print(a)
# r = one()
# for index in range(1,r+1):
#     r,l = wow()
#     n_dict = {}
#     for _ in range(r):
#         n_list = list(inputing())
#         for ll in range(l):
#             if ll not in n_dict:
#                 n_dict[ll]=[n_list[ll]]
#             else:
#                 n_dict[ll]+=[n_list[ll]]
#     a_list = []
#     for i in range(l):
#         a = n_dict[i]
#         if "X" in a:
#             ind = a.index("X")
#             cnt = 0
#             for x in range(ind):
#                 cnt+=3 if a[x] == "H" else 1
#             a_list.append(cnt)
#         else:
#             a_list.append("N")
#     if index != 1:
#         print()
#     print(f"Data Set {index}:")
#     print(*a_list)

# a = inputing()
# cnt = 1
# for i in list(a):
#     if i == "T":
#         cnt*=2
#     if i == "D":
#         cnt*=2
#     if i == "F" or i == "L":
#         cnt*=2
# print(cnt)

# max_l = 0
# n_list = []
# for i in sys.stdin.readlines():
#     max_l = max(max_l,len(i.rstrip()))
#     n_list.append(i.rstrip())
# cnt = 0
# n_list = n_list[:-1]
# for i in n_list:
#     cnt+=(max_l-len(i))**2
# print(cnt)

# import math
# r,l = wow()
# total = r*l
# for i in range(10,90+1,10):
#     print(math.ceil(total*(i/100)),end=" ")

# n_list = [inputing() for _ in range(one())]
# n_dict = {}
# for i in n_list:
#     n_dict[i]=len(list(set(list(i))))
# new_list = sorted(list(n_dict.items()),key=lambda x : x[1],reverse=True)
# print(new_list[0][1])

# l = one()
# n_list = inputing().split()
# m_list = []
# for i in n_list:
#     now = i
#     str_str = ""
#     l = len(now)
#     check = "no"
#     for index in range(len(now)-2):
#         if now[index] in "eioauy":
#             if now[index+1] not in "eioauy":
#                 if now[index+2] not in "eioauy":
#                     pass
#                 else:
#                     str_str+=now[index]
#             else:
#                 str_str+=now[index]
#         else:
#             str_str+=now[index]
#     str_str+=now[-2:]
#     m_list.append(str_str[::-1])
# m_list = m_list[::-1]
# print(*m_list)

# n_list = [one() for _ in range(one())]
# n_list.sort()
# cnt = sum(n_list)/2
# print(int(cnt) if cnt in n_list else "BAD")











