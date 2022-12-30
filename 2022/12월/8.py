import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1141
# n_list = []
# for _ in range(one()):
#     a = inputing()
#     if len(n_list)==0:
#         n_list.append(a)
#     else:
#         check = "no"
#         for i in range(len(n_list)):
#             b = n_list[i]
#             if a in b:
#                 if b.index(a) == 0:
#                     check = "yes"
#                     if len(a)>len(b):
#                         n_list[i]=a
#             if b in a:
#                 if a.index(b) == 0:
#                     check = "yes"
#                     if len(a)>len(b):
#                         n_list[i]=a
#         if check == "no":
#             n_list.append(a)
#     # print(n_list)
# print(len(n_list))

#https://www.acmicpc.net/problem/13411
# n_list = []
# for i in range(one()):
#     a,b,c= wow()
#     n_list.append([i+1,(((b**2+a**2))**(1/2))/c])
# n_list.sort(key=lambda x: x[1])               
# n_list = [a for a,b in n_list]
# # print(n_list)
# print(*n_list,sep="\n")

l = one()
n_list = sorted(list(wow()))
num = one()
start = 0
end = l-1
while start<=end:
    mid = (start+end)//2
    if n_list[mid]<num:
        start=mid+1
    else:
        end=mid-1
# print(start,end,n_list[start],n_list[end])
if n_list[start] == num or n_list[end]==num:
    print(0)
else:
    index = end
    end = n_list[index+1]-1
    start = n_list[index]+1
    if start >= num:
        print(0)
    else:
        cnt = 0
        for number in range(start,end):
            if number<=num<=end:
                if number < num:
                    cnt+=end-max(number,num)+1
                else:
                    cnt+=end-num
            else:
                break
        print(cnt)
        










