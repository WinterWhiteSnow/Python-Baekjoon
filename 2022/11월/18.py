import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/3063
# def go(a,b,c,d,num):
#     for yy in range(b,d):
#         for xx in range(a,c):
#             y_index = str(yy)
#             x_index = str(xx)
#             if x_index+y_index not in n_dict:
#                 if num == 1:
#                     n_dict[x_index+y_index]=1
#                     cnt[0]+=1
#             else:
#                 if n_dict[x_index+y_index] == 1:
#                     cnt[0]-=1
#                     n_dict[x_index+y_index]=2
# for _ in range(one()):
#     a,b,c,d,x,y,z,r = wow()
#     n_dict = {}
#     cnt = (c-a)*(d-b)
#     for yy in range(max(b,y),min(d,r)):
#         for xx in range(max(a,x),min(c,z)):
#             if b<=yy<=d and a<=xx<=c:
#                 cnt-=1
#     print(cnt)
    # go(a,b,c,d,1)
    # go(x,y,z,r,2)
    # print(n_dict,len(n_dict))
#1 1 10000 10000 2 2 5000 5000   

https://www.acmicpc.net/problem/3129
import string
str_str = list(string.ascii_lowercase)
a = inputing()#암호화된것 -> +index
b = inputing()#일부분 원문
state = "none"
ll = 0
for index in range(len(a)-len(b)+1):
    list_list = []
    ind = index
    for bb in b: #암호화 안된것
        after = str_str.index(a[ind])#암호화된것
        before = str_str.index(bb)#암호화 안된것
        if before>after:
            after+=26
        key= after-before
        ind+=1
        list_list.append(key)
    l = len(list_list)
    print(index,list_list)
    if state == "none":
        state = index
        ll = l
    else:
        if ll > l:
            state = index
            ll = l
print(state,ll)
# b_index = 0
# temp_list = [] 
# for index in range(state,state+len(b)):
#     aa,bb = a[index],b[b_index]
#     x = str_str.index(aa)#암호화된것
#     y = str_str.index(bb)#원문
#     print(aa,bb)
#     if x<y:
#         x+=25
#     gap = x-y
#     temp_list.append(gap)
#     b_index+=1
#     b_index%=len(b)
#     print(index,temp_list)
# # for x,y in zip(a,b):
# #     print(str_str.index(y),str_str.index(x))


















