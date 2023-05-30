import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/25858
# r,total = wow()
# n_list = [one() for _ in range(r)]
# s = total//sum(n_list)
# for i in n_list:
#     print(i*s)

#https://www.acmicpc.net/problem/26736
# f = inputing()
# a,b = f.count("A"),f.count("B")
# print(f"{a} : {b}")

#https://www.acmicpc.net/problem/26731
# import string
# a = set(list(inputing()))
# b = set(list(string.ascii_uppercase))
# print(list(b-a)[0])

#https://www.acmicpc.net/problem/26592
# for _ in range(one()):
#     a,b = map(float,inputing().split())
#     answer = 2*a/b
#     print(f"The height of the triangle is {answer:.2f} units")

#https://www.acmicpc.net/problem/26561
# for _ in range(one()):
#     start,time = wow()
#     start+=time//4
#     start-=time//7
#     print(start)

#https://www.acmicpc.net/problem/26546
# for _ in range(one()):
#     a,b,c = inputing().split()
#     b,c = int(b),int(c)
#     str_str = ""
#     for i in range(len(a)):
#         if b<=i<=c-1:
#             continue
#         str_str+=a[i]
#     print(str_str)

#https://www.acmicpc.net/problem/26531
# a = inputing().replace(" ","")
# x = a[:a.index("=")]
# y= a[a.index("=")+1:]
# print("YES" if eval(x)==int(y) else "NO")

#https://www.acmicpc.net/problem/26530
# for _ in range(one()):
#     cnt = 0
#     for _ in range(one()):
#         a,b,c = inputing().split()
#         b,c = float(b),float(c)
#         cnt+=b*c
#     print(f"${cnt:.2f}")

#https://www.acmicpc.net/problem/26500
# for _ in range(one()):
#     a,b = map(float,inputing().split())
#     answer = abs(b-a)
#     print(f"{answer:.1f}")

#https://www.acmicpc.net/problem/26350
# for index in range(one()):
#     n_list = list(wow())
#     n = n_list[0]
#     check = "yes"
#     n_list=n_list[1:]
#     for i in range(1,len(n_list)):
#         a,b = n_list[i],n_list[i-1]
#         if a>=2*b:
#             continue
#         check = "no"
#         break
#     if index !=0:
#         print("")
#     print(f"Denominations:",*n_list)
#     if check == "yes":
#         print("Good coin denominations!")
#     else:
#         print("Bad coin denominations! ")

#https://www.acmicpc.net/problem/26495
# n_dict = {}
# for i in sys.stdin.readlines():
#     i = i.rstrip()
#     gap = 0
#     n_list = []
#     for a in range(0,len(i),4):
#         n_list.append(i[a+gap:a+gap+4])
#         gap+=1
#     # print(n_list)
#     for i in range(len(n_list)):
#         if i not in n_dict:
#             n_dict[i]=[n_list[i].rstrip()]
#         else:
#             n_dict[i]+=[n_list[i].rstrip()]
# print(n_dict)
# n_dict = {0: ['0000', '0  0', '0  0', '0  0', '0000'], 1: ['   1', '   1', '   1', '   1', '   1'], 2: ['2222', '   2', '2222', '2', '2222'], 3: ['3333', '   3', '3333', '   3', '3333'], 4: ['4  4', '4  4', '4444', '   4', '   4'], 5: ['5555', '5', '5555', '   5', '5555'], 6: ['6666', '6', '6666', '6  6', '6666'], 7: ['7777', '   7', '   7', '   7', '   7'], 8: ['8888', '8  8', '8888', '8  8', '8888'], 9: ['9999', '9  9', '9999', '   9', '   9'], 10: ['', '', '', '', ''], 11: ['', '', '', '', ''], 12: ['', '', '', '', '']}
# index = 0
# for i in inputing():
#     i = int(i)
#     if index != 0:
#         print(" ")
#     for k in n_dict[i]:
#         print(k)
#     index+=1

#https://www.acmicpc.net/problem/27110
# a = one()
# n_list = list(wow())
# cnt = 0
# for i in n_list:
#     cnt+=min(a,i)
# print(cnt)

# str_list = []
# for i in sys.stdin.readlines():
#     i = i.rstrip()
#     str_list.append(i)

