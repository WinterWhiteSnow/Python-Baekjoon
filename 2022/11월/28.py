import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/26068
# cnt = 0
# for _ in range(one()):
#     num = int(inputing().replace("D-",""))
#     if num <= 90:
#         cnt+=1
# print(cnt)

#https://www.acmicpc.net/problem/2824
# import math
# l = one()
# x = 1
# for i in list(wow()):
#     x*=i
# y = 1
# l = one()
# for i in list(wow()):
#     y*=i
# print(str(math.gcd(x,y))[::-1][:9][::-1])

#https://www.acmicpc.net/problem/1124
# n_dict = {}
# a,b = wow()
# x=a
# for i in range(2,b+1):
#     if i not in n_dict:
#         for a in range(i,b+1,i):
#             n_dict[a]=0
#         n_dict[i]=1
# n_dict[0]=0
# n_dict[1]=0
# cnt = 0
# for num in range(x,b+1):
#     number =num
#     n_list = []
#     for i in range(2,int(num**(1/2))+1):
#         if num>=i:
#             while num>=i:
#                 if num%i == 0:
#                     n_list.append(i)
#                     num//=i
#                 else:
#                     break
#         else:
#             break
#     if num != 1:
#         n_list.append(num)
#     l = len(n_list)
#     # print(number,num,n_list,l)
#     cnt+=n_dict[l]
# print(cnt)

#https://www.acmicpc.net/problem/9421
# n_dict = {}
# for i in range(2,1000001):
#     if i not in n_dict:
#         for a in range(i,1000001,i):
#             n_dict[a]=0
#         n_dict[i]=1
# n_list = [a for a,b in n_dict.items() if b == 1]
# total_list = []
# for i in range(len(n_list)):
#     num = n_list[i]
#     list_list = [num]
#     check = "yes"
#     while True:
#         num_list = list(map(int,list(str(list_list[-1]))))
#         cnt = 0
#         for i in num_list:
#             cnt+=i**2
#         if cnt == 1:
#             break
        
#         if cnt not in list_list:
#             list_list.append(cnt)
#         else:
#             check = "no"
#             break
#     if check == "yes":
#         total_list.append(num)
# num = one()
# start=0
# end = len(total_list)-1
# while start<=end:
#     mid = (start+end)//2
#     if total_list[mid]>num:
#         end = mid-1
#     else:
#         start=mid+1
# for i in total_list[:start]:
#     print(i)

#https://www.acmicpc.net/problem/5636
# n_dict = {}
# for i in range(2,100001):
#     if i not in n_dict:
#         for a in range(i,100001,i):
#             n_dict[a]=0
#         n_dict[i]=1
# n_list = [a for a,b in n_dict.items() if b==1]
# while True:
#     num = list(inputing())
#     if num == ["0"]:
#         break
#     num_list = num[0]
#     list_list = num
#     l = len(num)
#     index = 2
#     end = index
#     while index <= l:
#         if index == 2:
#             temp_list = [[num_list,num[index-1]]]
#         else:
#             temp_list = [num_list+[num[index-1]]]
#         # print(temp_list)
#         for _ in range(l-index):
#             temp_list.append(temp_list[-1][1:]+[num[end]])
#             end+=1
#         num_list=temp_list[0]
#         # print(temp_list,temp_list[0])
#         temp_list = list(map("".join,temp_list))
#         index+=1
#         end=index
#         list_list.extend(temp_list)
#     list_list = list(map(int,list_list))
#     list_list.sort(reverse=True)
#     # print(list_list)
#     for i in list_list:
#         if i in n_list:
#             print(i)
#             break

n_dict = {}
for i in range(2,1001):
    if i not in n_dict:
        for a in range(i,1001,i):
            n_dict[a]=0
        n_dict[i]=1
n_list = [a for a,b in n_dict.items() if b == 1]

a,b = wow()
x,y = wow()
a_list = n_list[n_list.index(a):n_list.index(b)+1]
b_list = n_list[n_list.index(x):n_list.index(y)+1]
state = 0
# print(a_list,b_list,sep="\n")
while True:
    if state == 0:
        pop_list = a_list
        stay_list = b_list
    else:
        pop_list = b_list
        stay_list = a_list
    if len(pop_list) == 0:
        break
    check = list(set(pop_list)&set(stay_list))
    if len(check) > 0:
        del pop_list[pop_list.index(check[0])]
        del stay_list[stay_list.index(check[0])]
    else:
        pop_list.pop()
    if state == 0:
        a_list = pop_list
        b_list = stay_list
    else:
        b_list = pop_list
        a_list = stay_list   
    state+=1
    state%=2
    print(a_list,b_list,sep="\n")
# print(state)
print("yt" if state == 1 else "yj")

    












            
        
            
    
        






















