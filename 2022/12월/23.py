import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

l = one()
n_list = list(inputing())
total = []
def go(index,list_list):
    print("start",list_list,index)
    x,z,y = list_list[index:index+3]
    print(x,z,y)
    x,y = int(x),int(y)
    if z == "+":
        num = x+y
    if z == "-":
        num = x-y
    if z == "*":
        num = x*y
    if z == "/":
        if x<0 or y<0:
            if x<0 and y<0:
                num = int(abs(x)/abs(y))
            else:
                num = -int(abs(x)/abs(y))
        else:
            num = int(abs(x)/abs(y))
    list_list = list_list[:index]+[num]+list_list[index+3:]
    print("end",list_list)
    while len(list_list) >= 3:
        x,z,y = list_list[:3]
        x,y = int(x),int(y)
        print("x,y",x,y,z)
        if z == "+":
            num = x+y
        if z == "-":
            num = x-y
        if z == "*":
            print("wow",x,y,z)
            num = x*y
        if z == "/":
            if x<0 or y<0:
                if x<0 and y<0:
                    num = int(abs(x)/abs(y))
                else:
                    num = -int(abs(x)/abs(y))
        else:
            num = int(abs(x)/abs(y))
        print("num",num)
        list_list = [num]+list_list[3:]
        print(list_list)
    total.append(list_list)
        
        
    # for i in range(0,len(list_list)-2,2):
    #     go(i,list_list)
            
        
    x,y = int(x),int(y)
for i in range(0,l-2,2):
    print(n_list[i])
    print(go(i,n_list))
print(total)













