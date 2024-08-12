# 문자열 처리함수

# 1. 대문자를 소문자로 변환 : .lower()
python = "Python is Amazing"
print(python.lower())

# 2. 소문자를 대문자로 변환 : .upper
print(python.upper())

# 3. 인덱스 주소의 값이 대문자인지 알려주는 값 : isupper() -> true, false 출력
print(python[0].isupper()) 

# 4. 인덱스 주소의 값이 소문자인지 알려주는 값 : islower()
print(python.islower())

# 5. 문자열의 길이를 알려주는 값 : len(문자열)
print(len(python))

# 6. 문자열 바꾸기
print(python.replace("Python", "Java"))

# 7. 문자의 인덱스번호를 알 수 있음 : .index("값") -> 어디 인덱스값에 있나 확인 가능
index = python.index("n")
# 중복일 경우 앞에 있는 인덱스 값을 가져옴 
print(index)
# 두번쨰 값을 찾을 경우에 이렇게 한다
index = python.index("n", index + 1)
print(index)

# 8. find("값") 위와 같음 -> 값이 없느 경우 -1를 반환함
print(python.find("Java")) # -1
# print(python.index("java")) # 오류

# 9. 원하는 문자열을 몇 번 출력하는지 알 수 있는 함수 : .count
print(python.count("n")) 
