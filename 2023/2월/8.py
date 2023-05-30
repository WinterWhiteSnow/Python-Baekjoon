import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/14499
# r,l,y,x,k = wow()
# n_list = [list(wow()) for _ in range(r)]
# dice = [[0]*3 for _ in range(4)]
# move_list = [(0,1),(0,-1),(-1,0),(1,0)]
# move = list(wow())
# if n_list[y][x] != 0:
#     dice[3][1]=n_list[y][x]
#     n_list[y][x]=0
# for index in move:
#     # print("direction",index)
#     # print(dice[1][1])
#     index-=1
#     move_index = move_list[index]
#     yy,xx = move_index
#     if 0<=y+yy<=r-1 and 0<=x+xx<=l-1:
#         if index+1 == 1:#동쪽
#             dice[1],dice[3][1]=[dice[3][1]]+dice[1][:2],dice[1][-1]
#         elif index+1 == 2:#서쪽
#             dice[1],dice[3][1]=dice[1][1:]+[dice[3][1]],dice[1][0]
#         elif index+1 == 3:#북쪽
#             list_list = []
#             for i in range(4):
#                 list_list.append(dice[i][1])
#             list_list = list_list[1:]+[list_list[0]]
#             for i in range(4):
#                 dice[i][1]=list_list[i]
#         else:#남쪽
#             list_list = []
#             for i in range(4):
#                 list_list.append(dice[i][1])
#             list_list = [list_list[-1]]+list_list[:3]
#             for i in range(4):
#                 dice[i][1]=list_list[i]
#         if n_list[y+yy][x+xx] == 0:
#             n_list[y+yy][x+xx]=dice[3][1]
#         else:
#             dice[3][1]=n_list[y+yy][x+xx]
#             n_list[y+yy][x+xx]=0
#         print(dice[1][1])
#         # for i in dice:
#         #     print(i)
#         y+=yy
#         x+=xx
#     # for i in dice:
#     #     print(i)

#https://www.acmicpc.net/problem/12100
r = one()
n_list = [list(wow()) for _ in range(r)]

def top(list_list):
    temp_list = []
    n_dict ={}
    for i in range(r):
        b_list = list_list[i]
        list_list_list = []
        l = len(list_list)
        # print("temp",b_list)
        if l%2:
            ll = l-1
        else:
            ll = l
        for index in range(0,ll,2):
            x,y = b_list[index],b_list[index+1]
            # print(x,y,index,index+1)
            if x != 0 and y != 0:
                if len(list_list_list) > 0:
                    if list_list_list[-1] == x:
                        list_list_list.pop()
                        list_list_list.append(x*2)
                        list_list_list.append(0)                        
                        list_list_list.append(y)
                    else:                        
                        if x==y and x != 0 and y != 0:
                            list_list_list.append(x+y)
                            list_list_list.append(0)
                        else:
                            list_list_list.append(x)                      
                            list_list_list.append(y)
                else:
                    if x==y and x != 0 and y != 0:
                        list_list_list.append(x+y)
                        list_list_list.append(0)
                    else:
                        list_list_list.append(x)    
                        list_list_list.append(y)
            else:
                z = x+y
                if z != 0:
                    if len(list_list_list) > 0:
                        if list_list_list[-1] == z:
                            list_list_list.pop()
                            list_list_list.append(z*2)
                            list_list_list.append(0)
                        else:
                            list_list_list.append(z)
                    else:
                        list_list_list.append(z)
        #     print("end?",list_list_list)
        # print("now",list_list_list)
        if len(list_list_list) == 0:
            list_list_list.append(0)
        if l%2:
            if list_list_list[-1] == b_list[-1]:
                list_list_list.pop()
                list_list_list.append(b_list[-1]*2)
                list_list_list.append(0)
            else:
                list_list_list.append(b_list[-1])
        no = []
        for i in range(len(list_list_list)):
            if list_list_list[i] != 0:
                no.append(list_list_list[i])
        for _ in range(l-len(no)):
            no.append(0)
        # print(list_list_list)
        for i in range(len(no)):
            if i not in n_dict:
                n_dict[i]=[no[i]]
            else:
                n_dict[i]+=[no[i]]

    new_list = []
    for i in n_dict.values():
        # print("value",i)
        new_list.append(i)
    # print("top!!!!",new_list)
    return new_list
        
