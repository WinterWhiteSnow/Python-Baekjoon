import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#49

# import math
# sosu_dict = {}
# for i in range(2,10**6):
#     if i not in sosu_dict:
#         for a in range(i,10**6,i):
#             sosu_dict[a]=0
#         sosu_dict[i]=1
# sosu_list = [a for a,b in list(sosu_dict.items()) if b == 1]
# for _ in range(one()):
#     a = one()
#     check = "no"
#     for i in sosu_list:
#         if a%i == 0:
#             if i <=10**6:
#                 check="yes"
#             break
#     if check =="yes":
#         print("NO")
#     else:
#         print("YES")

# n = list(inputing())
# l = len(n)
# cnt = 0
# index = 0
# while True:
#     if index == len(n):
#         break
    
#     if n[index].isupper():
#         if index%4 != 0:
#             cnt+=(4-index%4)
#             for _ in range(4-index%4):
#                 n.insert(index,"x")        
#     index+=1
# new_l = len(n)
# print(new_l-l)
# for _ in range(one()):
#     index = 36
#     state = 36
#     a,b,c = inputing().split()
#     while True:
#         try:
#             x,y,z = int(a,index),int(b,index),int(c,index)
            
#             if x*y==z:
#                 state = index
#             index-=1
#         except:
#             break
#     print(state if state != 36 else 0)

# index = 1

# while True:
#     r = one()
#     state = 0
#     if r == 0:
#         break
#     start_list = []
#     end_list = []
#     a_list = [inputing() for _ in range(r)]
#     for i in a_list:
#         if state == 0:
#             start_list.append(i)
#             state=1
#         else:
#             end_list.append(i)
#             state=0
#     new_list = start_list+end_list[::-1]
#     print("SET",index)
#     for i in new_list:
#         print(i)
#     index+=1
# import math
# index = 1
# while True:
#     r = one()
#     if r == 0:
#         break
#     min_min = 10001
#     state = 0
#     for _ in range(r):
#         a,b = wow()
#         c = a/2
#         total = c*c*math.pi/b
#         if state == 0:
#             state = a
#             min_min=total
#         else:
#             if min_min<total:
#                 state = a
#                 min_min=total
#     print(f"Menu {index}:",state)
#     index+=1

# while True:
#     a = inputing()
#     if a == "END":
#         break
#     b = a.split('"')[1:]
#     if len(b) == 2:
#         x,y = b
#         if " "+x ==y:
#             print(f"Quine({x})")
#         else:
#             print("not a quine")
#     else:
#         print("not a quine")

n_dict = {}
for i in list("BFPV"):
    n_dict[i]=1
for i in list("CGJKQSXZ"):
    n_dict[i]=2
for i in list("DT"):
    n_dict[i]=3
for i in list("L"):
    n_dict[i]=4
for i in list("MN"):
    n_dict[i]=5
for i in list("R"):
    n_dict[i]=6

for i in sys.stdin.readlines():
    list_list = list(i)
    new_str = ""
    state = "none"
    for a in list_list:
        if state == "none":
            if a in n_dict:
                state = n_dict[a]
                new_str+=str(n_dict[a])
            else:
                pass
        else:
            if a in n_dict:
                if state == n_dict[a]:
                    pass
                else:
                    new_str+=str(n_dict[a])            
                state = n_dict[a]
            else:
                state="none"
    print(new_str)
                
    
        



