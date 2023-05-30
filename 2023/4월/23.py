import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# k = one()
# n_list = [-1]*(k+1)
# for i in [3,5]:
#     num = i
#     if num > k:
#         continue
#     n_list[num]=1
#     for k in range(num+1,k+1):
#         if n_list[k] == -1:
#             if n_list[k-num] != -1:
#                 n_list[k]=n_list[k-num]+1         
#         else:
#             if n_list[k-num] != -1:
#                 n_list[k]=min(n_list[k],n_list[k-num]+1)
#     # print(num)
#     # print(n_list)
# print(n_list[k])

# num = one()
# total = [0]*(num+1)
# total[1]=0
# for i in range(2,num+1):
#     total[i]=i-1
#     if i%2 == 0:
#         total[i]=min(total[i//2]+1,total[i])
#     if i%3 == 0:
#         total[i]=min(total[i//3]+1,total[i])
#     if i-1 > 1:
#         total[i]=min(total[i],total[i-1]+1)
#     # print(i)
#     # print(total)
# # print(total)
# print(total[num])

# def go(num):
#     # print(num,"!!!!")
#     if num in n_dict:
#         return n_dict[num]
#     a,b = go(num-1)
#     c,d = go(num-2)
#     n_dict[num]=[a+c,b+d]
#     return [a+c,b+d]
# n_dict = {}
# n_dict[1]=[0,1]
# n_dict[0]=[1,0]
# for _ in range(one()):
#     n = one()
#     if n in n_dict:
#         print(*n_dict[n])
#     else:
#         print(*go(n))

# n = one()
# x,y = 0,1
# for _ in range(n-1):
#     x,y = y,x+y
#     x%=10007
#     y%=10007
# print((x+y)%10007)

# r = one()
# n_list = [list(wow()) for _ in range(r)]
# for i in range(1,r):
#     for index in range(3):
#         n_list[i][index]+=min(n_list[i-1][(index+1)%3],n_list[i-1][(index+2)%3])
#         # print(index,index+1))
#     # print(i)
#     # print(n_list)
# print(min(n_list[-1]))

# total = [0]*12
# total[0]=1
# total[1]=1
# total[2]=2
# total[3]=4
# total[4]=7
# for i in range(5,12):
#     total[i]=total[i-1]+total[i-2]+total[i-3]
# for _ in range(one()):
#     n = one()
#     print(total[n])

# total = [0]*101
# total[1]=1
# total[2]=1
# total[3]=1
# for i in range(4,101):
#     total[i]=total[i-2]+total[i-3]
# for _ in range(one()):
#     print(total[one()])

# l = one()
# total = [0]*10
# for i in range(1,10):
#     total[i]=1
# # print(total)         

# for _ in range(l-1):
#     new_list = []
#     for i in range(10):
#         if i == 0:
#             new_list.append(total[1]%1000000000)
#         elif i == 9:
#             new_list.append(total[8]%1000000000)
#         else:
#             new_list.append((total[i-1]+total[i+1])%1000000000)
#     total=new_list 
# print(sum(total)%1000000000)  

# z,o = 0,1
# for _ in range(one()-1):
#     z,o=z+o,z 
# print(z+o)   

# r,k = wow()
# n_list = [0]*(k+1)
# for _ in range(r):
#     n = one()
#     if n > k:
#         continue
#     n_list[n]+=1
#     for i in range(n+1,k+1):
#         n_list[i]+=n_list[i-n]
# print(n_list[k])

# n = one()
# n_list = [one() for _ in range(n)]
# zero_list = [0]*(n+1)
# zero_list[1]=n_list[0]
# if n >= 2:
#     zero_list[2]=n_list[1]+zero_list[1]
# if n>=3:
#     zero_list[3]=max(zero_list[2],zero_list[1]+n_list[2],n_list[1]+n_list[2])
# for i in range(4,n+1):
#     zero_list[i]=max(max(zero_list[i-2],zero_list[i-3]+n_list[i-2])+n_list[i-1],zero_list[i-1])
# print(max(zero_list))

# r,k = wow()
# n_list = [0]*(k+1)
# for i in range(1,r+1):
#     weight,value = wow()
#     for w in range(k,0,-1):
#         if w < weight:
#             break
#         n_list[w]=max(n_list[w-weight]+value,n_list[w])
# print(n_list[k])

#https://www.acmicpc.net/problem/11054
# l = one()
# n_list = list(wow())
# a_list = [1]*l
# b_list = [1]*l
# for i in range(1,l+1):
#     a = n_list[i-1]
#     b = n_list[-i]
#     for index1 in range(i-1):
#         check = n_list[index1]
#         if check < a:
#             a_list[i-1]=max(a_list[i-1],a_list[index1]+1)
#     for index2 in range(-1,-i,-1):
#         check = n_list[index2]
#         if b>check:
#             b_list[-i]=max(b_list[-i],b_list[index2]+1)
# max_max = 0
# for i in range(l):
#     max_max = max(max_max,a_list[i]+b_list[i])
# print(max_max-1)

for t in range(int(input())):
    l,k = map(int,input().split())
    n_list = list(map(int,input().split()))
    zero_list = [[0]*(k+1) for _ in range(l+1)]
    













