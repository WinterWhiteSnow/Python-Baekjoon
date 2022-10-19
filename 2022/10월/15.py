import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/2993
# a = list(inputing())
# str_list=[]
# for x in range(1,len(a)-1):
#     for y in range(x+1,len(a)):
#         z = len(a)
#         aa,bb,cc = a[:x],a[x:y],a[y:z]
#         aa=aa[::-1]
#         bb=bb[::-1]
#         cc=cc[::-1]
#         answer = "".join(aa+bb+cc)
#         str_list.append(answer)
# str_list.sort()
# print(str_list[0])

#https://www.acmicpc.net/problem/2714
# import string
# a_list = list(string.ascii_uppercase)
# a_dict = {}
# for i in range(1,len(a_list)+1):
#     a_dict[i]=a_list[i-1]
# for _ in range(one()):
#     r,c,n_list=inputing().split()
#     r,c=int(r),int(c)
#     n_dict = {}
#     for i in range(r):
#         new_list = n_list[c*i:c*i+c]
#         n_dict[i]=list(new_list)
#     list_list=list(n_dict.values())
#     location = [[1,0],[0,1],[-1,0],[0,-1]]
#     x,y = 0,0
#     index = 0
#     n_index = 0
#     str_list = []
#     str_state = ""
#     while n_index < len(n_list):
#         if 0<=x<=c-1 and 0<=y<=r-1:
#             if list_list[y][x]!="X":
#                 # print("first")
#                 str_state+=list_list[y][x]
#                 list_list[y][x]="X"
#                 x+=location[index][0]
#                 y+=location[index][1]
#                 if not 0<=x<=c-1 or not 0<=y<=r-1:
#                     # print("first_plus")
#                     x-=location[index][0]
#                     y-=location[index][1]
#                     index+=1
#                     index%=len(location)
#                     x+=location[index][0]
#                     y+=location[index][1]
#             else:
#                 # print("second",x,y)
#                 x-=location[index][0]
#                 y-=location[index][1]
#                 index+=1
#                 index%=len(location)
#                 x+=location[index][0]
#                 y+=location[index][1]
#                 str_state+=list_list[y][x]
#                 list_list[y][x]="X"
#                 x+=location[index][0]
#                 y+=location[index][1]
#         else:
#             # print("third")
#             x-=location[index][0]
#             y-=location[index][1]
#             index+=1
#             index%=len(location)
#             x+=location[index][0]
#             y+=location[index][1]
#             str_state+=list_list[y][x]
#             list_list[y][x]="X"
#         n_index+=1
#         if len(str_state) == 5:
#             str_list.append(str_state)
#             str_state=""
#         # print(n_index,location[index],x,y,0<=x<=c-1 and 0<=y<=r-1)
#         # for i in list_list:
#         #     print(*i)
#     # print(str_list)
#     total = ""
#     for i in str_list:
#         a = int(i,2)
#         if a in a_dict:
#             total+=a_dict[int(i,2)]
#         else:
#             total+=" "
#     print(total.rstrip())



