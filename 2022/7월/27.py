import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# a=one()
# b=one()
# c=one()
# d=one()
# s=one()
# def ccc(s,x,y):
#     cnt_cnt = 0
#     index = 0
#     total = 0
#     while cnt_cnt < s:
#         if index == 0:
#             if cnt_cnt+x <= s:
#                 total+=x
#                 cnt_cnt+=x
#                 index=1
#             else:
#                 total+=s-cnt_cnt
#                 break
#         else:
#             if cnt_cnt+y <= s:
#                 total-=y
#                 cnt_cnt+=y
#                 index=0
#             else:
#                 total-=s-cnt_cnt
#                 break
#         # print("total",total,cnt_cnt)
#     return total
# aa =ccc(s,a,b)
# bb =ccc(s,c,d)        
# if aa==bb:
#     print("Tied")
# else:
#     if aa>bb:
#         print("Nikky")
#     else:
#         print("Byron")

# r = one()
# n_list = [inputing() for _ in range(r)]
# a_list = [inputing() for _ in range(r)]
# cnt = 0
# for a,b in zip(n_list,a_list):
#     if a == b:
#        cnt+=1
# print(cnt)
# t = 0#영어
# s = 0#프랑스어
# for _ in range(one()):
#     a = inputing().lower()
#     t+=a.count("t")
#     s+=a.count("s")
# if t > s:
#     print("English")
# else:
#     print("French")

# n_dict = {"A":0,"B":0}
# while True:
#     answer = inputing().split()
#     if answer[0] == "1":
#         n_dict[answer[1]]=int(answer[2])
#     elif answer[0] =="2":
#         print(n_dict[answer[1]])
#     elif answer[0] == "3":
#         n_dict[answer[1]]=n_dict[answer[1]]+n_dict[answer[2]]
#     elif answer[0] == "4":
#         n_dict[answer[1]]=n_dict[answer[1]]*n_dict[answer[2]]
#     elif answer[0] == "5":
#         n_dict[answer[1]]=n_dict[answer[1]]-n_dict[answer[2]]
#     elif answer[0] == "6":
#         n_dict[answer[1]]=int(n_dict[answer[1]]/n_dict[answer[2]])
#     else:
#         break

# a = one()
# b = one()
# c = one()
# total = one()
# cnt = 0
# for x in range(0,total+1,a):
#     for y in range(0,total+1,b):
#         for z in range(0,total+1,c):
#             if x+y+z <=total and x+y+z != 0:
#                 aa = x//a
#                 bb= y//b
#                 cc = z//c
#                 cnt+=1
#                 print(f"{aa} Brown Trout, {bb} Northern Pike, {cc} Yellow Pickerel")
# print(f"Number of ways to catch fish: {cnt}")
# r = one()
# for index in range(r):
#     a = inputing().split()
#     for i in a:
#         if len(i) == 4:
#             print("*"*4,end=" ")
#         else:
#             print(i,end=" ")
#     if index != r-1:
#         print()          
#         print()  
#     else:
#         print()
# r = one()
# for index in range(r):
#     a = inputing()
#     aa = a
#     print(a)
#     while len(a) >2:
#         b = int(a[-1])
#         a = int(a[:-1])-b
#         print(a)
#         a = str(a)
#     a = int(a)
#     if a%11 == 0:
#         print(f"The number {aa} is divisible by 11.")
#     else:
#         print(f"The number {aa} is not divisible by 11.")
#     if index != r-1:
#         print()

# for _ in range(one()):
#     n_list = list(wow())
#     gap = n_list[2]-n_list[1]
#     l = n_list[0]
#     n_list = n_list[1:]
#     new_list = [n_list[-1]+gap]
#     repeat= "yes"
#     for i in range(l-1):
#         if n_list[i+1]-n_list[i] == gap:
#             pass
#         else:
#             repeat = "no"
#     if repeat == "yes":
#         for _ in range(4):
#             new_list.append(new_list[-1]+gap)
#         print("The next 5 numbers after",n_list,"are:",new_list)
#     else:
#         print("The sequence",n_list,"is not an arithmetic sequence.")

# for _ in range(one()):
#     a,b = inputing().split()
#     b = int(b)
#     c = a[-b:]+a[:-b]
#     print(f"Shifting {a} by {b} positions gives us: {c}")
# a = inputing()
# b = ""
# for i in list(a):
#     if b == "":
#         b+=i
#     else:
#         if i != b[-1]:
#             b+=i
# print(b)           
r = one()
for index in range(1,1+r):
    l = one()
    list_list = inputing().split()
    cnt = 0
    for i in list_list:
        if i  == "sheep":
            cnt+=1
    print(f"Case {index}: This list contains {cnt} sheep.")
    if index != r:
        print()
    

