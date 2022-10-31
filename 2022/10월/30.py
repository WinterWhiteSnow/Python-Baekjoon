import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())


#https://www.acmicpc.net/problem/11051
# r,k = wow()
# n_list = [[1],[1,1]]
# if r <= 1:
#     print(n_list[r-1][k-1])
# else:
#     for _ in range(r-1):
#         list_list = n_list.pop()
#         new_list = []
#         for i in range(len(list_list)-1):
#             new_list.append((list_list[i]+list_list[i+1])%10007)
#         new_list.append(1)
#         new_list.insert(0,1)
#         n_list.append(new_list)
#     print(n_list[-1][k])   

for l in range(int(input())):
    number = input()
    strstr=""
    firstindex=0
    while len(strstr) != len(number):
        firstnum = number[firstindex]
        if int(firstnum) <=4: 
            strstr+=str(9-int(firstnum))
        else:
            strstr+=str(4)
            break
        firstindex+=1
    strstr=strstr.rjust(len(number),"4")
    number = strstr
    index = len(number)-1
    cnt = 0
    mumber = ""
    for i in number:
        mumber+=str(9-int(i))
    number_number = ""
    for i in number:
        number_number+=str(9-int(i))
    # print("number",number,"mumber",mumber)
    last_number = str(int(number[0])-1) if int(number[0])-1 >=1 else "0"
    last_number=last_number.rjust(len(number)-1,"4")
    max_max = ""
    for i in last_number:
        max_max+=str(9-int(i))
    print(max(int(number)*int(mumber),int(number_number)*int(number),int(last_number)*int(max_max)))












