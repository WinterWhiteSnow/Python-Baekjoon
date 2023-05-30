import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

from decimal import Decimal
total,garo,sero,height=wow()
start = 1
end = max(garo,sero,height)
while start<end:
    mid = (start+end)/2
    cnt = (garo//mid)*(sero//mid)*(height//mid)
    if cnt<total:
        if end != mid:
            end=mid
        else:
            break
    else:
        if start!=mid:    
            start=mid
        else:
            break
if "." in str(start):
    start = f"{start:.9f}" if len(str(start)[str(start).index(".")+1:])<=9 else str(start)
else:
    start = str(start)+"."+"0"*9
    # print(cnt,start,end)
if "." in str(end):
    end = f"{end:.9f}" if len(str(end)[str(end).index(".")+1:])<=9 else str(end)
else:
    end = str(end)+"."+"0"*9
start,end = Decimal(start),Decimal(end)
total,garo,sero,height = map(Decimal,[total,garo,sero,height])
total = float(total)
# print("end!!",start,end)
# print("start",int(garo/start)*int(sero/start)*int(height/start))
# print(float((garo//end)*(sero//end)*(height//end)),float((garo//start)*(sero//start)*(height//start)))
print(int((garo//end)*(sero//end)*(height//end))>=total, int((garo//start)*(sero//start)*(height//start))>=total)
if int((garo//end)*(sero//end)*(height//end))>=total and int((garo//start)*(sero//start)*(height//start))>=total:
    print(start if float(start)>float(end) else end)
else:
    # print("wiow")
    # print(end,start)
    print(end if int((garo//end)*(sero//end)*(height//end))>=total else start)












