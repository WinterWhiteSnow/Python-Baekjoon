import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/9626
# row,c = wow()
# u,l,r,d = wow()
# n_list = [inputing() for _ in range(row)]
# max_l = c+l+r
# str_list = ["#.",".#"]
# str_index = 0
# for _ in range(u):
#     a = str_list[str_index]
#     x = a*max_l
#     print(x[:max_l])
#     str_index+=1
#     str_index%=2
# for i in range(row):
#     a = str_list[str_index]
#     x = list((a*max_l)[:max_l])
#     # print(x)
#     str_str = n_list[i]
#     ii = 0
#     for index in range(l,l+c):
#         x[index]=str_str[ii]
#         ii+=1
#     print("".join(x))
#     str_index+=1
#     str_index%=2
# for _ in range(d):
#     a = str_list[str_index]
#     x = a*max_l
#     print(x[:max_l])
#     str_index+=1
#     str_index%=2

#https://www.acmicpc.net/problem/9329
# for _ in range(one()):
#     n,m = wow()
#     list_list = []
#     m_list = []
#     n_dict = {}
#     for _ in range(n):
#         n_list = list(wow())
#         money = n_list[-1]
#         l = n_list[0]
#         n_list = n_list[1:-1]
#         for key in n_list:
#             n_dict[key]=0
#         list_list.append(n_list)
#         m_list.append(money)
#     w_list = list(wow())
#     for i in range(1,1+m):
#         score = w_list[i-1]
#         if i in n_dict:
#             n_dict[i]=score
#     cnt = 0
#     # print(n_dict,list_list,m_list)
#     for index in range(len(m_list)):
#         money = m_list[index]
#         state = "none"
#         for l in list_list[index]:
#             if state == "none":
#                 state = n_dict[l]
#             else:
#                 state = min(state,n_dict[l])
#         # print(state,money)
#         cnt+=state*money
#     print(cnt)

#https://www.acmicpc.net/problem/7656
# a = inputing()
# while "What is" in a:
#     check = a.index("What is")
#     a = a[check+len("What is"):]
#     str_str = ""
#     for i in a:
#         if i == "W":
#             break
#         if "?" in i:
#             str_str+=i
#             break
#         else:
#             str_str+=i
#     if "?" in str_str:
#         print("Forty-two is"+str_str[:-1]+".")        
# What is the answer to life. What is the answer to money?

r = one()
for _ in range(one()):
    yy,xx = 0,0
    x,y = wow()
    x-=1
    y-=1
    state_list = ["R","B","Y"]
    l = abs(y-x)%3
    gap = min(x,y)
    end = (r-1)-gap
    print("end",end)
    if x>y:
        if x<=end:
            pass
        else:
            x-=end
            gap+=x
    gap%=3
    print(state_list[gap])
        
        
        
            
















