from re import L
import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#회의실배정 1931
l = one()
# n_dict = {}
# for _ in range(l):
#     a,b = wow()
#     if a not in n_dict:
#         n_dict[a]=b
#     else:
#         n_dict[a]=min(n_dict[a],b)
# list_list = list(n_dict.items())
# list_list.sort(key=lambda x : x[1],reverse=True)          
# list_list.sort(key=lambda x : x[0])
n_list = []
list_list = [list(wow()) for _ in range(l)]
list_list.sort(key=lambda x : x[1])
list_list.sort(key=lambda x: x[0])
for index in range(len(list_list)):
    if len(n_list) == 0:
        n_list.append(list_list[index])
    else:
        x,y = n_list[-1]
        a,b = list_list[index]
        if x<=a and y>b:
            n_list[-1]=[a,b]
        else:
            if y<=a:
                n_list.append([a,b])
    # print(n_list)
print(len(n_list))






