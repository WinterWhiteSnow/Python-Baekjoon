import sys
sin = sys.stdin
sout = sys.stdout
serr = sys.stderr
  
num = sout.write('문자를 입력하시오\n')  #'문자를 입력하시오'출력
sout.write(str(num)+'개의 문자 출력됨\n')  #띄어쓰기와 줄바꿈까지 포함하여 '문자를 입력하시오\\n' 총 10개의 문자가 출력됨을 출력
s = sin.read(4)  #read(size==len?):입력 스트림에서 size만큼만 읽음. 일종의 버퍼.
sout.write('입력받은 값:'+s+'\n')  #'가나다라마바사'를 위에서 입력했을 때 결과로 '입력받은 값:가나다라' 출력
sout.write('한줄을 입력하시오\n')  #입력메시지 출력
sin.readline()  #입력받음
s = sin.readline()  #위 입력값을 s에 저장
sout.write('입력받은 값:'+s+'\n')  #입력값 출력
serr.write('에러 메시지')  #에러 메시지 출력. 다만 에러출력은 버퍼가 없기 때문에 바로 윗줄보다 에러 메시지가 먼저 출력되는 현상 발생


flush => 기다렸다가 전부 입력되면 실행해준다?








