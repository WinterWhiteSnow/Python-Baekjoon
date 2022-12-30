import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/16637
# l = one()
# n_list = list(inputing())
# total = []
# def go(index,list_list):
#     # print("start",list_list,index)
#     if len(list_list)-3>=index:
#         x,z,y = list_list[index:index+3]
#         # print(x,z,y)
#         x,y = int(x),int(y)
#         if z == "+":
#             num = x+y
#         if z == "-":
#             num = x-y
#         if z == "*":
#             num = x*y
#         if z == "/":
#             if x<0 or y<0:
#                 if x<0 and y<0:
#                     num = int(abs(x)/abs(y))
#                 else:
#                     num = -int(abs(x)/abs(y))
#             else:
#                 num = int(abs(x)/abs(y))
#         list_list = list_list[:index]+[num]+list_list[index+3:]
#         # print("end",list_list)
#         for i in range(index+2,index+2+len(list_list)-2,2):
#             go(i,list_list)  
#     else:
#         # print("final")
#         # print("list_list",list_list)
#         while len(list_list) >= 3:
#             x,z,y = list_list[:3]
#             x,y = int(x),int(y)
#             if z == "+":
#                 num = x+y
#             if z == "-":
#                 num = x-y
#             if z == "*":
#                 num = x*y
#             if z == "/":
#                 if x<0 or y<0:
#                     if x<0 and y<0:
#                         num = int(abs(x)/abs(y))
#                     else:
#                         num = -int(abs(x)/abs(y))
#                 else:
#                     num = int(abs(x)/abs(y))
#             # print("num",num)
#             list_list = [num]+list_list[3:]
#             # print(list_list)
#         total.append(list_list[0])
# for i in range(0,l,2):
#     # print(n_list[i])
#     go(i,n_list)
# # print(total)
# print(max(total))

#https://www.acmicpc.net/problem/16638
# l = one()
# n_list = list(inputing())
# total = []
# def go(index,list_list):
#     # print("start",list_list,index)
#     if len(list_list)-3>=index:
#         x,z,y = list_list[index:index+3]
#         # print(x,z,y)
#         x,y = int(x),int(y)
#         if z == "+":
#             num = x+y
#         if z == "-":
#             num = x-y
#         if z == "*":
#             num = x*y
#         if z == "/":
#             if x<0 or y<0:
#                 if x<0 and y<0:
#                     num = int(abs(x)/abs(y))
#                 else:
#                     num = -int(abs(x)/abs(y))
#             else:
#                 num = int(abs(x)/abs(y))
#         list_list = list_list[:index]+[num]+list_list[index+3:]
#         # print("end",list_list)
#         for i in range(index+2,index+2+len(list_list)-2,2):
#             go(i,list_list)
#         while "*" in list_list:
#             index = list_list.index("*")
#             x,z,y = list_list[index-1:index+2]
#             x,y =int(x),int(y)
#             num = x*y
#             list_list = list_list[:index-1]+[num]+list_list[index+2:]
#         # print("restart",list_list)
#         while len(list_list) >= 3:
#             x,z,y = list_list[:3]
#             x,y = int(x),int(y)
#             if z == "+":
#                 num = x+y
#             if z == "-":
#                 num = x-y
#             if z == "*":
#                 num = x*y
#             if z == "/":
#                 if x<0 or y<0:
#                     if x<0 and y<0:
#                         num = int(abs(x)/abs(y))
#                     else:
#                         num = -int(abs(x)/abs(y))
#                 else:
#                     num = int(abs(x)/abs(y))
#             # print("num",num)
#             list_list = [num]+list_list[3:]
#             # print(list_list)
#         total.append(list_list[0])
              
#     else:
#         # print("final")
#         # print("list_list",list_list)
#         while "*" in list_list:
#             index = list_list.index("*")
#             x,z,y = list_list[index-1:index+2]
#             x,y =int(x),int(y)
#             num = x*y
#             list_list = list_list[:index-1]+[num]+list_list[index+2:]
#         while len(list_list) >= 3:
#             x,z,y = list_list[:3]
#             x,y = int(x),int(y)
#             if z == "+":
#                 num = x+y
#             if z == "-":
#                 num = x-y
#             if z == "*":
#                 num = x*y
#             if z == "/":
#                 if x<0 or y<0:
#                     if x<0 and y<0:
#                         num = int(abs(x)/abs(y))
#                     else:
#                         num = -int(abs(x)/abs(y))
#                 else:
#                     num = int(abs(x)/abs(y))
#             # print("num",num)
#             list_list = [num]+list_list[3:]
#             # print(list_list)
#         total.append(list_list[0])
# for i in range(0,l,2):
#     # print(n_list[i])
#     go(i,n_list)
# # print(total)
# print(max(total))

#https://www.acmicpc.net/problem/16639
# l = one()
# n_list = list(inputing())
# max_max = [-2**31]
# def go(index,list_list):
#     # print("start",list_list,index)
#     tem_list = [i for i in list_list]
#     x,z,y = tem_list[index],tem_list[index+1],tem_list[index+2]
#     x,y = int(x),int(y)
#     if z == "+":
#         num = x+y
#     if z == "-":
#         num = x-y
#     if z == "*":
#         num = x*y
#     tem_list = tem_list[:index]+[num]+tem_list[index+3:]
#     # print("end!!",tem_list)
#     if len(tem_list)>=3:
#         for i in range(0,len(tem_list)-2,2):
#             go(i,tem_list)
#     else:
#         # print("end!!!",tem_list)
#         max_max[0]=max(max_max[0],tem_list[0])
            
        
# if l >= 3:
#     for i in range(0,l-2,2):
#         # print(n_list[i])
#         go(i,n_list)
# else:
#     max_max[0]=max(max_max[0],int(n_list[0]))
# # print(total)
# print(max_max[0])

while True:
    a = one()
    if  a==0:
        break
    








