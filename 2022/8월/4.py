import sys


inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# 오늘도 38문제

# for _ in range(one()):
#     l = one()
#     n_list = list(wow())
#     cnt = 0
#     for a in range(1,l):
#         for b in range(a):
#             if n_list[a] >= n_list[b]:
#                 cnt+=1
#     print(cnt)
# n_dict={"C":12.01,"H":1.008,"O":16.00,"N":14.01}

# for _ in range(one()):
#     a = inputing()
#     num = ""
#     now = "none"
#     cnt = 0
#     for i in list(a):
#         if i in n_dict:
#             if now == "none":
#                 now = i
#             else:
#                 cnt+=n_dict[now]*int(num) if num != "" else n_dict[now]
#                 num = ""
#                 now = i
#         else:
#             num+=i
#         # print(num,now,cnt)
#     if now != "none":
#         cnt+=n_dict[now]*int(num) if num != "" else n_dict[now]
#     print(f"{cnt:.3f}")

# for index in range(1,one()+1):
#     a = inputing()
#     b = inputing()
#     print(f"Case {index}: {b}, {a}")

# for i in sys.stdin.readlines():
#     a,b = i.split("+")
#     b,c = b.split("=")
#     l = max(len(a),len(b))
#     a = a[::-1]
#     b = b[::-1]
#     # print(a,b)
#     cnt = int(a)+int(b)
#     print(cnt==int(c[::-1]))

# while True:
#     a = inputing().split()
#     if a[0] == "#":
#         break
    
#     for i in range(len(a)):
#         b = list(a[i])
#         b[1:-1] = b[1:-1][::-1]
#         a[i] = "".join(b)
#     print(*a)

# while True:
#     r = one()
#     if r == 0:
#         break
#     n_list = []
#     for _ in range(r):
#         a,b= inputing().split("-")
#         a = int(a.split(":")[0])*60*60+int(a.split(":")[1])*60
#         b = int(b.split(":")[0])*60*60+int(b.split(":")[1])*60
#         n_list.append([a,b])
#     n_list = sorted(n_list,key=lambda x : x[0])
#     conflict = "no"
#     for i in range(r-1):
#         if n_list[i][1]<= n_list[i+1][0]:
#             pass
#         else:
#             conflict = "yes"
#     if conflict =="yes":
#         print("conflict")
#     else:
#         print("no conflict")

# l = one()
# n_list = list(wow())
# total = 15000
# n_dict = {}
# for i in n_list:
#     n_dict[i]=1
# print(total-len(list(n_dict.keys())))

# import math
# l = one()
# n_list = inputing().replace(" ","")
# right_zero = n_list.find("0")
# right_one = n_list.find("1")
# left_zero = n_list.rfind("0")
# left_one = n_list.rfind("1")
# gap = max(abs(right_one-right_zero),abs(right_one-left_zero),abs(left_one-left_zero),abs(left_one-right_zero))
# print(gap)
    
# for _ in range(one()):
#     a,b= inputing().split()
#     x = set(sorted(list(a)))
#     y = set(sorted(list(b)))
#     if x==y:
#         print("YES")
#     else:
#         print("NO")
import math
a,b = wow()
print(math.gcd(a,b))










