# 파일을 읽는 여러 가지 방법

# 1. readline 함수 이용하기
# # 파일의 첫번째 줄만 읽음
f = open("new.txt" , 'r')
line = f.readline() 
print(line)
f.close

# 모든 줄을 읽어 화면에 출력
f = open("new.txt", 'r')
while True:
    line = f.readline()
    # if문을 이용해 모든 줄을 출력한다.
    # /n도 포함되어 있기에 빈 줄도 포함된다.
    if not line: break
    print(line)
f.close
