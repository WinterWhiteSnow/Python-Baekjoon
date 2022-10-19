import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1927
# import heapq
# h = []
# for _ in range(one()):
#     a = one()
#     if a == 0:
#         if h:
#             print(heapq.heappop(h))
#         else:
#             print(0)
#     else:
#         heapq.heappush(h,a)

#https://www.acmicpc.net/problem/11286
# import heapq
# h = []
# for _ in range(one()):
#     a = one()
#     if a == 0:
#         if h:
#             x,y = heapq.heappop(h)    
#             print(y)
#         else:
#             print(0)
#     else:
#         x,y = abs(a),a
#         r = [x,y]
#         heapq.heappush(h,r)

#https://www.acmicpc.net/problem/1904
# l = one()
# x,y = 1,2
# if l <=2:
#     print(l)
# else:
#     for _ in range(l-2):
#         x,y = y%15746,x+y%15746
#     print(y%15746)

#https://www.acmicpc.net/problem/14405
# n = inputing()
# for i in ["pi", "ka", "chu"]:
#     n = n.replace(i," ")
# print("YES" if set(list(n)) == {" "} else "NO")

#https://www.acmicpc.net/problem/8892
# for _ in range(one()):
#     k = one()
#     check = "no"
#     n_list = [inputing() for _ in range(k)]
#     for i in range(k-1):
#         for ii in range(i+1,k):
#             a = n_list[i]
#             b = n_list[ii]
#             if a+b == (a+b)[::-1]:
#                 print(a+b)
#                 check="yes"
#                 break
#             elif b+a == (b+a)[::-1]:
#                 print(b+a)
#                 check="yes"
#                 break
#         if check == "yes":
#             break
#     if check =="no":
#         print(0)

#https://www.acmicpc.net/problem/11637
# for _ in range(one()):
#     r = one()
#     n_list = [one() for _ in range(r)]
#     total = sum(n_list)
#     max_max = max(n_list)
#     if n_list.count(max_max) == 1:
#         if max_max/total >0.5:
#             a = "majority"
#         else:
#             a = "minority"
#         index = n_list.index(max_max)
#         print(f"{a} winner {index+1}")
#     else:
#         print("no winner")

#https://www.acmicpc.net/problem/6588
# n_dict = {}
# for i in range(2,1000000):
#     if i not in n_dict:
#         for a in range(i,1000000,i):
#             n_dict[a]=0
#         n_dict[i]=1
# while True:
#     a = one()
#     if a == 0:
#         break
#     check = "no"
#     for i in range(2,a//2+1):
#         x = n_dict[i]
#         if x == 1:
#             if n_dict[a-i] == 1:
#                 print(f"{a} = {i} + {a-i}")
#                 check ="yes"
#                 break
#     if check =="no":
#         print("Goldbach's conjecture is wrong.")
    
    






        
    
        



