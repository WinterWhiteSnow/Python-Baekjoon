import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/3054
# a = list(inputing())
# n_dict = {}
# for i in range(5):
#     n_dict[i]=[]
# for i in range(len(a)):
#     key = a[i]
#     if i%3==2:
#         list_list = ["..*..",".*.*.",f"*.{key}.*",".*.*.","..*.."]
#     else:
#         list_list = ["..#.",".#.#",f"#.{key}.",".#.#","..#."]
#     for index in range(5):
#         if i != 0 and i%3==0:
#             n_dict[index]+=list_list[index][1:]
#         else:
#             n_dict[index]+=list_list[index]    
#     if i == len(a)-1:
#         if i != 0 and i%3==2:
#             pass
#         else:
#             end_list = list("..#..")
#             for i in range(len(end_list)):
#                 n_dict[i]+=end_list[i]
# for i in n_dict.values():
#     print(*i,sep="")
            
#https://www.acmicpc.net/problem/3279
# n_list = [one() for _ in range(one())]
# state = "buy"
# num = n_list[0]
# a = 100
# b = 0
# for index in range(len(n_list)):
#     gap = n_list[index]
#     # print("start",a,b,gap,state)
#     if state == "buy":
#         if gap >= num:
#             num = gap
#         else:
#             b+=num*(a/100)
#             a=0       
#             state = "sell"
#             num = gap
#     else:
#         if gap <= num:
#             num = gap
#         else:
#             a+=b/num*100
#             b = 0
#             state = "buy"
#             num=gap
#     # print(num,a,b,state)
# if state == "sell":
#     a+=b/num*100
# a = str(a)
# if "." not in a:
#     a+=".00"
# else:
#     a = a[:a.index(".")+3]
# if (len(a)-1)-a.index(".") <2:
#     a+="0"*((len(a)-1)-a.index("."))
# print(a)

#https://www.acmicpc.net/problem/3553
# l,d = wow()
# start = 10**(l-1)
# if start%d != 0:
#     start+=(d-start%d)
# print(start if len(str(start)) ==l else "No solution")

#https://www.acmicpc.net/problem/14709
# n_list = []
# for _ in range(one()):
#     a = sorted(list(wow()))
#     n_list.append(a)
# n_list.sort(key=lambda x: (x[0],x[1]))
# b_list = [[1,3],[1,4],[3,4]]
# b_list.sort(key=lambda x: (x[0],x[1]))
# # print(n_list,b_list)
# print("Wa-pa-pa-pa-pa-pa-pow!" if n_list==b_list else "Woof-meow-tweet-squeek")

#https://www.acmicpc.net/problem/18242
# r,l = wow()
# n_list = []
# for _ in range(r):
#     list_list = list(inputing())
#     if "#" not in list_list:
#         continue
#     n_list.append(list_list)
# up = n_list[0]
# down = n_list[-1]
# if up.count("#") != down.count("#"):
#     if up.count("#")<down.count("#"):
#         print("UP")
#     else:
#         print("DOWN")
# else:
#     start_x = "none"
#     end_x = "none"
#     index = 0
#     for i in range(l):
#         if up[i]=="#":
#             if start_x == "none":
#                 start_x = i
#             else:
#                 index = i
#     end_x = index
#     left_cnt=0
#     right_cnt=0
#     for i in range(len(n_list)):
#         left_cnt+=1 if n_list[i][start_x] == "#" else 0
#         right_cnt+=1 if n_list[i][end_x] == "#" else 0
#     if left_cnt>right_cnt:
#         print("RIGHT")
#     else:
#         print("LEFT") 

# l = one()
# n_list = list(inputing())
# m_list = list(inputing())
# nn_list = [i for i in n_list if i not in "aeiou"]
# mm_list = [i for i in m_list if i not in "aeiou"]
# check = "yes"
# # print(nn_list,mm_list)
# if nn_list==mm_list:
#     if n_list[0]==m_list[0] and n_list[-1] == m_list[-1]:
#         if set(n_list) == set(m_list):
#             for i in set(n_list):
#                 a = n_list.count(i)
#                 b = m_list.count(i)
#                 if a != b:
#                     check="no"
#         else:
#             check="no"
#     else:
#         check = "no"
# else:
#     check = "no"
# print("YES" if check == "yes" else "NO")

#https://www.acmicpc.net/problem/14732
# r = one()
# n_list = [[0]*(501) for _ in range(501)]
# cnt = 0
# for _ in range(r):
#     a,b,aa,bb = wow()
#     for y in range(b,bb):
#         for x in range(a,aa):
#             if n_list[y][x] == 0:
#                 cnt+=1
#                 n_list[y][x]=1
# print(cnt)

#https://www.acmicpc.net/problem/21966
# l = one()
# n_list = inputing()
# if l <=25:
#     print(n_list)
# else:
#     a = n_list[11:-11]
#     if (a[-1] == "." and a.count(".")==1) or "." not in a:
#         print(n_list[:11]+"..."+n_list[-11:])
#     else:
#         print(n_list[:9]+"."*6+n_list[-10:])

#https://www.acmicpc.net/problem/4446
# str_str = list("b k x z n h d c w g p v j q t s r l m f".replace(" ",""))
# o = list("aiyeou")
# new_list = []
# for i in sys.stdin.readlines():
#     str_list = ""
#     n_list = list(i.strip())
#     for i in range(len(n_list)):
#         check ="no"
#         a = n_list[i]
#         if a.isupper():
#             check="yes"
#         if check == "yes":
#             a=a.lower()

#         if a in o:
#             index = (o.index(a)-3)
#             if check == "yes":
#                 str_list+=o[index].upper()
#             else:
#                 str_list+=o[index]
#         elif a in str_str:
#             index = (str_str.index(a)-10)
#             if check == "yes":
#                 str_list+=str_str[index].upper()
#             else:
#                 str_list+=str_str[index]    
#         else:
#             str_list+=a
#     new_list.append(str_list)
# for i in new_list:
#     print(i)
import math
r = one()
ss = inputing()
count = 0
for _ in range(r):
    a = inputing()
    for start in range(len(a)-len(ss)):
        check = "no"
        str_str = ""
        try:
            for gap in range()
            for i in range(len(ss)):
                str_str+=a[start+gap*i]
            print(start,str_str)
            if str_str == ss:
                print(a,str_str)
                check ="yes"
                count+=1
                break
        except:
            continue 
        if check == "yes":
            break
        gap+=1
print(count)
                
                

        
        


