import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

l,k = wow()
n_list = list(wow())
cnt = 0  
def merge(x,y):
    global k
    global cnt
    temp_list = []
    x_index = 0
    y_index = 0
    while x_index<len(x) and y_index<len(y):
        cnt+=1
        xx,yy = x[x_index],y[y_index]
        if xx<yy:
            if cnt == k:
                print(xx)
                exit()
            temp_list.append(xx)
            x_index+=1
        else:
            if cnt == k:
                print(yy)
                exit()
            temp_list.append(yy)
            y_index+=1
    if x_index != len(x):
        for i in range(x_index,len(x)):
            cnt+=1
            if cnt == k:
                print(x[i])
                exit()
            temp_list.append(x[i])
    if y_index != len(y):
        for i in range(y_index,len(y)):
            cnt+=1
            if cnt == k:
                print(y[i])
                exit()
            temp_list.append(y[i])
    return temp_list
    
    
def go(list_list,l):
    list_list = [i for i in list_list]
    if l%2:
        a,b = l//2+1,l-l//2
    else:
        a,b = l//2,l-l//2
    x=list_list[:a]
    x_l=len(list_list[:a])
    y=list_list[a:a+b+1]
    y_l=len(list_list[a:a+b+1])
    if x_l >= 2:
        x = go(x,x_l)
    if y_l >= 2:
        y = go(y,y_l)
    total = merge(x,y)
    return total
        

f = go(n_list,l)
# print("f",f)
print(-1)











