import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())


#https://www.acmicpc.net/problem/5883
# r = one()
# str_str = []
# for _ in range(r):
#     str_str+=[inputing()]
# max_max = 0
# for key in set(list(str_str)):
#     new_str = [i for i in str_str if i != key]
#     cnt = 0
#     state = "none"
#     for i in new_str:
#         if state == "none":
#             state = i
#             cnt=1
#         else:
#             if state == i :
#                 cnt+=1
#             else:
#                 max_max=max(max_max,cnt)
#                 state = i
#                 cnt=1
#     max_max=max(max_max,cnt)
# print(max_max)

#https://www.acmicpc.net/problem/17254
# rr,r = wow()
# n_list = []
# for _ in range(r):
#     a,b,c = inputing().split()
#     a,b = int(a),int(b)
#     n_list.append([a,b,c])
# n_list.sort(key=lambda x: (x[1],x[0]))
# print("".join([i[2] for i in n_list]))

#https://www.acmicpc.net/problem/20114
# l,r,ll = wow()
# list_list = []
# for _ in range(r):
#     if len(list_list) == 0:
#         list_list.extend(list(inputing()))
#     else:
#         a = list(inputing())
#         for i in range(len(a)):
#             if list_list[i] == "?" and a[i] != "?":
#                 list_list[i]=a[i]
# total = ""
# for index in range(len(list_list)//ll):
#     str_str = "".join(list_list[ll*index:ll*index+ll]).replace("?","")
#     if str_str:
#         total+=str_str[0]
#     else:
#         total+="?"
# print(total)

n_list = [i for i in range(1,one()+1)]
index = 1
while len(n_list) != 1:
    i = index**index%len(n_list)
    print(n_list,i-1)
    del n_list[i-1]
    index+=1




