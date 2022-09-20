import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# def recursion(s, l, r, cnt):
#     cnt+=1
#     if l >= r: return 1,cnt
#     elif s[l] != s[r]: return 0,cnt
#     else: return recursion(s, l+1, r-1,cnt)

# def isPalindrome(s):
#     return recursion(s, 0, len(s)-1,0)

# for _ in range(one()):
#     print(*isPalindrome(inputing()))
# import itertools
# l = one()
# n_list = list(wow())
# new_list = list(itertools.permutations(n_list,r=3))
# check = "yes"    
# for i in new_list:
#     x,y,z = i
#     r = (x-y)/z
#     if r == int(r):
#         pass
#     else:
#         check="no"
#         break
# print("yes" if check=="yes" else "no")

# n_list = [inputing().split()[::-1][:-1] for _ in range(one())]
# n_list.sort(key=lambda x : len(x))
# print(len(n_list[-1]))
# for i in n_list[-1]:
#     print(i)

# num,l = wow()
# n_list = set(list(wow()))
# nn_list = set([i for i in range(1,1+num)])
# nnn_list = sorted(list(nn_list-n_list))
# print(*nnn_list if len(nnn_list) != 0 else "*")
# n_dict = {}
# r = one()
# location = list(wow())
# l = one()
# r_list = list(wow())
# for index in r_list:
#     if location[index-1]+1 in location:
#         pass
#     else:
#         location[index-1]+=1
#         location[index-1]=min(location[index-1],2019)
# print(*location,sep="\n")

# n,k = wow()
# cnt = 1
# for _ in range(n):
#     cnt*=one()
#     cnt%=2**k
# print(1 if cnt%2**k == 0 else 0)

# n_list = list(wow())
# n_list = n_list[1:]
# cnt = 0
# for _ in range(one()):
#     nn_list = list(wow())[1:]
#     count = 0
#     for i in nn_list:
#         if i in n_list:
#             count+=1
#     if count == 0:
#         cnt+=1
# print(cnt)

# num = one()/52
# index = 6*7//2
# n_list = []
# for x in range(1,101):
#     for y in range(1,101):
#         if 7*x+index*y == num:
#             n_list.append([x,y])
# n_list.sort(key= lambda x : x[1])
# n_list.sort(key= lambda x : x[0],reverse=True)
# print(*n_list[0],sep="\n")

# while True:
#     a = inputing()
#     if a == "#":
#         break
#     a,b,c = a.split()
#     n_list = list(b)
#     a,b,c,d = n_list 
#     if a==b and c==d:
#         if b != c:
#             print(f"{a} {a} glued and {c} {c} glued")     
#         else:
#             print(f"{a} {a} glued")     
#     else:
#         if a==b:
#             print(f"{a} {a} glued")
#         elif b==c:
#             print(f"{b} {b} glued")
#         elif c==d:
#             print(f"{c} {c} glued")
#         else:
#             pass

l = one()
n_list = list(wow())
max_max = max(n_list)
a = n_list[0:n_list.index(max_max)]
b = n_list[n_list.index(max_max)+1:]
print(0 if len(a) == 0 else sum(a))
print(0 if len(b) == 0 else sum(b))

    
    





