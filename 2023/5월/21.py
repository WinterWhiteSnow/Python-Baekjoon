import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# https://www.acmicpc.net/problem/1052
# n,k = wow()
# cnt = bin(n).count("1")
# if k>=n:
#     print(0)
# else:
#     if cnt<=k:
#         print(0)
#     else:
#         b = list(bin(n)[2:])[::-1]
#         b = [int(i) for i in b]
#         count = 0
#         h = []
#         for i in range(len(b)):
#             if b[i]==1:
#                 h.append(2**i)  
#         h.sort(reverse=True)
#         while len(h) > k:
#             a,b = h.pop(),h.pop()
#             # print("now",a,b)
#             if a==b:
#                 h.append(a+b)
#             else:
#                 count+=min(a,b)
#                 h.append(min(a,b)*2)
#                 h.append(max(a,b))
#             h.sort(reverse=True)
#         print(count)
            
            
            
            

            













