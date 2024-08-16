# readlines 함수 사용하기
# readlines 함수는 파일의 모든 줄을 읽어서 줄을 요소로 가지는 리스트를 리턴한다.

f = open("new.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close

# 줄 바꿈(\n) 문자 제거하기
# 파일을 읽을 때 줄 끝의 줄 바꿈(\n) 문자를 제거하고 사용해야 할 경우가 많다. 다음처럼 strip함수를 사용하면 줄 바꿈 문자를 제거할 수 있다
f = open("new.txt", 'r')
lines = f.readlines()
for line in lines:
    line = line.strip() # 줄 끝의 줄 바꿈 문자를 제거한다.
    print(line)
f.close()