def down(list_list):
    temp_list = []
    n_dict ={}
    for i in range(r):
        b_list = list_list[i][::-1]
        list_list_list = []
        l = len(b_list)
        # print("temp",b_list)
        if l%2:
            ll = l-1
        else:
            ll = l
        zero_cnt = 0
        for index in range(0,ll,2):
            x,y = b_list[index],b_list[index+1]
            # print(x,y,index,index+1)
            if x != 0 and y != 0:
                if len(list_list_list) > 0:
                    if list_list_list[-1] == x:
                        list_list_list.pop()
                        list_list_list.append(x*2)
                        list_list_list.append(0)                        
                        list_list_list.append(y)
                    else:                        
                        if x==y and x != 0 and y != 0:
                            list_list_list.append(x+y)
                            list_list_list.append(0)
                        else:
                            list_list_list.append(x)                      
                            list_list_list.append(y)
                else:
                    if x==y and x != 0 and y != 0:
                        list_list_list.append(x+y)
                        list_list_list.append(0)
                    else:
                        list_list_list.append(x)    
                        list_list_list.append(y)
            else:
                z = x+y
                if z != 0:
                    if len(list_list_list) > 0:
                        if list_list_list[-1] == z:
                            list_list_list.pop()
                            list_list_list.append(z*2)
                            list_list_list.append(0)
                        else:
                            list_list_list.append(z)
                    else:
                        list_list_list.append(z)
        #     print("state",list_list_list)
        # print("now",list_list_list)
        if len(list_list_list) == 0:
            list_list_list.append(0)
        if l%2:
            if list_list_list[-1] == b_list[-1]:
                list_list_list.pop()
                list_list_list.append(b_list[-1]*2)
                list_list_list.append(0)
            else:
                list_list_list.append(b_list[-1])
        no = []
        for i in range(len(list_list_list)):
            if list_list_list[i] != 0:
                no.append(list_list_list[i])
        for _ in range(l-len(no)):
            no.append(0)
        list_list_list=no
        for i in range(len(list_list_list)):
            if i not in n_dict:
                n_dict[i]=[list_list_list[i]]
            else:
                n_dict[i]+=[list_list_list[i]]
    
    new_list = []
    for i in n_dict.values():
        # print("value",i)
        new_list.append(i)
    # print("top!!!!",new_list)
    
    return new_list[::-1]

    

def left(list_list):
    temp_list = []
    for i in range(r):
        b_list = list_list[i]
        list_list_list = []
        l = len(b_list)
        if l%2:
            ll = l-1
        else:
            ll = l
        for index in range(0,ll,2):
            x,y = b_list[index],b_list[index+1]
            if x != 0 and y != 0:
                if len(list_list_list) > 0:
                    if list_list_list[-1] == x:
                        list_list_list.pop()
                        list_list_list.append(x*2)
                        list_list_list.append(0)                        
                        list_list_list.append(y)
                    else:                        
                        if x==y and x != 0 and y != 0:
                            list_list_list.append(x+y)
                            list_list_list.append(0)
                        else:
                            list_list_list.append(x)                      
                            list_list_list.append(y)
                else:
                    if x==y and x != 0 and y != 0:
                        list_list_list.append(x+y)
                        list_list_list.append(0)
                    else:
                        list_list_list.append(x)    
                        list_list_list.append(y)
            else:
                z = x+y
                if z != 0:
                    if len(list_list_list) > 0:
                        if list_list_list[-1] == z:
                            list_list_list.pop()
                            list_list_list.append(z*2)
                            list_list_list.append(0)
                        else:
                            list_list_list.append(z)
                    else:
                        list_list_list.append(z)
        if len(list_list_list) == 0:
            list_list_list.append(0)
        if l%2:
            if list_list_list[-1] == b_list[-1]:
                list_list_list.pop()
                list_list_list.append(b_list[-1]*2)
                list_list_list.append(0)
            else:
                list_list_list.append(b_list[-1])
        no = []
        for i in range(len(list_list_list)):
            if list_list_list[i] != 0:
                no.append(list_list_list[i])
        for _ in range(l-len(no)):
            no.append(0)
        temp_list.append(no)
    return temp_list

    
