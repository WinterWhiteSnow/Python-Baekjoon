import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())


# a = inputing()
# b = inputing()
# cnt = 1
# for x,y in zip(a,b):
#     if x != y:
#         cnt*=2
# print(cnt)

# a = inputing()
# state = "none"
# c = 26
# d = 10
# cnt = 1
# for i in a:
#     # print(cnt,state,i)
#     if state != i:
#         c = 26
#         d = 10
#     else:
#         if stack == 26:
#             c = 25
#         else:
#             d = 9
#     if i == "c":
#         stack = c
#     else:
#         stack = d
#     cnt*=stack
#     state = i
# print(cnt)
# import string
# str_str = list(string.ascii_letters)

# a= inputing()
# b=inputing()
# c = "".join([i for i in a if i in str_str])
# print(1 if b in c else 0)

# r,l,y,x = wow()
# for _ in range(r):
#     a = inputing()
#     for _ in range(y):
#         for aa in a:
#             print(aa*x,end="")
#         print()

# r,l = wow()
# n_dict= {}
# for i in range(r):
#     a = inputing()[::-1]
#     for ii in range(l):
#         answer = a[ii]
#         if answer == "-":
#             answer = "|"
#         elif answer == "|":
#             answer= "-"
#         elif answer == "<":
#             answer = "v"
#         elif answer == ">":
#             answer = "^"
#         elif answer == "^":
#             answer = "<"
#         elif answer == "v":
#             answer = ">"
#         elif answer == "/":
#             answer = '\\'
#         elif answer == "\\":
#             answer = "/"
#         if ii not in n_dict:
#             n_dict[ii] = [answer]
#         else:
#             n_dict[ii]+=[answer]
# for i in range(l):
#     print(*n_dict[i],sep="")

# l,r = wow()
# n_list = list(wow())
# new_list = []
# for i in range(len(n_list)-r+1):
#     new_list.append(sum(n_list[i:i+r]))
# print(max(new_list))

# n_dict = {1967: ['DavidBowie'], 1969: ['SpaceOddity'], 1970: ['TheManWhoSoldTheWorld'], 1971: ['HunkyDory'], 1972: ['TheRiseAndFallOfZiggyStardustAndTheSpidersFromMars'], 1973: ['AladdinSane', 'PinUps'], 1974: ['DiamondDogs'], 1975: ['YoungAmericans'], 1976: ['StationToStation'], 1977: ['Low', 'Heroes'], 1979: ['Lodger'], 1980: ['ScaryMonstersAndSuperCreeps'], 1983: ['LetsDance'], 1984: ['Tonight'], 1987: ['NeverLetMeDown'], 1993: ['BlackTieWhiteNoise'], 1995: ['1.Outside'], 1997: ['Earthling'], 1999: ['Hours'], 2002: ['Heathen'], 2003: ['Reality'], 2013: ['TheNextDay'], 2016: ['BlackStar']}
# for _ in range(one()):
#     a,b = list(wow())
#     cnt = 0
#     key_list = []
#     for i in range(a,b+1):
#         if i in n_dict:
#             key_list+=[i]
#             cnt+=len(n_dict[i])
#     print(cnt)
#     for i in key_list:
#         for a in n_dict[i]:
#             print(i,a)

# while True:
#     r = one()
#     if r == 0:
#         break
#     max_max = 0
#     for i in range(r):
#         a = inputing()
#         if i == 0:
#             a = a.split()
#             max_max = len(a[0])
#         else:
#             a+=" "
#             for index in range(max_max,len(a)):
#                 if a[index] == " ":
#                     max_max=index
#                     break               
#     print(max_max+1)
   
# a,b,c = wow()
# a = a^b
# n_list = [a]
# for _ in range(c):
#     a = a^b
#     if a not in n_list:
#         n_list.append(a)
#     else:
#         break
# print(n_list[c%2-1])
# cnt = 0
# for _ in range(one()):
#     a,b = wow()
#     cnt+=a*b
# print(cnt)    

# start = "none"
# end = "none"
# cnt = 0
# n_list = [list(wow()) for _ in range(one())]
# n_list.sort(key=lambda x: x[0])
# for i in n_list:
#     a,b = i
#     if start == end == "none":
#         start = a
#         end = b
#     else:
#         if start<=a<=end:
#             end = max(b,end)
#         else:
#             cnt+=end-start
#             start = a
#             end = b
# print(cnt+(end-start))

# r,l = wow()
# for _ in range(r):
#     n_list = list(map(int,inputing().split()))
#     for x in range(0,len(n_list),3):
#         rr,gg,bb = n_list[x]*2126,7152*n_list[x+1],722*n_list[x+2]
#         cnt = rr+gg+bb
#         if cnt < 510000:
#             answer="#"
#         elif 510000<=cnt<1020000:
#             answer = "o"
#         elif 1020000<=cnt<1530000:
#             answer = "+"
#         elif 1530000<=cnt<2040000:
#             answer = "-"
#         elif 2040000<=cnt:
#             answer = "."
#         print(answer,end="")
#     print()

