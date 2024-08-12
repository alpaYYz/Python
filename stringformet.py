# 문자열 포멧

# 방법 1
print("나는 %d살입니다. " % 20)
print("나는 %s 좋아해요. " % "파이썬")
print("Apple은 %c로 시작해요. " % 'A') 

# 모두 %s로 출력가능
# 두개 이상을 하는 방법
print("나는 %s색과 %s색을 좋아해요" %('파란', '빨간'))

# 방법 2
print("나는 {}살입니다" .format(20))
# 두개 이상을 사용할때
print("나느 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
print("나느 {0}색과 {1}색을 좋아해요." .format("파란", "빨간"))
print("나느 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))


# 방법 3
# 변수 사용
print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요." .format(color = "빨간", age = 20))


# 방법 4 (v3.6 이상)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# \n 사용 enter
print("안녕하세요 \n 감사해요")

# \"\" \'\' 사용하기
print('나는 "월드클래스"입니다.')
# 햇갈리니까 이거 사용 '' 도 가능 
print("저는 \"월드클래스\"입니다")

# \\ : 문장 내에서는 \로 인식
print("\\dwd\\adwa\\adwaa\\")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

# \b : 백스페이스 (한글자 삭제) 
print("Redd\bAplle")