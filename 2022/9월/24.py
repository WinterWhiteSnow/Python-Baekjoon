import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# #2628
# l,r = wow()
# sero_list = [0,r]
# garo_list = [0,l]
# for _ in range(one()):
#     a,b = wow()
#     if a==0:
#         sero_list.append(b)
#     else:
#         garo_list.append(b)
# sero_list.sort()
# garo_list.sort()
# # print(sero_list)
# # print(garo_list)
# max_max = 0
# for y in range(len(sero_list)-1):
#     y_d = sero_list[y+1]-sero_list[y]
#     for x in range(len(garo_list)-1):
#         x_d = garo_list[x+1]-garo_list[x]
#         max_max = max(max_max,y_d*x_d)
# print(max_max)

import pandas as pd
import openpyxl

    
def solution(commands):
    n_dict = {}
    for row in range(10):
        n_dict[row]=[0]*10
    date = pd.DataFrame(n_dict)
    print_list = []
    for i in commands:
        list_list = i.split()
        if list_list[0] == "UPDATE":
            if len(list_list) == 4:
                order,row,column,value = list_list
                row,column = int(row),int(column)
                date.loc[row,column]=value
            else:
                order,key,answer = list_list
                date.replace(key,answer)
        elif list_list[0]=="MERGE":
            order,row1,column1,row2,column2 = list_list
            row1,column1,row2,column2 = int(row1),int(column1),int(row2),int(column2)
            date.loc[row1:row2,column1:column2]
            print(date)

        elif list_list[0]=="UNMERGE":
            order,row,column=list_list
            row,column=int(row),int(column)
        else:
            order,row,column = list_list
            row,column = int(row),int(column)
            print_list.append(date.loc[row,column])
        
commands = ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]
solution(commands)

