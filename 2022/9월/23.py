from re import L
import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

for _ in range(one()):
    a = inputing()
    if a == a[::-1]:
        print(1)
    else:
        a = int(a)
        check = "no"
        for i in range(2,65):
            n_list = []
            num = a
            while num != 0:
                n_list.append(num%i)
                num//=i
            if n_list == n_list[::-1]:
                print(1)
                check ="yes"
                break
        if check == "no":
            print(0)










