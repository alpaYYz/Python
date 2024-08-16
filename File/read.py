# read 함수 사용하기 
# f.read()는 파일의 내용 전체를 문자열로 리턴한다. 따라서 위 예의 data는 파일 전체 내용이다.
f = open("new.txt", 'r')
data = f.read()
print(data)
f.close