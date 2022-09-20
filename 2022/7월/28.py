import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# a = one()
# min_min = "none"
# repeat = "no"
# for x in range(1,int((10**6)/3)+1):
#     for y in range(1,a//x+1):
#         for z in range(1,a//x+1):
#             if x*y*z > a:
#                 break
            
#             if x*y*z == a:
#                 index = 2*x*y+2*x*z+2*y*z
#                 if min_min == "none":
#                     min_min = index
#                 else:
#                     min_min = min(min_min,index)
# print(min_min)
# total = one()
# for index in range(1,total+1):
#     r = one()
#     price = [one() for _ in range(r-1)]
#     list_list =  [inputing() for _ in range(r)]
#     start = inputing()
#     end = inputing()
#     ss = list_list.index(start)
#     ee = list_list.index(end)
#     gap = abs(ss-ee)
#     print(f"Data Set {index}:")
#     print(price[gap-1])
#     if index != total:
#         print()

# for index in range(1,one()+1):
#     r,l = wow()
#     n_list = [list(wow())+[0,0] for _ in range(l)]
#     for i in n_list:
#         i[4]=i[0]
#     for _ in range(r):
#         a = one()
#         if n_list[a-1][2]>=1:
#             n_list[a-1][2]-=1
#             n_list[a-1][4]+=n_list[a-1][1]
#             n_list[a-1][5]+=n_list[a-1][3]
#     n_list = [i+1 for i in range(l) if n_list[i][4]<n_list[i][5]]
#     print(f"Data Set {index}:")
#     for i in n_list:
#         print(i)
#     print()

# for _ in range(one()):
#     n_list = list(wow())
#     r = n_list[0]
#     n_list = n_list[1:]
#     n_dict = {}
#     for i in range(len(n_list)):
#         if i%2:
#             if n_list[i] not in n_dict:
#                 n_dict[n_list[i]]=1
#             else:
#                 n_dict[n_list[i]]+=1
#     print(max(n_dict.values()))

# a =oct(int(inputing(),16))
# print(a[2:])

# a,b = wow()
# c = str(a**b)
# for i in range(0,len(c),70):
#     print(c[i:i+70])
# import string
# a_list = list(string.ascii_uppercase)
# n_dict = {}
# dict_n = {}
# for i in range(len(a_list)):
#     n_dict[a_list[i]]=i
#     dict_n[i]=a_list[i]
# k = one()
# a = list(inputing())
# ind = 1
# for i in a:
#     index = n_dict[i]-(3*ind+k)
#     now = index%26
#     print(dict_n[now],end="")
#     ind+=1

# a = one()
# b = a+1
# while len(set(str(b))) != len(list(str(b))):
#     b+=1
# print(b)

# set_list = set(sorted(["I", "O", "S", "H", "Z", "X", "N"]))
# answer = set(sorted(list(inputing())))
# cnt = 0
# for i in answer:
#     if i in set_list:
#         cnt+=1
# if cnt == len(answer):
#     print("YES") 
# else:
#     print("NO")      

for _ in range(one()):
    cnt = 1
    a,b=wow()
    for i in range(1,a+1):
        cnt*=i
    print(str(cnt).count(str(b)))
       

                    
                    