# for _ in range(one()):
#     n_dict = {}
#     for _ in range(one()):
#         a = one()
#         if a not in n_dict:
#             n_dict[a]=1
#         else:
#             n_dict[a]+=1
#     list_list = sorted(list(n_dict.items()),key=lambda x : x[0])
#     list_list.sort(key=lambda x : x[1],reverse=True)
#     print(list_list[0][0])
# n_dict = {'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 3, 'F': 3, 'G': 3, 'H': 3, 'I': 1, 'J': 1, 'K': 3, 'L': 1, 'M': 3, 'N': 3, 'O': 1, 'P': 2, 'Q': 2, 'R': 2, 'S': 1, 'T': 2, 'U': 1, 'V': 1, 'W': 2, 'X': 2, 'Y': 2, 'Z': 1}
# answer = [n_dict[i] for i in inputing()]
# while len(answer) != 1:
#     new_list = []
#     l = len(answer)
#     if l%2:
#         answer.append(0)
#     for index in range(0,len(answer),2):
#         new_list.append((answer[index]+answer[index+1])%10)
#     answer = new_list
# if answer[0]%2:
#     print("I'm a winner!")
# else:
#     print("You're the winner?")

# import string
# str_str = list(string.ascii_letters)
# index = 1
# for _ in range(one()):
#     n_dict = {}
#     for i in string.ascii_lowercase:
#         n_dict[i]=0
#     a = list(inputing())
#     for i in a:
#         if i in str_str:
#             i = i.lower()
#             n_dict[i]+=1
#     answer = min(n_dict.values())
#     if answer == 0:
#         print(f"Case {index}: Not a pangram")
#     elif answer == 1:
#         print(f"Case {index}: Pangram!")
#     elif answer == 2:
#         print(f"Case {index}: Double pangram!!")
#     else:
#         print(f"Case {index}: Triple pangram!!!")
#     index+=1
# import math
# for _ in range(one()):
#     a = one()
#     l = len(str(a))
#     index = 1
#     if l == 1:
#         print(a)
#     else:
#         while l != index:
#             b = int(str(a)[-index])
#             if b >= 5:
#                 a+=10**(index)
#                 a = int(str(a)[:-index]+"0"*index)
#             else:
#                 a = int(str(a)[:-index]+"0"*index)
#             index+=1
#         print(a)

# n = one()
# cnt = 1
# for i in range(1,n+1):
#     cnt*=i
# print(cnt)

# a = one()
# b = one()
# cnt = 0
# index = 2
# while a > 5:
#     c = int(a*(b/100))
#     if c >5:
#         cnt+=int(a*(b/100))*index
#         a = int(a*(b/100))
#         index*=2
#     else:
#         break
# print(cnt)

# l = one()
# n_list = inputing()
# new_list = [[0,0]]
# x = 0
# y = 0
# for i in n_list:
#     if i == "S":
#         y-=1
#     if i == "E":
#         x+=1
#     if i == "W":
#         x-=1
#     if i == "N":
#         y+=1
#     answer = [x,y]
#     if answer not in new_list:
#         new_list.append(answer)
# print(len(new_list))

# l = one()
# n_list = list(wow())
# state ="+"
# cnt = 0
# for i in range(l-1):
#     if n_list[i]<n_list[i+1]:
#         if state == "+":
#             pass
#         else:
#             cnt+=1
#     else:
#         if state == "+":
#             state = "-"
#         else:
#             if n_list[i]>n_list[i+1]:
#                 pass
#             else:
#                 cnt+=1
# print("YES" if cnt == 0 else "NO")
            
# while True:
#     a = one()
#     if a == -1:
#         break
#     n_list = []
#     for i in range(1,a//2+1):
#         if a%i == 0:
#             n_list.append(i)
#             n_list.append(a//i)
#     n_list = sorted(list(set(n_list)))[:-1]
#     if sum(n_list) ==a:
#         print(a,"=",end="")
#         for i in range(len(n_list)):
#             if i  == 0:
#                 print("",n_list[i],end="")
#             else:
#                 print(" + "+str(n_list[i]),end="")
#         print()
#     else:
#         print(f"{a} is NOT perfect.")

# import string
# str_str = list(string.ascii_uppercase)        
# l = one()
# n_list = inputing()
# max_max = 0
# cnt = 0
# state = 0
# for i in n_list:
#     if cnt == 0:
#         state = i
#         cnt=1
#     else:
#         gap = abs(str_str.index(i)-str_str.index(state))
#         if gap == 1:
#             cnt+=1
#             state = i
#         else:
#             max_max = max(max_max,cnt)
#             cnt = 1
#             state = i
#     # print(max_max,cnt,state)
# max_max=max(max_max,cnt)
# print("YES" if max_max >= 5 else "NO")

# r,l= wow()
# a,b,c,d = wow()
# cnt = 0
# for _ in range(r):
#     a = inputing()
#     cnt+=a.count("P")
# print(1 if cnt < c*d else "0")

# l = one()
# n_list = list(wow())
# index = 1
# cnt = 0
# for i in n_list:
#     if i == index:
#         index+=1
#     else:
#         cnt+=1
# print(cnt)

# for i in sys.stdin.readlines():
#     i = i.rstrip()
#     for index in range(0,len(i),2):
#         print(chr(int(i[index:index+2],16)),end="")
#     print()
        
num = inputing()
cnt = 0
while True:
    n = num.zfill(4)
    x = n[1:-1]
    cnt+=1
    n = str(int(x)*int(x))
    if num != n:
        num=n
    else:
        break
    
    # print(n,num)
print(cnt)


    






        