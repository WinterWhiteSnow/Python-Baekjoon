from audioop import reverse
import sys



inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#주유소
# l = one()
# d = list(wow())
# p = list(wow())[:-1]
# d_l = len(d)
# cnt = 0
# state = "none"
# for a,b in zip(d,p):
#     if state == "none":
#         state = b
#     else:
#         state = min(state,b)
#     cnt+=a*state
# print(cnt)

# a = list(inputing())
# b = list(inputing())
# if len(a)>len(b):
#     a,b=b,a
# while len(b) != len(a):
#     if b[-1] == "A":
#         b.pop()
#     else:
#         b.pop()
#         b=b[::-1]
# print(1 if a==b else 0)

#배 골드5
l = one()
n_list = sorted(list(wow()),reverse=True)
box_l = one()
box_list = sorted(list(wow()),reverse=True)
if max(n_list) < max(box_list):
    print(-1)
else:
    cnt = 0
    while len(box_list) !=0:
        cnt+=1
        for i in range(l):
            index = 0
            while index != len(box_list)-1:
                if n_list[i]>=box_list[index]:
                    break
                else:
                    index+=1
                # print(box_list,n_list[i],box_list[index],i,index)
            if n_list[i]>=box_list[index]:
                del box_list[index]
                if len(box_list) == 0:
                    # print("wow")
                    break
    print(cnt)