#https://www.acmicpc.net/problem/26772
# str_list = [' @@@   @@@ ', '@   @ @   @', '@    @    @', '@         @', ' @       @ ', '  @     @  ', '   @   @   ', '    @ @    ', '     @     ']
# n = one()
# for i in range(len(str_list)):
#     for _ in range(n):
#         print(str_list[i],end=" ")
#     print()

#https://www.acmicpc.net/problem/26768
# n_dict = {"a":"4","4":"a","e":"3","3":"e","i":"1","1":"i","o":"0","0":"o","s":"5","5":"s"}
# a = list(inputing())
# for i in range(len(a)):
#     # print(a[i])
#     if a[i] in n_dict:
#         a[i]=n_dict[a[i]]
# print("".join(a))

#https://www.acmicpc.net/problem/26767
# for i in range(1,one()+1):
#     if i%7 == 0:
#         if i%11 == 0:
#             print("Wiwat!")
#         else:
#             print("Hurra!")
#     else:
#         if i%11==0:
#             print("Super!")
#         else:
#             print(i)

#https://www.acmicpc.net/problem/26742
# n_dict = {}
# cnt=0
# for i in inputing():
#     if i not in n_dict:
#         n_dict[i]=1
#     else:
#         n_dict[i]+=1
#         if n_dict[i]%2 == 0:
#             cnt+=1
# print(cnt)

#https://www.acmicpc.net/problem/26340
# for i in range(one()):
#     a,b,c = wow()
#     x,y,z = a,b,c
#     for _ in range(c):
#         if a>b:
#             a//=2
#         else:
#             b//=2
#     if i != 0:
#         print()
#     print("Data set:",x,y,z)
#     print(max(a,b),min(a,b))

#https://www.acmicpc.net/problem/26332
# for _ in range(one()):
#     a,b = wow()
#     total = a*b-(2*(a-1))
#     print(a,b)
#     print(total)

#https://www.acmicpc.net/problem/25932
# for i in range(one()):
#     n_list = list(wow())
#     if i != 0:
#         print(" ")
#     print(*n_list)
#     if 18 in n_list and 17 in n_list:
#         print("both")
#     elif 18 in n_list:
#         print("mack")
#     elif 17 in n_list:
#         print("zack")
#     else:
#         print("none")

#https://www.acmicpc.net/problem/25893
# for a in range(one()):
#     cnt = 0
#     if a != 0:
#         print(" ")
#     n_list = list(wow())
#     for i in n_list:
#         if i>=10:
#             cnt+=1
#     print(*n_list)
#     if cnt == 3:
#         print("triple-double")
#     elif cnt == 2:
#         print("double-double")
#     elif cnt == 1:
#         print("double")
#     else:
#         print("zilch")

#https://www.acmicpc.net/problem/25756
# l = one()
# n_list = list(wow())
# index = 0
# state = 0
# for i in n_list:
#     a = 1-(1-(state/100))*(1-(i/100))
#     state=a*100
#     print(a*100)

#https://www.acmicpc.net/problem/26594
# a = inputing()
# for i in a:
#     print(a.count(i))
#     break

#https://www.acmicpc.net/problem/25786
# a = inputing()
# b = inputing()
# l = max(len(a),len(b))
# a = a.rjust(l,"0")
# b = b.rjust(l,"0")
# str_str = ""
# for i in range(l):
#     x,y = int(a[i]),int(b[i])
#     if x<=2 and y<=2:
#         str_str+="0"
#     elif x>=7 and y>=7:
#         str_str+="0"
#     else:
#         str_str+="9"
# print(str_str)

#https://www.acmicpc.net/problem/26645
# n = one()
# a = min(n+8,210)-n
# b = min(n+4,220)-n
# c = min(n+2,230)-n
# d = 1
# # print(a,b,c,d)
# max_max = max(a,b,c,d)
# n_list = [a,b,c,d]
# index = "none"
# for i in range(4):
#     if max_max == n_list[i]:
#         index = i
# print(index+1)

#https://www.acmicpc.net/problem/26264
# l = one()
# a = inputing()
# x,y = a.count("security"),a.count("bigdata")
# if x>y:
#     print("security!")
# elif y>x:
#     print("bigdata?")
# else:
#     print("bigdata? security!")

#https://www.acmicpc.net/problem/26040
# a = list(inputing())
# n_list = inputing().split()
# for i in range(len(a)):
#     if a[i] in n_list:
#         a[i]=a[i].lower()
# print("".join(a))







