import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/16935
# r,c,l = wow()
# n_list = [list(wow()) for _ in range(r)]
# move = [(0,0),(0,1),(1,1),(1,0)]
# for order in list(wow()):
#     n_dict = {}
#     if order == 1:
#         n_list = n_list[::-1]
#     if order == 2:
#         for i in range(r):
#             n_list[i]=n_list[i][::-1]
#     if order == 3 or order == 4:
#         for y in range(r):
#             for x in range(c):
#                 if order == 3:
#                     if x not in n_dict:
#                         n_dict[x]=[n_list[y][x]]
#                     else:
#                         n_dict[x]+=[n_list[y][x]]
#                 else:
#                     if y not in n_dict:
#                         n_dict[y]=[n_list[y][x]]
#                     else:
#                         n_dict[y]+=[n_list[y][x]]
                    
                
#         r = len(n_dict)
#         c = len(n_dict[0])
#         new_list = list(n_dict.values())
#         # print("start!")
#         if order == 3:
#             for i in range(len(new_list)):
#                 new_list[i]=new_list[i][::-1]
#         else:
#             for i in range(len(new_list)):
#                 new_list[i]=new_list[i][::-1]
#             n_dict = {}
#             for y in range(r):
#                 for x in range(c):
#                     if x not in n_dict:
#                         n_dict[x]=[new_list[y][x]]
#                     else:
#                         n_dict[x]+=[new_list[y][x]]
#             new_list = list(n_dict.values())
#         n_list = new_list
#         r = len(n_list)
#         c = len(n_list[-1])
#     if order == 5 or order == 6:
#         new_list = [[0]*c for _ in range(r)]
#         for repeat in range(4):
#             y,x=move[repeat]
#             if order == 5:
#                 b,a= move[(repeat+1)%4]
#             else:
#                 b,a = move[(repeat-1)%4]
#             b,a =b*r//2,a*c//2
#             y,x = y*r//2,x*c//2
#             for yy in range(r//2):
#                 for xx in range(c//2):
#                     yyy,xxx=y+yy,x+xx
#                     bbb,aaa=b+yy,a+xx
#                     # print("start!",yyy,xxx,bbb,aaa)
#                     new_list[bbb][aaa]=n_list[yyy][xxx]
#         n_list =new_list
# for i in n_list:
#     print(*i)


numbers = inputing()
n_dict = {}
n_list = []
answer = {}
def check(visit,str_str):
    global cnt
    if int(str_str) in n_list:
        answer[int(str_str)]=1
    for i in range(len(numbers)):
        if visit[i] == 0:
            visit[i]=1
            check(visit,str_str+numbers[i])
            visit[i]=0
for i in range(2,9999999):
    if i not in n_dict:
        for a in range(i,9999999,i):
            n_dict[a]=0
        n_list.append(i)
print(len(n_list))
v = [0]*len(numbers)
for i in range(len(numbers)):
    v[i]=1
    check(v,numbers[i])
    v[i]=0
print(answer)


        
            
        
        











