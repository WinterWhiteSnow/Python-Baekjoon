import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# r =one()
# n_list = [list(wow()) for _ in range(r)]
# max_max = 0
# for i in range(r):
#     n_dict = {}
#     for index in range(r):
#         if index == i:
#             pass
#         else:
#             a,b = n_list[index]
#             for num in range(a,b):
#                 n_dict[num]=1
#     max_max = max(max_max,len(n_dict.keys()))
# print(max_max)
    
# minus,plus,a,b = wow()
# print((a+b)//(minus-plus))
# import string
# str_str = list(string.ascii_uppercase)
# while True:
#     a = inputing()
#     if a == "0":
#         break
#     b = inputing()
#     a = a*(len(b)//len(a)+2)
#     for x,y in zip(a,b):
#         print(str_str[(((str_str.index(x)+1)+str_str.index(y))%26)],end="")
#     print()
while True:
    a = inputing()
    if a == "I quacked the code!":
        break
    
    try:
        print()
        if a[-1] == ".":
            print("*Nod*")
        else:
            print("Quack!")
    except:
        pass
    
    # sys.stdout.flush()
    sys.stdin.flush()
            
            
    
    

