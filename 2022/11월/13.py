import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/17122
# import string
# import math
# str_str = list(string.ascii_uppercase)
# for _ in range(one()):
#     a,b = inputing().split()
#     a = list(a)
#     x,y = a
#     y = int(y)
#     b = int(b)
#     if y%2:
#         if str_str.index(x)%2:
#             a_color = "white"
#         else:
#             a_color = "black"
#     else:
#         if str_str.index(x)%2:
#             a_color = "black"
#         else:
#             a_color = "white"
#     b_index = math.ceil(b/8)
#     b_str = b%8
#     if b_index%2:
#         if b_str%2:
#             b_color = "black"
#         else:
#             b_color = "white"
#     else:
#         if b_str%2:
#             b_color = "white"
#         else:
#             b_color = "black"
#     # print(b_color,a_color)
#     if b_color==a_color:
#         print("YES")
#     else:
#         print("NO")

#https://www.acmicpc.net/problem/16677
# n_list = inputing()
# n_dict = {}
# l = len(n_list)
# for num in range(one()):
#     index = 0
#     a,b = inputing().split()
#     b = int(b)
#     str_str = ""
#     for i in a:
#         if index < l:
#             if i == n_list[index]:
#                 index+=1
#             else:
#                 str_str+=i
#         else:
#             str_str+=i
#     if index == l:
#         n_dict[a]=[b/len(str_str),num]
# list_list = list(n_dict.items())
# if len(list_list) > 0:
#     list_list.sort(key=lambda x: x[1][1])
#     list_list.sort(key=lambda x: x[1][0],reverse=True)
#     print(list_list[0][0])
# else:
#     print("No Jam")

#https://www.acmicpc.net/problem/25562
# n = one()
# a_list = [1]
# index = 2
# for i in range(n-1):
#     a_list.append(a_list[-1]*index)
# a_cnt = {}
# for x in range(len(a_list)-1):
#     for y in range(x+1,len(a_list)):
#         a,b = a_list[x],a_list[y]
#         a_cnt[abs(a-b)]=1
# print(len(a_cnt))
# print(*a_list)
# b_list = [a_list[-1]+1]
# for _ in range(n-1):
#     b_list.append(b_list[-1]+1)
# b_cnt={}
# for x in range(len(b_list)-1):
#     for y in range(x+1,len(b_list)):
#         a,b = b_list[x],b_list[y]
#         b_cnt[abs(a-b)]=1
# print(len(b_cnt))
# print(*b_list)

#https://www.acmicpc.net/problem/16200
# l = one()
# n_list = sorted(list(wow()))
# now_list = []
# cnt = 0
# for i in n_list:
#     if len(now_list) <= i:
#         now_list.append(i)
#         if len(now_list) == now_list[0]:
#             now_list = []
#             cnt+=1
# if len(now_list) != 0:
#     cnt+=1
# print(cnt)

#https://www.acmicpc.net/problem/15233
# a,b,c = wow()
# a_list = inputing().split()
# a_dict = {}
# for i in a_list:
#     a_dict[i]=0
# b_list = inputing().split()
# b_dict = {}
# for i in b_list:
#     b_dict[i]=0
# a_cnt = 0
# b_cnt = 0
# # print(a_dict,b_dict)
# for i in inputing().split():
#     if i in a_dict:
#         a_cnt+=1
#     if i in b_dict:
#         b_cnt+=1
# if a_cnt>b_cnt:
#     print("A")
# elif a_cnt==b_cnt:
#     print("TIE")
# else:
#     print("B")

# gap = 1
# list_list = [list(inputing()) for _ in range(5)]
# n_dict = {}
# for x in range(10):
#     x_index = 3*x
#     if x != 0:
#         x_index+=gap
#         gap+=1
#     new_list = ""
#     for y in range(5):
#         print(list_list[y][x_index:x_index+3])
#         new_list+="".join(list_list[y][x_index:x_index+3])
#     n_dict[new_list]=x
# print(n_dict)

n_dict={'**** ** ** ****': 0, '  *  *  *  *  *': 1, '***  *****  ***': 2, '***  ****  ****': 3, '* ** ****  *  *': 4, '****  ***  ****': 5, '****  **** ****': 6, '***  *  *  *  *': 7, '**** ***** ****': 8, '**** ****  ****': 9}
list_list = [list(inputing()) for _ in range(5)]
answer = ""
gap = 1
check = "yes"
stack = 1
# while 3*stack+(stack-1) != len(list_list[0]):
#     stack+=1

for x in range(stack):
    x_index = 3*x
    if x != 0:
        x_index+=gap
        gap+=1
    str_str = ""
    for y in range(5):
        plus = list_list[y][x_index:x_index+3]
        for _ in range(3-len(plus)):
            plus +=[" "]
        # print(plus)
        str_str+="".join(plus)
    # print("wow")
    if str_str in n_dict:
        answer+=str(n_dict[str_str])
    else:
        check = "no"
if check =="no":
    print("BOOM!!")
else:
    answer = int(answer)%6
    if answer == 0:
        print("BEER!!")
    else:
        print("BOOM!!")







          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
            
            
            
        





















