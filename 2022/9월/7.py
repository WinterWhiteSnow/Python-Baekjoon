import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# a,b = wow()
# count=0
# for i in range(a,b+1):
#     num = list(str(i))
#     set_num = set(num)
#     if "0" not in set_num:
#         if len(list(set_num))==6:
#             cnt = 0
#             for s in set_num:
#                 if i%int(s)==0:
#                     cnt+=1
#             if cnt == 6:
#                 count+=1
# print(count)

# for _ in range(one()):
#     n_dict = {}
#     r = one()
#     for _ in range(r):
#         a,b=wow()
#         if b not in n_dict:
#             n_dict[b]=a
#         else:
#             n_dict[b]=max(a,n_dict[b])    
#     key_list = sorted(n_dict.keys())
#     if key_list == [i for i in range(1,11)]:
#         print(sum(list(n_dict.values())))
#     else:
#         print("MOREPROBLEMS")

# a = [i for i in list(inputing()) if i in "aeiou"]
# b = a[::-1]
# print("S" if a==b else "N")

# while True:
#     l = one()
#     if l == 0:
#         break
#     n_list = list(wow())
#     cnt = 0
#     for i in range(l-1,-1,-1):
#         cnt+=n_list[i]
#         for k in range(0,i):
#             n_list[k]+=n_list[i]
#     print(cnt)

str_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    a= inputing()
    if a == "0":
        break
    a,b = a.split()
    a = int(a)
    new_str = ""
    for i in b:
        index = (str_str.index(i)+a)%len(str_str)
        new_str+=str_str[index]
    print(new_str[::-1])



