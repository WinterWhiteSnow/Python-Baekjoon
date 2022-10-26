import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/18265
# a = [1, 2, 3, 1, 3, 2]
# b = [1, 2, 1, 2, 3, 1, 3, 2]
# num = one()
# if num == 1:
#     print(1)
# if num <= len(a)+1:
#     print(1+sum(a[:num-1]))
# else:
#     start = 1+sum(a)
#     index = num-7
#     repeat = index//len(b)
#     remainder = index%len(b)
#     print(start+sum(b)*repeat+sum(b[:remainder]))
#[1, 2, 4, 7, 8, 11, 13, 14, 16, 17, 19, 22, 23, 26, 28, 29, 31, 32, 34, 37, 38, 41, 43, 44, 46, 47, 49, 52, 53, 56, 58, 59, 61, 62, 64, 67, 68, 71, 73, 74, 
#76, 77, 79, 82, 83, 86, 88, 89, 91, 92, 94, 97, 98]

#https://www.acmicpc.net/problem/12034
# index = 1
# for _ in range(one()):
#     l = one()
#     list_list = list(wow())
#     wow_list = list_list
#     n_list = []
#     for i in list_list:
#         if i%4 != 0:
#             n_list.append(i)
#             del wow_list[wow_list.index((i/0.75))]
#         elif i%4 == 0 and i/0.75 in wow_list:
#             n_list.append(i)
#             del wow_list[wow_list.index((i/0.75))]
#         # print(i,i%4,i/0.75)
#     print(f"Case #{index}:",*n_list)
#     index+=1

#https://www.acmicpc.net/problem/13133
# r = one()
# n_list = [list(wow()) for _ in range(r)]
# l = one()
# m_list = list(wow())
# list_list = []
# for i in range(1,r+1):
#     if i not in m_list:
#         a,b = n_list[i-1]
#         if a not in m_list and b not in m_list:
#             if a != 0 and b !=0:
#                 list_list.append(i)
# print(len(list_list))

#https://www.acmicpc.net/problem/7596
# index = 1
# while True:
#     r = one()
#     if r == 0:
#         break
#     n_list = [inputing() for _ in range(r)]
#     n_list.sort()
#     print(index)
#     for i in n_list:
#         print(i)
#     index+=1

#https://www.acmicpc.net/problem/25631
# l = one()
# n_list = list(wow())
# set_list = set(n_list)
# max_max = 0
# for i in set_list:
#     max_max=max(max_max,n_list.count(i))
# print(max_max)        

#윗층 진짜 짜증난다 다리를 문질러버릴수도없고
#발망치충 제발 멈춰

#https://www.acmicpc.net/problem/9733
# a = "Re,Pt,Cc,Ea,Tb,Cm,Ex".split(",")
# n_dict = {}
# for i in a:
#     n_dict[i]=0
# n_list = []
# total = 0
# for i in sys.stdin.readlines():
#     i = i.split()
#     for b in i:
#         if b in n_dict:
#             n_dict[b]+=1
#     total+=len(i)
# for i in "Re,Pt,Cc,Ea,Tb,Cm,Ex".split(","):
#     answer = round(n_dict[i]/total,2)
#     print(i,n_dict[i],f"{answer:.2f}")
# print(f"Total {total} 1.00")

#https://www.acmicpc.net/problem/23246
# r = one()
# n_list = []
# for _ in range(r):
#     a,b,c,d = wow()
#     cnt = b*c*d
#     grades = b+c+d
#     n_list.append([a,b,c,d,cnt,grades])
# n_list.sort(key=lambda x: x[0])
# n_list.sort(key=lambda x: x[5])
# n_list.sort(key=lambda x: x[4])
# n_list = [i[0] for i in n_list]
# print(*n_list[:3])


r,l = wow()
u,l,r,d = wow()
for i in range(u):
    if i%2 == 0:
        print("#."*l)
    else:
        print(".#"*l)
for i in range(r):
    if i%2==0:
        pass
    






        









