import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1972
# while True:
#     a = inputing()
#     if a == "*":
#         break
#     index = len(a)-1
#     gap = 1
#     state = True
#     if index == 0:
#         print(f"{a} is surprising.")
#     else:
#         while gap != index:
#             list_list = {}
#             for start in range(len(a)-gap):
#                 end = a[start]+a[start+gap]
#                 if end not in list_list:
#                     list_list[end]=1
#                 else:
#                     state = False
#                     break
#             if state == False:
#                 break
#             gap+=1
#         if state:
#             print(f"{a} is surprising.")
#         else:
#             print(f"{a} is NOT surprising.")

#https://www.acmicpc.net/problem/4900
# n_list = [[] for _ in range(10)]
# n_list[0]=[0,5,3,4,1,2]
# n_list[1]=[3,1]
# n_list[2]=[0,3,6,4,2]
# n_list[3]=[0,3,6,1,2]
# n_list[4]=[5,6,3,1]
# n_list[5]=[0,5,6,1,2]
# n_list[6]=[0,5,6,1,2,4]
# n_list[7]=[0,3,1]
# n_list[8]=[0,3,6,5,1,2,4]
# n_list[9]=[0,5,3,6,1]
# n_dict = {}
# re_n_dict = {}
# for i in range(10):
#     list_list = n_list[i]
#     new_list = [0]*7
#     for ii in list_list:
#         new_list[ii]=1
#     str_str = "".join(list(map(str,new_list[::-1])))
#     n_dict[str(int(str_str,2)).zfill(3)]=i
#     re_n_dict[i]=str(int(str_str,2)).zfill(3)
# def go(num):
#     return n_dict[num]
# def gogo(list_list):
#     str_str = ""
#     for i in range(0,len(list_list),3):
#         k = list_list[i:i+3]
#         str_str+=str(go(k))
#     return int(str_str)
        
    
# while True:
#     aa = inputing()
#     if aa =="BYE":
#         break
#     a,b = aa.split("+")
#     b = b[:-1]
#     a = gogo(a)
#     b = gogo(b)
#     c = a+b
#     new_str = ""
#     # print("last",re_n_dict)
#     for i in str(c):
#         number = int(i)
#         # print("i@@@",i,number)
#         new_str+=re_n_dict[number]
#     print(aa+new_str)

#https://www.acmicpc.net/problem/2200
# l = one()
# ll = l
# n_list = list(wow())
# check = n_list.pop()
# cnt = 1
# n_list = n_list[::-1]
# minus = 0
# for i in range(len(n_list)): # 순서대로 곱,제곱,세제곱...
#     exponent=i+1-minus
#     index = n_list[i]
#     if i != ll-1:
#         if index !=0:
#             cnt+=len(str(index))+1
#             cnt+=exponent*2
#             l-=exponent
#             minus+=exponent
#     else:
#         if index != 0:
#             if index != 1:
#                 cnt+=len(str(index))+1
#             cnt+=exponent*2-1
# if check != 0:
#     if cnt == 1:
#         cnt+=len(str(check))
#     else:
#         cnt+=len(str(check))+1
# print(cnt)
























