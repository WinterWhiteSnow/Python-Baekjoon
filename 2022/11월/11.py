import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/2089
# num = one()
# if num == 0:
#     print(0)
# else:
#     n_list = []
#     while num != 0:
#         answer = num%-2
#         check = "no"
#         if answer < 0:
#             answer+=2
#             check ="yes"
#         n_list.append(str(answer))
#         if check == "yes":
#             num-=2
#         num//=-2
#         # print(n_list,num)
#     print("".join(n_list[::-1]))

#https://www.acmicpc.net/problem/9711
# n_list = [1, 1, 2, 3, 5, 8, 13, 21, 34]
# for i in range(1,1+one()):
#     k,d = wow()
#     while len(n_list) < k:
#         n_list.append(n_list[-2]+n_list[-1])
#     answer = n_list[k-1]%d
#     print(f"Case #{i}: {answer}")

#https://www.acmicpc.net/problem/25375
# for _ in range(one()):
#     a,b = wow()
#     if b%a == 0:
#         if 2*a <= b:
#             print(1)
#         else:
#             print(0)
#     else:
#         print(0)

#https://www.acmicpc.net/problem/12755
# index = 1
# l = 0
# num = one()
# while l+len(str(index)) < num :
#     l+=len(str(index))
#     index+=1
# print(str(index)[num-l-1])   

#https://www.acmicpc.net/problem/21557
# l = one()
# n_list = list(wow())
# cnt = l-3
# while cnt != 0:
#     a = n_list[0]
#     b=n_list[-1]
#     gap = min(cnt,abs(a-b))
#     if gap >0:
#         if a>b:
#             n_list[0]-=gap
#         else:
#             n_list[-1]-=gap
#         cnt-=gap
#     else:
#         n_list[0]-=1
#         cnt-=1
# a = n_list[0]
# b=n_list[-1]  
# print(max(a-1,b-1))    

#https://www.acmicpc.net/problem/25325
# l = one()
# n_dict = {}
# name = inputing().split()    
# for i in name:
#     n_dict[i]=0
# for i in range(l):
#     now_name = name[i]
#     list_list=inputing().split()
#     for plus in list_list:
#         if plus != now_name:
#             n_dict[plus]+=1
# list_list = sorted(n_dict.items(),key=lambda x: x[0])
# list_list.sort(key=lambda x: x[1],reverse=True)
# for a,b in list_list:
#     print(a,b)
    


    
    
    
    
    
    
    
    
    







