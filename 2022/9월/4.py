import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# n,k,i,l = wow()
# start = n-k+1
# cnt = 0
# count = 1
# for _ in range(l):
#     if i<=count<=l:
#         cnt+=start
#     start+=1
#     if start > n:
#         start-=n
#     count+=1
# print(cnt)

# for index in range(1,one()+1):
#     l = one()
#     n_list = list(wow())
#     check = "no"
#     for a in range(l-2):
#         for b in range(a+1,l-1):
#             for c in range(b+1,l):
#                 if abs(n_list[a]-n_list[b]) == abs(n_list[b]-n_list[c]):
#                     if n_list[a] != 0 and n_list[b] != 0 and n_list[c] !=0:
#                         check = "yes"
#                         break
#             if check == "yes":
#                 break
#         if check == "yes":
#             break
#     print(f"Case #{index}:","YES" if check == "no" else "NO")

# for _ in range(one()):
#     a = inputing().split()
#     cnt = 0
#     l = len(a)
#     for i in range(l):
#         if a[i] == "u" or a[i] == "ur":
#             cnt+=10
#         if "lol" in a[i]:
#             cnt+=10
#         if a[i] == "should" or a[i] == "would":
#             if i == l-1:
#                 pass
#             else:
#                 if a[i+1] == "of":
#                     cnt+=10
#     print(cnt)

while True:
    a,b,c,d= wow()
    if a==b==c==d==-1:
        break
    n_list = [a,b,c,d]
    
    
    

    




                










