import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/2239
# n_list = [list(map(int,list(inputing()))) for _ in range(9)]
# # print(n_list)
# # for i in n_list:
# #     print(i,i[0],type(i[0]))
# # print(n_list[0],n_list[0][1],n_list[0][2])
# index_list = []
# for y in range(9):
#     for x in range(9):
#         if n_list[y][x] == 0:
#             index_list.append((y,x))
# # print(n_list,index_list)
# def sero(x,i):
#     for index in range(9):
#         if n_list[index][x]==i:
#             return False
#     return True

# def garo(y,i):
#     for index in range(9):
#         if n_list[y][index]==i:
#             return False
#     return True

# def triangle(y,x,i):
#     yy,xx = y//3*3,x//3*3
#     for y_index in range(3):
#         for x_index in range(3):
#             if n_list[y_index+yy][x_index+xx]==i:
#                 return False
#     return True

# def go(index,l):
#     if index == l:
#         for i in n_list:
#             print(*i,sep="")
#         exit()
    
#     y,x = index_list[index]
#     # print("Start",index,y,x)
#     for i in range(1,10):
#         if sero(x,i) and garo(y,i) and triangle(y=y,x=x,i=i):
#             n_list[y][x]=i
#             go(index+1,l)
#             n_list[y][x]=0
# go(0,len(index_list))


def sero(x,i):
    for index in range(9):
        if n_list[index][x]==i:
            return False
    return True

def garo(y,i):
    for index in range(9):
        if n_list[y][index]==i:
            return False
    return True

def triangle(y,x,i):
    yy,xx = y//3*3,x//3*3
    for y_index in range(3):
        for x_index in range(3):
            if n_list[y_index+yy][x_index+xx]==i:
                return False
    return True

def go(index,l):
    global num
    global check
    if check == "no":
        if index == l:
            if num != 0:
                print()
            check = "yes"
            for i in n_list:
                print(*i,sep="")
            return
        
        y,x = index_list[index]
        # print("Start",index,y,x)
        for i in range(1,10):
            if sero(x,i) and garo(y,i) and triangle(y=y,x=x,i=i):
                n_list[y][x]=i
                go(index+1,l)
                n_list[y][x]=0
                
for num in range(one()):
    n_list = [list(map(int,list(inputing()))) for _ in range(9)]

    # for i in n_list:
    #     print(i,i[0],type(i[0]))
    # print(n_list[0],n_list[0][1],n_list[0][2])
    index_list = []
    check = "no"
    for y in range(9):
        for x in range(9):
            if n_list[y][x] == 0:
                index_list.append((y,x))
    # print(n_list,index_list)
    go(0,len(index_list))
    if check == "no":
        if num != 0:
            print()
        print("Could not complete this grid.")








