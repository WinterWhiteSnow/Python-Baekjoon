import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/2816
# n = one()
# n_list = [inputing() for _ in range(n)]
# index = 0
# index_list = []
# for i in range(n):
#     if n_list[i] == "KBS1":
#         for _ in range(i):
#             index_list.append(1)
#         for _ in range(i):
#             index_list.append(4)
# n_list.remove("KBS1")
# n_list = ["KBS1"]+n_list
# # print(n_list)
# for i in range(n):
#     if n_list[i] == "KBS2":
#         for _ in range(i):
#             index_list.append(1)
#         for _ in range(i-1):
#             index_list.append(4)
# print(*index_list,sep="")

#https://www.acmicpc.net/problem/3154
# a,b = map(int,inputing().split(":"))
# h = []
# for i in range((99-a)//24+1):
#     index = a+24*i
#     if index < 10:
#         index = "0"+str(index)
#     else:
#         index =str(index)
#     h.append(index)
# m = []
# if b < 10:
#     m.append("0"+str(b))
# else:
#     m.append(str(b))
# if b+60 < 100:
#     m.append(str(b+60))
# move = [(3,1),(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
# index_list = []
# for hh in h:
#     for mm in m:
#         total_str = hh+mm
#         d = 0
#         for i in range(3):
#             q,w = total_str[i],total_str[i+1]
#             q,w = int(q),int(w)
#             y,x = move[q]
#             yy,xx = move[w]
#             d+=abs(x-xx)+abs(y-yy)
#             # print(total_str,q,w)
#         index_list.append((hh,mm,d))
# index_list.sort(key=lambda x : (x[2],x[0],x[1]))
# print(*index_list[0][:-1],sep=":")

#https://www.acmicpc.net/problem/3230
# a,b = wow()        
# index_list = []
# for i in range(a):
#     index = one()
#     index_list.insert(index-1,i+1)
# # print(index_list)
# total = []
# for index in index_list[:b][::-1]:
#     final = one()
#     total.insert(final-1,index)
# # total.sort(key=lambda x: (x[1],x[2]))
# print(*total[:3],sep="\n")

#https://www.acmicpc.net/problem/10275
# for _ in range(one()):
#     n,a,b = wow()
#     print(n-(bin(min(a,b))[::-1]).index("1"))

#https://www.acmicpc.net/problem/19945
# number =one()
# print(bin(number))

#https://www.acmicpc.net/problem/22113
# n,m = wow()
# m_list = list(wow())
# n_list = [list(wow()) for _ in range(n)]
# y,x=0,0
# cnt = 0
# for i in range(m-1):
#     a,b = m_list[i]-1,m_list[i+1]-1
#     # print(a,b)
#     cnt+=n_list[a][b]
# print(cnt)

#https://www.acmicpc.net/problem/20977
# l = one()
# j = []
# i = []
# o = []
# str_str = inputing()
# for index in range(l):
#     if str_str[index] == "J":
#         j.append("J")
#     elif str_str[index]=="O":
#         o.append("O")
#     else:
#         i.append("I")
# print(*j+o+i,sep="")

#https://www.acmicpc.net/problem/18125
# r,l = wow()
# n_list = [list(wow()) for _ in range(l)]
# m_list = [list(wow()) for _ in range(r)]
# index = 0
# state = True
# for x in range(r):
#     list_list = []
#     for y in range(l):
#         # print(y,x)
#         list_list.append(n_list[y][x])
#     list_list = list_list[::-1]
#     # print(list_list)
#     if list_list == m_list[index]:
#         index+=1
#     else:
#         state =False
#         break
#     if state == False:
#         break
# if state:
#     print("""|>___/|        /}
# | O < |       / }
# (==0==)------/ }
# | ^  _____    |
# |_|_/     ||__|""")
# else:
#     print('''|>___/|     /}
# | O O |    / }
# ( =0= )""""  \\
# | ^  ____    |
# |_|_/    ||__|''')

#https://www.acmicpc.net/problem/25371
# n,k = wow()
# n_list = []
# while n != 0:
#     n_list.append(n%k)
#     n//=k
# n_list = n_list[::-1]
# str_str = "".join(list(map(str,n_list)))
# a = str_str.split("0")
# cnt = 0
# for i in a:
#     if i != "":
#         cnt+=int(i)
# list_list = []
# while cnt != 0:
#     list_list.append(cnt%k)
#     cnt//=k
# print(*list_list[::-1],sep="")

#https://www.acmicpc.net/problem/6942
# count = 0
# for i in range(one(),one()+1):
#     state = True
#     for ii in str(i):
#         if ii in ["0","1","8","6","9"]:
#             continue
#         state=False
#     if state:
#         num = list(str(i))[::-1]
#         for index in range(len(num)):
#             if num[index]== "6":
#                 num[index]="9"
#             elif num[index] == "9":
#                 num[index]="6"
#         # print(i,num,int("".join(num)),i==int("".join(num)))
#         if i==int("".join(num)):
#             count+=1
# print(count)

                 








    
        





