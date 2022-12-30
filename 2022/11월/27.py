import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/4134
# for _ in range(one()):
#     num = one()
#     if num <= 2:
#         print(2)
#     else:
#         while True:
#             check = "no"
#             for i in range(2,int(num**(1/2))+1):
#                 if num%i == 0:
#                     check ="yes"
#                     break
#             if check == "yes":
#                 num+=1
#             else:
#                 break
#         print(num)

#https://www.acmicpc.net/problem/10434
# for _ in range(one()):
#     index,num = wow()
#     sosu_check ="yes"
#     for i in range(2,int(num**(1/2))+1):
#         if num%i == 0:
#             sosu_check = "no"
#             break
#     answer = "YES"
#     if num == 1:
#         sosu_check="no"
#     if sosu_check == "no":
#         answer = "NO"
#     else:
#         num_list =  list(map(int,sorted(list(str(num)))))
#         # print(num_list)
#         new_list = [num_list]
#         while True:
#             # print(new_list)
#             cnt = 0
#             for i in new_list[-1]:
#                 cnt+=i**2
#             # print(cnt)
#             if cnt ==1:
#                 break
#             tem_list = list(map(int,sorted(list(str(cnt)))))
#             if tem_list not in new_list:
#                 new_list.append(tem_list)
#             else:
#                 answer = "NO"
#                 break
#     print(index,num,answer)

#https://www.acmicpc.net/problem/19699
# import itertools
# n_dict = {}
# for i in range(2,9001):
#     if i not in n_dict:
#         for a in range(i,9001,i):
#             n_dict[a]=0
#         n_dict[i]=1
# # list_list = [a for a,b in n_dict.items() if b == 1]
# l,r = wow()
# n_list = list(wow())
# a = list(map(sum,list(itertools.combinations(n_list,r=r))))
# cnt_list = []
# for i in a:
#     if n_dict[i] == 1:
#         if i not in cnt_list:
#             cnt_list.append(i)
# if len(cnt_list) > 0:
#     print(*sorted(cnt_list))
# else:
#     print(-1)

#https://www.acmicpc.net/problem/9753
# n_dict = {}
# num = 100000+1
# for i in range(2,num):
#     if i not in n_dict:
#         for a in range(i,num,i):
#             n_dict[a]=0
#         n_dict[i]=1
# n_list = [a for a,b in n_dict.items() if b==1]
# for _ in range(one()):
#     num = one()
#     if num == 1:
#         print(6)
#     else:
#         start = 0
#         end = len(n_list)-1
#         number = num//2+1
#         # print(number)
#         while start<=end:
#             mid = (start+end)//2
#             # print("mid",mid,n_list[mid])
#             if n_list[mid]>number:
#                 end=mid-1
#             else:
#                 start = mid+1
#         list_list = n_list[:start+1]
#         # print(list_list)
#         min_min = "none"
#         for a in range(len(list_list)-1):
#             for b in range(a+1,len(list_list)):
#                 x,y = list_list[a],list_list[b]
#                 if x*y>=num:
#                     if x*y == num:
#                         min_min=x*y
#                         break
#                     if min_min == "none":
#                         min_min=x*y
#                     else:
#                         min_min=min(x*y,min_min)
#             if min_min==num:
#                 break
#         print(min_min)

#https://www.acmicpc.net/problem/10859
# num = one()
# check = "yes"
# if num == 1:
#     print("no")
# else:
#     for i in range(2,int(num**(1/2))+1):
#         if num%i==0:
#             check ="no"
#             break
#     if check == "yes":
#         str_num = ""
#         if "3" in str(num) or "4" in str(num) or "7" in str(num):
#             print("no")
#         else:
#             for i in str(num)[::-1]:
#                 if i == "6":
#                     str_num+="9"
#                 elif i == "9":
#                     str_num+="6"
#                 else:
#                     str_num+=i
#             str_num = int(str_num)
#             check = "yes"
#             for i in range(2,int(str_num**(1/2))+1):
#                 if str_num%i == 0:
#                     check = "no"
#                     break
#             print(check)
#     else:
#         print("no")

#https://www.acmicpc.net/problem/9842
# n_dict = {}
# for i in range(2,110000):
#     if i not in n_dict:
#         for a in range(i,110000,i):
#             n_dict[a]=0
#         n_dict[i]=1
# n_list = [a for a,b in n_dict.items() if b == 1]
# print(n_list[one()-1])


for _ in range(one()):
    n_list = list(wow())
    l = n_list[0]
    zero_list=[[n_list[0],n_list[1]]]
    check = "no"
    index = 2
    # while index <= l:
    zero_index = 0
    end = index
    while index <= l:
        if index == 2:
            for _ in range(l-(index-1)):
                zero_list.append(zero_list[-1][1:]+[n_list[end]])
                end+=1
        else:
            for i in range(l-)
        for i in range(len(zero_list)):
            total = sum(zero_list[i])
            for num in range(2,int(total**(1/2))+1):
                if total%num != 0:
                    check ="yes"
                    zero_index=i
                    break
        if check == "yes":
            break
        index+=1
        
        

                

    






























