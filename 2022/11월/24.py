import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/25966
# a,b,r = wow()
# n_list = [list(wow()) for _ in range(a)]
# for _ in range(r):
#     n = list(wow())
#     if n[0]==1:
#         x,y,z = n
#         n_list[y],n_list[z]=n_list[z],n_list[y]
#     else:
#         x,y,z,r = n
#         n_list[y][z]=r
# for i in n_list:
#     print(*i)

# n_dict = {'a': 'aespa', 'b': 'baekjoon', 'c': 'cau', 'd': 'debug', 'e': 'edge', 'f': 'firefox', 'g': 'golang', 'h': 'haegang', 'i': 'iu', 
# 'j': 'java', 'k': 'kotlin', 'l': 'lol', 'm': 'mips', 'n': 'null', 'o': 'os', 'p': 'python', 'q': 'query', 'r': 'roka', 's': 'solvedac', 't': 'tod', 'u': 'unix', 'v': 'virus', 'w': 'whale', 'x': 'xcode', 'y': 'yahoo', 'z': 'zebra'}
# # a_dict = {'aespa': 'a', 'baekjoon': 'b', 'cau': 'c', 'debug': 'd', 'edge': 'e', 'firefox': 'f', 'golang': 'g', 'haegang': 'h', 'iu': 'i', 
# # 'java': 'j', 'kotlin': 'k', 'lol': 'l', 'mips': 'm', 'null': 'n', 'os': 'o', 'python': 'p', 'query': 'q', 'roka': 'r', 'solvedac': 's', 'tod': 't', 'unix': 'u', 'virus': 'v', 'whale': 'w', 'xcode': 'x', 'yahoo': 'y', 'zebra': 'z'}
# # https://www.acmicpc.net/problem/25594
# n = inputing()
# index = 0
# str_str = ""
# while index < len(n):
#     a = n[index]
#     if n[index:index+len(n_dict[a])] == n_dict[a]:
#         str_str+=a
#         # print(index,a,n[index:index+len(n_dict[a])])
#         index+=len(n_dict[a])
#     else:
#         # print(a,"no")
#         break

# if index== len(n):
#     # if len(str_str) == 1:
#     #     print("It's HG!")
#     #     print(n)
#     # else:
#     print("It's HG!")
#     print(str_str)
# else:
#     print("ERROR!")
        
# https://www.acmicpc.net/problem/25757
# r,s = inputing().split()
# r = int(r)
# if s == "Y":
#     limit = 2
# elif s == "F":
#     limit = 3
# else:
#     limit = 4
# n_dict = {}
# for _ in range(r):
#     a = inputing()
#     if a not in n_dict:
#         n_dict[a] = 1
#     else:
#         n_dict[a]+=1
# print(len(n_dict)//(limit-1))     
        
#https://www.acmicpc.net/problem/10994
# n = one()
# r = n*2-1
# front = 1
# l = (2*(n-1))*2+1
# back = l-2
# str_str = list("*"*(l))
# r = n-1
# list_list = ["".join(str_str)]
# # print(list_list)
# for _ in range(n-1):
#     c = list(str_str)
#     # print(front,back)
#     c[front:back+1] = " "*(back-front+1)
#     c = [i for i in c]
#     list_list.append("".join(c))
#     str_str[front],str_str[back]=" "," "
#     list_list.append("".join(str_str))
#     front+=2
#     back -=2
#     # print("".join(c),"".join(str_str))
# for i in list_list:
#     print(i)
# for i in list_list[::-1][1:]:
#     print(i)

#https://www.acmicpc.net/problem/10997
# n = one()
# if n == 1:
#     print("*")
# else:
#     l = (2*(n-1))*2+1
#     r = 7+4*(n-2)
#     n_list = [[" "]*l for _ in range(r)]
#     y,x = 0,l-1
#     move = [[0,-1],[1,0],[0,1],[-1,0]]
#     index = 0
#     cnt = 0
#     while True:
#         cnt+=1
#         if 0<=x<=l-1 and 0<=y<=r-1:
#             if n_list[y][x] == " ":
#                 n_list[y][x]="*"
#                 m = move[index]
#                 y+=m[0]
#                 x+=m[1]
#             else:
#                 m = move[index]
#                 y-=m[0]
#                 x-=m[1]
#                 n_list[y][x]=" "
#                 y-=m[0]
#                 x-=m[1]
#                 index+=1
#                 index%=len(move)
#                 m = move[index]
#                 y+=m[0]
#                 x+=m[1]
#                 if n_list[y][x] == " ":
#                     n_list[y][x]="*"
#                     m = move[index]
#                     y+=m[0]
#                     x+=m[1]
#                 else:
#                     break
#         else:
#             m = move[index]
#             y-=m[0]
#             x-=m[1]
#             index+=1
#             index%=len(move)
#             m = move[index]
#             y+=m[0]
#             x+=m[1]
#             if n_list[y][x] == " ":
#                 n_list[y][x]="*"
#                 m = move[index]
#                 y+=m[0]
#                 x+=m[1]
#             else:
#                 break
#         # print(cnt)
#     # print(y,x)
#     n_list[y+1][x+1]=" "
#     n_list[1]="*"
#     for i in n_list:
#         print("".join(i))



        
                
            
    
        
        
        
        
        
        
        
        
        
        













