import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/11819
# cnt = 1
# a,b,c = wow()
# def go(index,num,c):
#     # print("Start",index,num,c)
#     if index == 1:
#         return num%c
#     a = go(index//2,num,c)
#     a*=a
#     if index%2:
#         a*=num     
#     # print("end",index,num,c,a)   
#     return a%c

# aaa = go(b,a,c)
# print(aaa)

#https://www.acmicpc.net/problem/24460
# l = one()
# n_list = [list(wow()) for _ in range(l)]
# if l == 1:
#     print(n_list[0][0])
# else:
#     def go(list_list,y_index,x_index,l):
#         if l//2>=2:
#             new_list = []
#             for y in range(0,l,l//2):
#                 for x in range(0,l,l//2):
#                     if l//2>2:
#                         a = go(list_list,y+y_index,x+x_index,l//2)
#                         new_list.append(a)
#                     else:
#                         b = [list_list[y+y_index][x+x_index],list_list[y+y_index+1][x+x_index],list_list[y+y_index][1+x+x_index],list_list[y+y_index+1][1+x+x_index]]
#                         b.sort()
#                         new_list.append(b[1])
#             if new_list:
#                 new_list.sort()
#                 return new_list[1] 
#         else:
#             ll = []
#             for y in range(l):
#                 for x in range(l):
#                     ll.append(list_list[y][x])
#             ll.sort()
#             return ll[1]
#     c = go(n_list,0,0,l)
#     print(c)

#https://www.acmicpc.net/problem/6012
# num = one()
# n_list = [i for i in range(1,num+1)]
# cnt = 0
# def go(n_list,l):
#     global cnt
#     # print(n_list)
#     if l%2:
#         a= l//2+1
#     else:
#         a=l//2
#     if a>1:
#         go(n_list[:a],len(n_list[:a]))
#         go(n_list[a:],len(n_list[a:]))
#     else:
#         if l==2:
#             cnt+=n_list[1]*n_list[0]
#     # print(n_list,l)
# go(n_list,num)
# print(cnt)

n_list = []
for i in sys.stdin.readlines():
    n_list.append(int(i.rstrip()))
def go(n_list,l):
    if l%2:
        a = l//2+1
    else:
        a = l//2
    x,y = n_list[:a],n_list[a:]
    print(x,y)
    if a>1:
        go(x,len(x))
        go(y,len(y))














