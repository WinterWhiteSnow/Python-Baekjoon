import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1544
# n_dict = {}
# for _ in range(one()):
#     if len(n_dict) == 0:
#         n_dict[inputing()]=1
#     else:
#         a = inputing()
#         check = "no"
#         for i in range(1,len(a)):
#             b = a[i:]+a[:i]
#             if b in n_dict:
#                 n_dict[b]+=1
#                 check="yes"
#                 break
#         if check == "no":
#             n_dict[a]=1
# print(len(n_dict))


#https://www.acmicpc.net/problem/12873
# n_list = [i for i in range(1,one()+1)]
# index = 1
# location = "none"
# while len(n_list) != 1:
#     cnt = ((index**3)%len(n_list))-1
#     if location == "none":
#         location = cnt
#     else:
#         cnt+=location
#         cnt%=len(n_list)
#     del n_list[cnt]
#     location=cnt
#     # print(n_list,cnt,location)
#     index+=1
# print(n_list[0])

#https://www.acmicpc.net/problem/1590
# import math
# r,t = wow()
# min_min = 1000001
# for _ in range(r):
#     start,gap,c = wow()
#     if t>start:
#         a = math.ceil(abs(t-start)/gap)
#         if a<=c-1:
#             min_min=min(min_min,(start+gap*a)-t)
#     else:
#         min_min=min(min_min,abs(start-t))
# print(min_min if min_min != 1000001 else -1)

#https://www.acmicpc.net/problem/14382
# ind = 1
# for _ in range(one()):
#     a = one()
#     if a == 0:
#         print(f"Case #{ind}: INSOMNIA")
#     else:
#         str_str = {}
#         for i in str(a):
#             str_str[i]=1
#         index= 2
#         while len(str_str) != 10:
#             num = a*index
#             for i in str(num):
#                 str_str[i]=1
#             index+=1
#         print(f"Case #{ind}: {num}")
#     ind+=1

#https://www.acmicpc.net/problem/5766
# while True:
#     n_dict={}
#     r,l = wow()
#     if r==l==0:
#         break
#     for _ in range(r):
#         n_list = list(wow())
#         for i in n_list:
#             if i not in n_dict:
#                 n_dict[i]=1
#             else:
#                 n_dict[i]+=1
#     second = list(set(sorted(n_dict.values())))[-2]
#     list_list = [a for a,b in n_dict.items() if b == second]
#     print(*sorted(list_list))

#https://www.acmicpc.net/problem/20125
# r = one()
# index = "none"
# waist ="no"
# start_i = "none"
# waist_cnt = 0
# ll,rr =0,0
# for i in range(r):
#     a = inputing()
#     if index == "none":
#         if "*" in a:
#             index = a.index("*")    
#             x,y = i+2,index+1
#             start_i =i+1
#         else:
#             continue
#     if waist == "yes":
#         if "*" in a:
#             if a.index("*") == index:
#                 waist_cnt+=1
#             else:
#                 if a[index-1] == "*":
#                     ll+=1
#                 if a[index+1]=="*":
#                     rr+=1
#         else:
#             continue
#     if type(start_i) == int and i == start_i:
#         cnt = a.count("*")
#         l_a= len(a[a.index("*"):index])
#         r_a= cnt-l_a-1
#         waist = "yes"

# print(x,y)
# print(l_a,r_a,waist_cnt,ll,rr)


        
        