def right(list_list):
    temp_list = []
    for i in range(r):
        b_list = list_list[i][::-1]
        # print("b_list",b_list)
        list_list_list = []
        l = len(b_list)
        if l%2:
            ll = l-1
        else:
            ll = l
        for index in range(0,ll,2):
            x,y = b_list[index],b_list[index+1]
            if x != 0 and y != 0:
                if len(list_list_list) > 0:
                    if list_list_list[-1] == x:
                        list_list_list.pop()
                        list_list_list.append(x*2)
                        list_list_list.append(0)                        
                        list_list_list.append(y)
                    else:                        
                        if x==y and x != 0 and y != 0:
                            list_list_list.append(x+y)
                            list_list_list.append(0)
                        else:
                            list_list_list.append(x)                      
                            list_list_list.append(y)
                else:
                    if x==y and x != 0 and y != 0:
                        list_list_list.append(x+y)
                        list_list_list.append(0)
                    else:
                        list_list_list.append(x)    
                        list_list_list.append(y)
            else:
                z = x+y
                if z != 0:
                    if len(list_list_list) > 0:
                        if list_list_list[-1] == z:
                            list_list_list.pop()
                            list_list_list.append(z*2)
                            list_list_list.append(0)
                        else:
                            list_list_list.append(z)
                    else:
                        list_list_list.append(z)
        #     print("state",list_list_list)
        # print("end!!!!",list_list_list)
        if len(list_list_list) == 0:
            list_list_list.append(0)
        if l%2:
            # print("start!!!",list_list_list,b_list[-1])
            if list_list_list[-1] == b_list[-1]:
                list_list_list.pop()
                list_list_list.append(b_list[-1]*2)
                list_list_list.append(0)
            else:
                list_list_list.append(b_list[-1])
        no = []
        for i in range(len(list_list_list)):
            if list_list_list[i] != 0:
                no.append(list_list_list[i])
        for _ in range(l-len(no)):
            no.append(0)
        list_list_list = no[::-1]
        temp_list.append(list_list_list)
    return temp_list
cnt = 2
def go(count,k_list):
    global cnt
    global r
    # print(count)
    # for i in k_list:
    #     print(*i)
    if count == 5:
        # print("wow!!!")
        for i in k_list:
            # print(*i)
            cnt = max(cnt,max(i))
        return
    n_dict = {}
    for i in range(r):
        for index in range(r):
            if index not in n_dict:
                n_dict[index]=[k_list[i][index]]
            else:
                n_dict[index]+=[k_list[i][index]]
    new_list = []
    for i in n_dict.values():
        new_list.append(i)
    # print("new!!!!")
    # for i in new_list:
    #     print(*i)
    # exit()
    count+=1
    # print(count)
    d_list = down(new_list)
    l_list =left(k_list)
    r_list =right(k_list)
    t_list = top(new_list)
    go(count,t_list)
    go(count,d_list)
    go(count,r_list)
    go(count,l_list)
    # print("right",a_list)
    # print("left",a_list)
    # print("top",a_list)
    # print("down",a_list)
    count-=1
    # exit()
    
go(0,n_list)
# for i in right(n_list):
#     print(*i)
# n_dict = {}
# x = left(n_list)
# for i in range(r):
#     for index in range(r):
#         if index not in n_dict:
#             n_dict[index]=[n_list[i][index]]
#         else:
#             n_dict[index]+=[n_list[i][index]]
# new_list = []
# for i in n_dict.values():
#     new_list.append(i)
# for i in top(left(top(top(new_list)))):
#     print(*i)
# for i in down(new_list):
#     print(i)
print(cnt)
# 6
# 2 2 4 8 16 32
# 0 0 0 8 0 0
# 0 0 0 16 0 0
# 0 0 0 32 0 0
# 0 0 0 64 0 0
# 0 0 0 128 0 0







