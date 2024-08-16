# 파일 읽고 쓰기

# 파일 생성하기 
# 파일을 생성하기 위해 파이썬 내장 함수 open을 사용함
# 파일 객체 = open(파일 이름, 파일 열기 모드)

f = open("new.txt", 'w')
for i in range(1,11):
    data = "%d번째 줄입니다. \n" % i
    f.write(data)
f.close

