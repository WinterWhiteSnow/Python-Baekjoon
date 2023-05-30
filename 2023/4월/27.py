import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())


#https://www.acmicpc.net/problem/9252
# a = list(inputing())
# b = list(inputing())
# a_l = len(a)
# b_l = len(b)
# total = [[[0,""]]*(a_l+1) for _ in range(b_l+1)]
# # print(total[0][0])
# for y in range(1,b_l+1):
#     for x in range(1,a_l+1):
#         if b[y-1]==a[x-1]:
#             total[y][x]=[total[y-1][x-1][0]+1,total[y-1][x-1][1]+b[y-1]]
#         else:
#             q,w = total[y-1][x]
#             e,r = total[y][x-1]
#             if q>=e:
#                 total[y][x]=total[y-1][x]
#             else:
#                 total[y][x]=total[y][x-1]
# l = total[-1][-1]
# a,b = l
# if a == 0:
#     print(a)
# else:
#     print(a,b,sep="\n")

# def check(num):
#     for i in range(2,int(num**(1/2))+1):
#         if num%i == 0:
#             return True
#     return False
# def go(gap):
#     for i in range(4,10**9+1-gap):
#         if check(i):
#             if check(i+gap):
#                 return i
# for t in range(int(input())):
#     t = t+1
#     n = int(input())
#     index = go(n)
#     print("#"+str(t),index,index+n)
# def check(n,t,repeat):
#     for i in range(2,repeat+1):
#         number = sorted(list(str(i*n)))
#         # print(number,check_list,number==check_list)
#         if number == check_list:
#             # print(number==check_list)
#             print("#"+str(t),"possible")
#             return
#     print("#"+str(t),"impossible")
    
# for t in range(int(input())):
#     t = t+1
#     n = input()
#     check_list = sorted(list(n))
#     n_list = list(map(int,list(n)))
#     n_list.sort()
#     max_max = int("".join(map(str,sorted(n_list,reverse=True))))
#     repeat = max_max//int(n)+1
#     check(int(n),t,repeat)
    
# for t in range(int(input())):
#     t = t+1
#     n,m,k = map(int,input().split())
#     n_list = list(map(int,input().split()))
#     cnt = 0
#     n_list.sort()
#     state = True
#     for time in range(n_list[-1]+1):
#         if time%m==0 and time !=0:
#             cnt+=k
#         if n_list[0]==time:
#             if cnt>0:
#                 cnt-=1
#                 n_list = n_list[1:]
#             else:
#                 state=False
#                 break
#     # print(n_list)
#     print("#"+str(t),"Possible" if state else "Impossible")
            
# for t in range(int(input())):
#     t = t+1
#     r = int(input())
#     total = [0]*5001
#     for _ in range(r):
#         a,b = list(map(int,input().split()))
#         for index in range(a,b+1):
#             total[index]+=1
#     # print(total[:10])
#     c = int(input())
#     print("#"+str(t),end=" ")
#     for _ in range(c):
#         num = int(input())
#         print(total[num],end=" ")
#     print()

n_dict = {}
for i in range(2,10**6+1):
    if i not in n_dict:
        for a in range(i,10**6+1,i):
            n_dict[a]=0
        n_dict[i]=1
n_list = [a for a,b in n_dict.items() if b == 1]
n_list.sort()
l = len(n_list)

def check(num,state):
    global l
    start = 0
    end = l-1
    while start<=end:
        # print(start,end,l)
        mid = (start+end)//2
        n = n_list[mid]
        if num == n_list[mid]:
            return mid
        if n > num:
            end=mid-1
        else:
            start=mid+1
    # print("end",num,end,start,n_list[end],n_list[start])
    if end < 0:
        end = 0
    # print(start,end,n_list[start],n_list[end])
    return end

for t in range(int(input())):
    t = t+1
    d,a,b = map(int,input().split())
    start = check(a,"front")
    end = check(b,"back")
    if n_list[start] < a:
        start+=1
    # print(n_list[start],n_list[end])
    cnt = 0
    for i in range(start,end+1):
        n = n_list[i]
        if str(d) in str(n):
            cnt+=1
    print("#"+str(t),cnt)



