import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1911
# r,l = wow()
# n_list = [list(wow()) for _ in range(r)]
# n_list.sort(key=lambda x: x[0])
# # print(n_list)
# max_max = n_list[-1][1]
# # print(m_list)
# cnt = 0
# state = "none"
# for i in n_list:
#     a,b = i
#     for x in range(a,b):
#         # print("x",x,"state",state,"cnt",cnt)
#         if state == "none":
#             state=min(x+l-1,max_max)
#             cnt+=1
#         else:
#             if state < x:
#                 cnt+=1
#                 state = x+l-1
# print(cnt)

#https://www.acmicpc.net/problem/2713
# import string
# str_list = list(string.ascii_uppercase)
# str_list = [" "]+str_list
# # print(str_list)
# for _ in range(one()):
#     n_list = sys.stdin.readline()
#     r = "none"
#     c = "none"
#     temp = ""
#     num = ""
#     for i in range(len(n_list)):
#         # print("wow",n_list[i],i)
#         if n_list[i].isdigit():
#             num+=n_list[i]
#             # print(num,i)
#         else:
#             if r == "none":
#                 # print("first")
#                 r = int(num)
#                 num = ""
#             else:
#                 if c == "none":
#                     # print(i,"woooooo")
#                     c = int(num)
#                     break
        

#     str_str = n_list[i+1:-1]
#     # print(str_str,len(str_str),str_str.replace(" ","wow"))
#     a = []
#     # for i in str_str:
#     #     a.append(" "+i)
#     # str_str = "".join(a)[1:]
#     num_list = []
#     for i in str_str:
#         # print("yes",i)
#         b = bin(str_list.index(i))[2:].rjust(5,"0")
#         num_list.extend(list(b))
#     for _ in range(r*(c+1)-len(num_list)):
#         num_list.append("0")
#     # print(num_list)
#     num_index = 0
#     zero_list = [[0]*c for _ in range(r)]
#     move_list = [[0,1],[1,0],[0,-1],[-1,0]]
#     move_index = 0
#     y,x = 0,0
#     while True:
#         # print("start",y,x)
#         if 0<=y<=r-1 and 0<=x<=c-1:
#             if zero_list[y][x] == 0:
#                 # print(zero_list[y][x],num_list[num_index],type(zero_list[y][x]),type(num_list[num_index]))
#                 zero_list[y][x]=num_list[num_index]
#                 num_index+=1
#                 move = move_list[move_index]
#                 y+=move[0]
#                 x+=move[1]
#             else:
#                 move = move_list[move_index]
#                 y-=move[0]
#                 x-=move[1]
#                 move_index+=1
#                 move_index%=4
#                 move = move_list[move_index]
#                 y+=move[0]
#                 x+=move[1]
#                 if zero_list[y][x] == 0:
#                     zero_list[y][x]=num_list[num_index]
#                     num_index+=1
#                     y+=move[0]
#                     x+=move[1]
#                 else:
#                     break
#         else:
#             move = move_list[move_index]
#             y-=move[0]
#             x-=move[1]
#             move_index+=1
#             move_index%=4
#             move = move_list[move_index]
#             y+=move[0]
#             x+=move[1]
#             if 0<=y<=r-1 and 0<=x<=c-1:
#                 if zero_list[y][x] == 0:
#                     zero_list[y][x]=num_list[num_index]
#                     num_index+=1
#                     y+=move[0]
#                     x+=move[1]
#                 else:
#                     break
#             else:
#                 break
#         # print(y,x)
#         # for i in zero_list:
#         #     print(i)
#     str_str = []
#     for i in zero_list:
#         for a in i:
#             a = str(a)
#             str_str.append(a)
#     print("".join(str_str))
            
r = one()
n_dict = {}
for i in range(2,10001):
    if i not in n_dict:
        for a in range(i,10001,i):
            n_dict[a]=0
        n_dict[i]=1
n_list = [a for a,b in n_dict.items() if b == 1] 
for _ in range(r):
    list_list = list(wow())
    total = sum(list_list)
    start = 0
    end = len(n_list)
    while start<=end:
        mid = (start+end)//2
        if n_list[mid] > total:
            end = mid-1
        else:
            start=mid+1
    sosu_list = n_list[:end+1]
    count = 0
    minus = []
    start = "none"
    end = "none"
    l = 10001
    for i in range(len(list_list)):
        x = list_list[i]
        count+=x
        if i>=2:
            if count in sosu_list:
                l = i+1
                start = 0
                end = i
                # print("one",start,end,l)
            for key in range(len(minus)):
                if count-minus[key] in sosu_list:
                    gap = i-key-1
                    if 2<= gap < l:
                        print("gap",gap,i)
                        l = gap
                        state = key
                        end = i
        minus.append(count)
        print(minus,start,end,l)
    print(start,end,l)
    
        
             
        
                













