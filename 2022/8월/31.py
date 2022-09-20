import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())


# n,m = wow()
# n_list = list(wow())
# m_list = list(wow())
# cnt = 0
# for a in range(n):
#     for b in range(m):
#         if n_list[a]<=m_list[b]:
#             cnt+=1
# print(cnt) 

# n,m = wow()
# n_dict = {}
# for i in range(1,n+1):
#     n_dict[i]= [i]
# for _ in range(m):
#     a,b = wow()
#     n_dict[a]+=[b]
# for x,y in list(n_dict.items()):
#     print(y[-1])

# n = one()
# k= one()
# n_list = list(inputing())
# print("R" if n_list.count("R")<k else "W")

# l = one()
# n_list = inputing().replace("joi","JOI")
# print(n_list)

# l,k = wow()
# n_list = list(inputing())
# for index in range(k-1,l):
#     a = n_list[index]
#     if a.isupper():
#         n_list[index]=n_list[index].lower()
#     else:
#         n_list[index]=n_list[index].upper()
# print("".join(n_list))

# a,b = wow()
# n_list = set(list(wow()))
# m_list = set(list(wow()))
# o_list = sorted(list(n_list.intersection(m_list)))
# print(*o_list,sep="\n")

# l = one()
# right = list("IO"*(l//2)+"I")
# n_list = list(inputing())
# cnt = 0
# for a,b in zip(right,n_list):
#     if a != b :
#         cnt+=1
# print(cnt)

# s = "0"
# while len(s)<100000:
#     reverse_s = list(s)
#     reverse_s_s = ""
#     new_s = s+"0"
#     for i in reverse_s:
#         reverse_s_s+="1" if i == "0" else "0"
#     s=new_s+reverse_s_s[::-1]
# for index in range(one()):
#     a = one()
#     index = index+1
#     a = s[a-1]
#     print(f"Case #{index}: {a}")


# n_dict = {"A":1,"B":2,"D":1,"O":1,"P":1,"Q":1,"R":1}
# for _ in range(one()):
#     a = list(inputing().replace(" ",""))
#     cnt = 0
#     for i in a:
#         if i in n_dict:
#             cnt+=n_dict[i]
#     print(cnt)

# n,m = wow()
# n_list = list(wow())
# list_list = []
# for index in range(n):
#     m_list = list(wow())
#     cnt = 0
#     for a,b in zip(n_list,m_list):
#         if a==b:
#             cnt+=1
#     list_list.append([index+1,cnt])
# list_list.sort(key=lambda x : x[0])
# list_list.sort(key=lambda x : x[1],reverse=True)
# print(list_list[0][0])

# n_list =[i for i in range(1,5)]
# list_list = list(wow())
# cnt = list_list.count(0)
# set_list = [i for i in n_list if i not in list_list]
# if cnt == 1:
#     print(list_list.index(0)+1,set_list[0])
# elif cnt == 2:
#     print(*sorted(set_list))
# else:
#     print(list_list[0],list_list[1])

# a,b = inputing().split()
# b = int(b)
# if a == "residential":
#     if b == 1:
#         print(0)
#     elif 2<=b<=5:
#         print(1)
#     elif 6<=b<=10:
#         print(2)
#     elif 11<=b<=15:
#         print(3)
#     elif 16<=b<=20:
#         print(4)
# elif a == "commercial":
#     if b == 1:
#         print(0)
#     elif 2<=b<=7:
#         print(1)
#     elif 8<=b<=14:
#         print(2)
#     elif 15<=b<=20:
#         print(3)
# else:
#     if b == 1:
#         print(0)
#     elif 2<=b<=4:
#         print(1)
#     elif 5<=b<=8:
#         print(2)
#     elif 9<=b<=12:
#         print(3)
#     elif 13<=b<=16:
#         print(4)
#     elif 17<=b<=20:
#         print(5)
    
# n,m = wow()
# n_list = list(wow())
# list_list = []
# for i in range(0,len(n_list),2):
#     list_list.append(n_list[i:i+2]+[0])
# for _ in range(m):
#     num = one()
#     for i in range(len(list_list)):
#         a = list_list[i]
#         if a[a[2]] <= num:
#             list_list[i][2]=(list_list[i][2]+1)%2
# cnt = 0
# for i in list_list:
#     cnt+=i[i[2]]
# print(cnt)  

# l,m = wow()
# n_list = list(wow())
# max_max = 0
# for i in range(1,m+1):
#     max_max=max(max_max,n_list.count(i))  
# print(max_max)

# n = inputing()
# if "+" in n:
#     n = n.split("+")
#     y = int(n[0][:2])
#     if y>=20:
#         year = "18"
#     else:
#         year = "19"
# else:
#     n = n.split("-")
#     y = int(n[0][:2])
#     if y>=20:
#         year = "19"
#     else:
#         year = "20"
# print(year+n[0]+n[1])

# str_str = ""
# index = 1
# r = one()
# while len(str_str) < r:
#     str_str+=str(index**3)
#     index+=1
# print(str_str[r-1])

# l = one()
# check = "no"
# n_list = list(inputing())
# for a in range(0,l-2):
#     for b in range(a+1,l-1):
#         for c in range(b+1,l):
#             if n_list[a]+n_list[b]+n_list[c] == "IOI":
#                 check = "yes"
#                 break
#         if check=="yes":
#             break
#     if check=="yes":
#         break
# print("Yes" if check == "yes" else "No")

# n = list("SciComLove")
# index = 0
# for _ in range(one()%10):
#     n+=[n[0]]
#     n=n[1:]
# print("".join(n))

# cnt = 1
# count = 1
# for i in range(1,one()+1):
#     count*=i
#     cnt+=1/count
# print(cnt)
# price = 10001
# ind = "none"
# for index in range(one()):
#     a,b = inputing().split()
#     b = list(b)
#     a=int(a)
#     two = b.count("2")
#     zero = b.count("0")
#     wan = b.count("1")
#     # print(two,zero,wan)
#     if two >= 2 and zero >= 1 and wan >= 1:
#         if ind =="none":
#             ind = index+1
#             price = a
#         else:
#             if price > a:
#                 price = a
#                 ind = index+1 
#     # print(price,ind)
# print(ind if ind != "none" else 0)   

n_list = list(wow())
l = len(n_list)
cnt = 0
https://www.acmicpc.net/problem/15449
    






