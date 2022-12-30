import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#문자열 폭발
# a = inputing()
# b = inputing() 
# stack = []
# last = b[-1]
# for i in a:
#     stack+=[i]
#     if b == "".join(stack[-len(b):]):
#         # print(stack)
#         del stack[-len(b):]
# print("".join(stack) if len(stack) != 0 else "FRULA")

r,l,k= wow()
n_list = [list(inputing()) for _ in range(r)]
white = []
black = []
for i in range(r):
    if i%2:#두번째
        white.append(list("BW"*l)[:l])
        black.append(list("WB"*l)[:l])
    else:
        white.append(list("WB"*l)[:l])
        black.append(list("BW"*l)[:l])
for y in range(r-k):
    for x in range(l-k):
        print(y,x)















