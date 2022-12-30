import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/25632
# n_dict = {}
# for i in range(2,1001):
#     if i not in n_dict:
#         for a in range(i,1001,i):
#             n_dict[a]=0
#         n_dict[i]=1
# n_list = [a for a,b in n_dict.items() if b == 1]

# a,b = wow()
# x,y = wow()
# def go(num,what):
#     start = 0
#     end = len(n_list)-1
#     while start<=end:
#         mid = (start+end)//2
#         if num<n_list[mid]:
#             end=mid-1
#         else:
#             start=mid+1
#     if what == "front":
#         return end
#     else:
#         return start
# aa,bb = go(a,"front"),go(b,"back")
# if n_list[aa]<a:
#     aa+=1
# xx,yy = go(x,"front"),go(y,"back")
# if n_list[xx]<x:
#     xx+=1
# a_list = n_list[aa:bb]
# b_list = n_list[xx:yy]
# state = 0
# # print(a_list,b_list,sep="\n")
# while True:
#     if state == 0:
#         pop_list = a_list
#         stay_list = b_list
#     else:
#         pop_list = b_list
#         stay_list = a_list
#     if len(pop_list) == 0:
#         break
#     check = list(set(pop_list)&set(stay_list))
#     if len(check) > 0:
#         del pop_list[pop_list.index(check[0])]
#         del stay_list[stay_list.index(check[0])]
#     else:
#         pop_list.pop()
#     if state == 0:
#         a_list = pop_list
#         b_list = stay_list
#     else:
#         b_list = pop_list
#         a_list = stay_list   
#     state+=1
#     state%=2
#     # print(a_list,b_list,state,sep="\n")
# # print(state)
# print("yt" if state == 1 else "yj")

two,five = 0,0
cnt = 1
index = 1
limit = one()
while min(two,five) < limit:
    cnt*=index
    if cnt%2 == 0:
        while cnt%2 == 0:
            cnt//=2
            two+=1
    if cnt%5 == 0:
        while cnt%5 == 0:
            cnt//=5
            five+=1
    if min(two,five)==limit:
        break
    index+=1
print(index,two,five)
if min(two,five) == limit:
    print(index)
else:
    print(-1)





















