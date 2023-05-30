import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

n = one()
a = int(n**(1/2))+1
x,y,z = 10**6,10**6,10**6
for i in range(1,a):
    for ii in range(1,a):
        if n%(i*ii) == 0:
            iii = n//(i*ii)
            if 2*((x*y)+(y*z)+(z*x)) > 2*((i*ii)+(ii*iii)+(i*iii)):
                x,y,z=i,ii,iii
print(x,y,z)













