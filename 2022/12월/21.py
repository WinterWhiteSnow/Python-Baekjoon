import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1759
# import string
# str_list = list(string.ascii_lowercase)
# for i in "aeiou":
#     str_list.remove(i)
# l,n = wow()
# n_list = inputing().split()
# aeiou = []
# n_list.sort()
# n_dict = {}
# # print(n_list)
# def go(index,l,n,str_str):
#     if index<=n-1:
#         str_str+=n_list[index]
#     # print(index,l,n,str_str)
#     if len(str_str) == l:
#         check = "no"
#         cnt = 0
#         for i in "aeiou":
#             if i in str_str:
#                 check ="yes"
#                 break
#         for i in str_str:
#             if i in str_list:
#                 cnt+=1
#                 if cnt == 2:
#                     break
#         if check == "yes" and cnt == 2:
#             n_dict[str_str]=1
#     else:
#         for ind in range(index+1,n):
#             go(ind,l,n,str_str)
# for start in range(n):
#     str_str = n_list[start]
#     for sta in range(start+1,n):
#         go(sta,l,n,str_str)
#     # print(n_dict)
# print(*sorted(n_dict.keys()),sep="\n")

#https://www.acmicpc.net/problem/15686
# chicken = []
# home = []
# r,m = wow()
# for y in range(r):
#     list_list = list(wow())
#     for x in range(r):
#         if list_list[x] == 1:
#             home.append([y,x])
#         if list_list[x] == 2:
#             chicken.append([y,x])
# # print("chicken",chicken)
# # print("home",home)
# def go(list_list,index,cnt,m,home_l,chicken_l):
#     if index <= chicken_l-1 and cnt != m:
#         cnt+=1
#         temp_list = []
#         # print("start",list_list,cnt,index)
#         y,x= chicken[index]
#         if cnt == 1:
#             for i in range(home_l):
#                 b,a = home[i]
#                 temp_list.append(abs(y-b)+abs(x-a))
#         else:
#             for i in range(home_l):
#                 b,a = home[i]
#                 temp_list.append(min(abs(y-b)+abs(x-a),list_list[i]))
#         list_list = temp_list
#         # print("end",list_list)
#         # print("sum",sum(list_list))
#         if cnt != m:
#             for i in range(index+1,chicken_l):
#                 go(list_list,i,cnt,m,home_l,chicken_l)
#         else:
#             if cnt == m:
#                 total.append(sum(list_list))
# total = []
# for index in range(len(chicken)):
#     go([],index,0,m,len(home),len(chicken))
#     # print("index",total)
# print(min(total))

#https://www.acmicpc.net/problem/15658
# from collections import deque
# l = one()
# n_list = deque(list(wow()))
# symbol = list(wow())
# r = l-1
# total = []
# def go(plus,minus,multipl,division,list_list):
#     # print(list_list,plus,minus,multipl,division)
#     if len(list_list) != 1:
#         temp_list = deque([i for i in list_list])
#         a,b = temp_list.popleft(),temp_list.popleft()
#         if plus > 0:
#             go(plus-1,minus,multipl,division,deque([a+b]+list(temp_list)))
#         if minus > 0:    
#             go(plus,minus-1,multipl,division,([a-b]+list(temp_list)))
#         if division > 0:
#             if (a>0 and b>0) or (a<0 and b<0):
#                 go(plus,minus,multipl,division-1,deque([int(abs(a)/abs(b))]+list(temp_list)))
#             else:
#                 go(plus,minus,multipl,division-1,deque([-int(abs(a)/abs(b))]+list(temp_list)))
#         if multipl >0:
#             go(plus,minus,multipl-1,division,deque([a*b]+list(temp_list)))
#     else:
#         total.append(sum(list_list))
# go(symbol[0],symbol[1],symbol[2],symbol[3],n_list)
# print(max(total))
# print(min(total))

#https://www.acmicpc.net/problem/1535
# l = one()
# a_list = list(wow())
# b_list = list(wow())
# n_list = []
# for i in range(l):
#     n_list.append([a_list[i],b_list[i]])
# total = []
# def go(hp,happy,index,l):
#     # print(hp,happy,index,l)
#     if index <= l-1:
#         minus_hp,plus_happy = n_list[index]
#         if hp-minus_hp>0:
#             hp-=minus_hp
#             happy+=plus_happy
            
#             for i in range(index+1,l+1):
#                 go(hp,happy,i,l)
#         else:
#             total.append(happy)
#     else:
#         total.append(happy)
# for i in range(l):      
#     go(100,0,i,l)
# print(max(total))

l = one()
n_list = list(wow())
total = []
def go(l,list_list,cnt):
    print(l,list_list,cnt)
    temp_list = [i for i in list_list]
    if l >= 3:
        for i in range(1,l-1):
            go(l-1,temp_list[:i]+temp_list[i+1:],cnt*temp_list[i-1]*temp_list[i+1])
    else:
        total.append(cnt)
go(l,n_list,1)
print(total)














