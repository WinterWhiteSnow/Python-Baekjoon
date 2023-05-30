# import sys
# inputing = lambda : sys.stdin.readline().rstrip()
# wow = lambda : map(int,inputing().split())
# one = lambda : int(inputing())

#https://www.acmicpc.net/problem/9251
# a,b = list(inputing()),list(inputing())
# aa,bb = len(a),len(b)
# n_list = [[0]*(aa+1) for _ in range(bb+1)]
# for y in range(1,bb+1):
#     for x in range(1,aa+1):
#         if b[y-1]==a[x-1]:
#             n_list[y][x]=n_list[y-1][x-1]+1
#         else:
#             n_list[y][x]=max(n_list[y][x-1],n_list[y-1][x])
# print(n_list[-1][-1])

# for t in range(int(input())):
#     t = t+1
#     n_list = list(map(int,input().split()))
#     l = len(n_list)
#     for i in range(l):
#         n_list[i]=max(n_list[i],40)
#     print("#"+str(t),sum(n_list)//l)

# for t in range(10):
#     t = t+1
#     l,n_list = input().split()
#     n_list = list(n_list)
#     l = int(l)
#     while True:
#         check = False
#         for i in range(len(n_list)-1):
#             a,b = n_list[i],n_list[i+1]
#             if a==b:
#                 del n_list[i]
#                 del n_list[i]
#                 check =True
#                 break
#         if check == False:
#             break
#     print("#"+str(t),"".join(n_list))
        
# for t in range(10):
#     t = int(input())
#     a = input()
#     b = input()
#     print("#"+str(t),b.count(a))    

# for t in range(int(input())):
#     t = t+1
#     r = int(input())
#     n_list = [list(map(int,list(input()))) for _ in range(r)]
#     cnt = 0
#     index = r//2
#     gap = 0
#     for i in range(r//2):
#         # print(i)
#         # print(n_list[i][index-gap:index+gap+1])
#         # print(n_list[-1-i][index-gap:index+gap+1])
#         cnt+=sum(n_list[i][index-gap:index+gap+1])
#         cnt+=sum(n_list[-1-i][index-gap:index+gap+1])
#         gap+=1
#         # print(i,cnt)
#     cnt += sum(n_list[index])
#     print("#"+str(t),cnt)

# for t in range(int(input())):
#     t=t+1
#     n,l = map(int,input().split())
#     n_list = [0]*(n+1)
#     for i in map(int,input().split()):
#         n_list[i]=1
#     print("#"+str(t),end=" ")
#     for i in range(1,n+1):
#         if n_list[i]==0:
#             print(i,end=" ")
#     print()

# n_list = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
# for t in range(int(input())):
#     t= t+1
#     a = input()
#     answer = 7-n_list.index(a)-1
#     if answer == 0:
#         answer = 7
#     print("#"+str(t),answer)

# n_list= ["..#..",".#.#.","#.D.#",".#.#.","..#.."]
# for t in range(int(input())):
#     t = t+1
#     a = input()
#     n_dict = {}
#     for i in range(5):
#         n_dict[i]=""
#     l = len(a)
#     for i in range(l):
#         for b in range(5):
#             if i == l-1:
#                 end = 5
#             else:
#                 end = 4
#             if b == 2:
#                 before = list(n_list[b][:end])
#                 before[2]=a[i]
#                 n_dict[b]+="".join(before)
#             else:
#                 n_dict[b]+=n_list[b][:end]
#     for i in range(5):
#         print(n_dict[i])
# def check(plus,list_list):
#     for y in range(100):
#         for x in range(100-plus):
#             a = list_list[y][x:x+plus+1]
#             b = a[::-1]
#             if a==b:
#                 return True
#     return False
# for t in range(10):
#     t = int(input())
#     n_list = [list(input()) for _ in range(100)]
#     n_dict = {}
#     for y in range(100):
#         for x in range(100):
#             if x not in n_dict:
#                 n_dict[x]=[n_list[y][x]]
#             else:
#                 n_dict[x]+=[n_list[y][x]]
#     a_list = list(n_dict.values())
#     state = False
#     gap = 100
#     while True:
#         if check(gap,n_list):
#             break
#         if check(gap,a_list):
#             break
#         gap-=1
#     print("#"+str(t),gap+1)

# def start(y,x):
#     num_list = []
#     # print(a_list[y][x:x+49])
#     # print(y,x)
#     # print(a_list[y][:x+1])
#     for i in range(x,x-50,-7):
#         num = "".join(a_list[y][i-6:i+1])
#         num_list.append(n_list.index(num))
#     num_list = num_list[::-1]
#     total = 0
#     for i in range(8):
#         if i%2 == 0:
#             total+=num_list[i]*3
#         else:
#             total+=num_list[i]
#     # print(num_list,sum(num_list),total)
#     if total%10 == 0:
#         return sum(num_list)
#     else:
#         return 0
# def check(r,l):
#     for y in range(r):
#         for x in range(l-1,-1,-1):
#             if a_list[y][x] == "1":
#                 answer = start(y,x)
#                 return answer

# n_list = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
# for t in range(int(input())):
#     t = t+1
#     r,l = map(int,input().split())
#     a_list = []
#     for _ in range(r):
#         list_list = list(input())
#         if set(list_list) == {"0"}:
#             continue
#         a_list.append(list_list)
#     print("#"+str(t),check(len(a_list),len(a_list[0])))

# for t in range(int(input())):
#     t = t+1
#     n_list = list(map(int,input().split()))
#     n_list.sort()
#     print("#"+str(t),end=" ")
#     if n_list[0]==n_list[1]:
#         print(n_list[-1])
#     else:
#         print(n_list[0])

# n_dict = {}
# n_dict["b"]="d"
# n_dict["q"]="p"
# n_dict["d"]="b"
# n_dict["p"]="q"
# for t in range(int(input())):
#     t = t+1
#     n = list(input())[::-1]
#     for i in range(len(n)):
#         n[i]=n_dict[n[i]]
#     print("#"+str(t),"".join(n))
    
# for t in range(int(input())):
#     t = t+1
#     n = int(input())
#     print("#"+str(t),end=" ")
#     if n%2:
#         print("Odd")
#     else:
#         print("Even")


    
    
    

    








