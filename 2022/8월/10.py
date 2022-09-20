import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#35

# n_list = list(wow())
# first = 0
# second = 0
# for i in range(len(n_list)):
#     if n_list[i] != 0:
#         if first == 0:
#             first = i
#         else:
#             second = i
# check = (n_list[first]-n_list[second])/(first-second)
# if check == int(check):
#     for i in range(first+1,len(n_list)):
#         n_list[i]=n_list[i-1]+int(check)
#     for i in range(first-1,-1,-1):
#         n_list[i]=n_list[i+1]-int(check)
#     print(*n_list)
# else:
#     print(-1)

# n_list = sorted([one() for i in range(one())])
# cnt = 0
# for i in range(len(n_list)-1):
#     cnt+=(n_list[i+1]-n_list[i])**2
# print(cnt)
# r = one()
# for index in range(1,r+1):
#     a,b = wow()
#     n_dict = {}
#     cnt = 0
#     for ii in range(1,a+1):
#         x,y = wow()
#         if x == 1:
#             n_dict[ii]=-y
#         else:
#             n_dict[ii]=y
#     for _ in range(b):
#         q,w,e = wow()
#         if e == 0:
#             if n_dict[q] < 0:
#                 cnt+=abs(n_dict[q])
#             if n_dict[w] < 0:
#                 cnt+=abs(n_dict[w])
#         elif e == 1:
#             if n_dict[q] < 0:
#                 cnt+=abs(n_dict[q])
#             else:
#                 cnt+=n_dict[q]
#             if n_dict[w] < 0:
#                 cnt+=abs(n_dict[w])
#         else:
#             if n_dict[q] < 0:
#                 cnt+=abs(n_dict[q])
#             if n_dict[w] < 0:
#                 cnt+=abs(n_dict[w])
#             else:
#                 cnt+=n_dict[w]            
#     print(f"Data Set {index}:")
#     print(cnt)  
#     if index != r:
#         print()    

# while True:
#     a = inputing()
#     if a == '#':
#         break
#     b = list(map(int,list(a)[::-1]))
#     index = 2
#     cnt = 0
#     for i in b:
#         cnt+=i*index
#         index+=1
#     answer = 11-(cnt%11)
#     if answer == 10:
#         answer = "Rejected"
#     elif answer == 11:
#         answer = "0"
#     print(a,"->",answer)

# r = one()
# for _ in range(r):
#     a = inputing()
#     if a == a[::-1]:
#         print(1)
#     else:
#         print(2)

# while True:
#     a = inputing()
#     if a == "0":
#         break
#     index = 1
#     a = list(map(int,list(a)[::-1]))
#     cnt = 0
#     for i in a:
#         cnt+=i*(2**index-1)
#         index+=1
#     print(cnt)
# n_dict= {}
# for _ in range(one()):
#     name,a,aa,b,bb,c,cc,d,dd =inputing().split()
#     a,aa,b,bb,c,cc,d,dd = int(a),int(aa),int(b),int(bb),int(c),int(cc),int(d),int(dd)
#     solve = 0
#     penalty = 0
#     for x,y in zip([a,b,c,d],[aa,bb,cc,dd]):
#         if y != 0:
#             solve+=1
#             penalty+=y if x == 1 else y+(x-1)*20
#     n_dict[name]=[solve,penalty]
# list_list = sorted(list(n_dict.items()),key=lambda x : x[1][1])
# list_list.sort(key=lambda x : x[1][0],reverse=True)       
# a = list_list[0]
# print(a[0],*a[1])

# start,r = wow()
# cnt = 0
# for i in range(start+1,100):
#     if int(str(2**i)[0]) == r:
#         cnt = i
#         break
# print(cnt)
# import string
# a_list = list(string.ascii_uppercase)
# n_list = ['3', '2', '1', '2', '4', '3', '1', '3', '1', '1', '3', '1', '3', '2', '1', '2', '2', '2', '1', 
# '2', '1', '1', '1', '2', '2', '1']
# n_dict = {}
# for a,b in zip(a_list,n_list):
#     n_dict[a]=int(b)
# l_x,l_y = wow()
# x,y = inputing().split()
# min_l = min(len(x),len(y))
# max_l = max(len(x),len(y))
# str_str = ""
# for xx,yy in zip(list(x),list(y)):
#     str_str+=xx+yy
# if l_x>l_y:
#     str_str+=x[min_l:]
# else:
#     str_str+=y[min_l:]
# str_str = list(str_str)
# list_list = []
# for i in str_str:
#     list_list.append(n_dict[i])
# while True:
#     new_list = []
#     for i in range(len(list_list)-1):
#         new_list.append((list_list[i+1]+list_list[i])%10)
#     if len(new_list) == 2:
#         break
#     else:
#         list_list=new_list
# ss = ""
# for i in new_list:
#     ss+=str(i)
# ss = int(ss)
# print(f"{ss}%")
a,b= wow()
n_list = []
for _ in range(a):
    list_list = list(wow())
    new_list = []
    for i in list_list:
        new_list+=[i]*b
    for _ in range(b):
        n_list.append(new_list)
for i in n_list:
    print(*i)

