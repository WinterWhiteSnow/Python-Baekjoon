import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/5637
# import string
# str_str = list(string.ascii_letters)+["-"]
# n_list = []
# index = 0
# while True:
#     a = inputing()
#     for i in a.split():
#         str_list = ""
#         for ii in i:
#             if ii in str_str:
#                 str_list+=ii
#         n_list.append([str_list.lower(),index])
#         index+=1
#     if "E-N-D" in a:
#         break
# n_list.sort(key=lambda x: x[1])
# n_list.sort(key=lambda x: len(x[0]), reverse=True)
# print(n_list[0][0])

#https://www.acmicpc.net/problem/11947
for _ in range(one()):
    a = list(inputing())
    str_str = ""
    for i in a:
        i = int(i)
        if i >= 4:
            str_str+="4"
        else:
            if i>=3:
                str_str+="3"
            elif 6<=i<=9:
                str_str+="6"
            else:
                str_str+=str(i)
        break
    first_text = int(str_str)
    if int(a[0]) > first_text:
        answer = 
    print(str_str)









#https://www.acmicpc.net/problem/22351
#https://www.acmicpc.net/problem/17419
#https://www.acmicpc.net/problem/16439







