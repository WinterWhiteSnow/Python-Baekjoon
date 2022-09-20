import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#42
# state = 10001
# for _ in range(one()):
#     a,b = wow()
#     if a>b:
#         pass
#     else:
#         state = min(b,state)
# print(state if state != 10001 else -1)

# while True:
#     r = float(inputing())
#     if r == 0:
#         break
#     answer = r+r*r+r*r*r+r*r*r*r+1
#     print(f"{answer:.2f}")

# n = one()
# a = one()
# print(int(a/2+((180-a)/2)))


