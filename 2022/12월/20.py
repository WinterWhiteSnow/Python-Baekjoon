import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/2470
# l = one()
# n_list = sorted(list(wow()))
# gap = "none"
# start = 0
# end = l-1
# xx = "none"
# yy = "none"
# while start<end:
#     a,b = n_list[start],n_list[end]
#     temp = a+b
#     if gap =="none":
#         gap = temp
#         xx,yy = min(a,b),max(a,b)
#     else:
#         if abs(gap)>abs(temp):
#             gap = temp
#             xx,yy = min(a,b),max(a,b)
#     if temp<0:
#         start+=1
#     else:
#         end-=1
#     # print(xx,yy,gap)
#     # print(start,end)
# print(xx,yy)

# https://www.acmicpc.net/problem/17609
# for _ in range(one()):
#     str_str = inputing()
#     if str_str == str_str[::-1]:
#         print(0)
#     else:
#         point = 1
#         start = 0
#         end = len(str_str)-1
#         while start<end:
#             x,y = str_str[start],str_str[end]
#             if x==y:
#                 start+=1
#                 end-=1
#             else:
#                 # print(start,end)
#                 # print(str_str[start+1:end+1])
                
#                 if point != 0:
#                     if str_str[start:end]==str_str[start:end][::-1]:
#                         start=2
#                         end=1
#                         break
#                     elif str_str[start+1:end+1] == str_str[start+1:end+1][::-1]:
#                         start=2
#                         end=1
#                         break
#                     else:
#                         start=0
#                         end=len(str_str)-1
#                         break
#                 else:
#                     start=0
#                     end=len(str_str)-1
#                     break
#             # print(start,end)
#             # print(str_str[start],str_str[end])
#         # print(start,end)
#         print(1 if abs(start-end) <= 1 else 2)
# babba(1)
# XYXYAAYXY(1)
# cccfccfcc(1)

n_dict = {}
n = one()
if n == 3:
    print(1)
else:
    for i in range(2,n+1):
        if i not in n_dict:
            for a in range(i,n+1,i):
                n_dict[a]=0
            n_dict[i]=1
    n_list = [a for a,b in n_dict.items() if b==1]
    cnt = 0
    n_list.sort()
    n_list = [0]+n_list
    # print(n_list)
    # cnt+=n_list.count(n)
    start =0
    end=len(n_list)-1
    zero_list = [n_list[0]]
    for i in range(1,len(n_list)):
        zero_list.append(zero_list[-1]+n_list[i])
    print(zero_list)
    while start != len(zero_list)-1:
        start_start = start
        end_end = end
        while start_start<=end_end:
            mid = (start+end)//2
            x,y = zero_list[start_start],zero_list[mid]
            # if y-x == n: 
            #     print(start_start,mid,y-x)
            if y-x > n:
                end_end=mid-1
            else:
                if y-x == n:
                    cnt+=1
                    start+=1
                    end=len(zero_list)-1
                    break
                else:
                    end=mid+1
            print("end!!",cnt,y-x,start,end)
    print(cnt)        














