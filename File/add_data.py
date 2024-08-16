# 파일에 새로운 내용 추가하기 
# 쓰기 모드('w')로 파일을 열 때 이미 존재하는 파일을 열면 그 파일의 내용이 모두 사라지게 된다.
f= open("new.txt", 'a')
for i in  range(11,20):
    data = "%d번째 줄입니다. \n" % i 
    f.write(data)
f.close()

# with 문과 함께 사용하기
# f = open("foo.txt", 'w')
# f.write("Life is too short, youneed python")
# f.close
# with 문을 사용하면 자동으로 닫아주기 때문에 close문을 사용하지 않아도 된다.
with open("foo.txt", 'w') as f:
    f.write("Life is too short, you need python")
