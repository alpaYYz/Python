# 파이썬에서 함수는 def 시작

# 함수의 구조
# def 함수명(매개변수):
#     <수행할 문장1>
#     <수행항 문장2>
#     ...
#     <수행항 문장n>
#     return 리턴값

# 1. 더하기 기능 함수
def add(a,b):
    return a+b

# 함수 사용
print(add(1,2))
# 1과 2는 argument다

#매개변수(parameter) - 함수에서 정의되어 사용되는 변수 (인자, 파라미터)
# 인수(arguments) - 함수를 호룿할 때 건네주는 변수

# 2. 입력값이 없는 함수 
def say():
    return 'hi'

a = say() # 파라미터를 넣으면 오류가 나난다 say("안녕") x
print(a)

# 3. 출력값이 없는 변수 
def add(a,b):
    print("%d, %d의 합은 %d입니다." %(a,b, a+b))

a = add(1,2)
print(a)

# 4. 입력값도 리턴값도 없는 함수
def say():
    print('Hi')

a = say()
print(a)

# 5. 매개변수 지정하기 
def sub(a,b):
    return a - b

# a = sub(3,1)
a  = sub(b =1, a = 7) # a=7전달 b=3 전달
print(a)

# 6. 파라미터 *값 사용
def add_many(*args):
    result = 0
    for i in args:
        result = result + i # *args에 입력받은 모든 값을 더한다.
    return result

print(add_many(1,2,3,4,5,6))

# 7. 두개 이상의 파라미터를 사용 한개는 여러개의 파라미터 변수 사용
# 파라미터가 몇개가 될지 모를때 사용하면 good
def add_mul(choice, *args):
    if choice == "add": # 파라미터 choice에 "add"를 입력받았을 때
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul": # 파
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul("add", 1,2,3) # choice 아규먼트만 바꿔준다.
print(result)

# 8. 키워드 매개변수, kwargs 
# kwargs는 딕셔너리 형태로 분류 한다 **kwargs

def print_kwargs(**kwargs):
    print(kwargs) # 이러면 출력값은 딕셔너리형태
    print(kwargs['a']) # 이러면 출력값은 a의 값만 

print_kwargs(a=1, b=2)

# 9. 함수의 리턴값은 언제나 하나다
def add_and_mul(a,b):
    return a+b, a*b

print(add_and_mul(3,5)) # 리턴값은 하나가 되야 하마느로 (8, 15)로 출력됨

a, b = add_and_mul(3,4)
print(a) # 리턴값은 하나 이므로 a+b 먼저 출력
print(b) # 그리고 a*b 출력

# ex
def say_myself(name, old, man = True):
    print("나의 이름은 %s입니다. " %name)
    print("나이는 %d살 입니다." %old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("홍길동", 20) # 기본값이 true이므로 매개변수를 사용하지 않으면 기본값 사용 BUT
say_myself("춘향이", 20, False) # 기본값을 지정해주면 if문을 만나서 위와 다르게 출력

# 매개변수는 순서를 맞춰서 사용해야함!!! 기본값이 지정된 파라미터는 맨 뒤에 쓸것!!!!

# return의 또다른 쓰임새
# 특별한 상황일 때 함수를 빠져나가고 싶다면 return을 단독으로 써서 함수를 즉시 빠져나갈 수 있다. 

# ex)
def say_nick(nick):
    if nick == "바보": 
        return
    print("나의 별명은 %s입니다." %nick)
# nick의 인자가 "바보"가 된다면 if문을 만나 return이 실행되어 함수가 종료
# 리턴값이 없는 함수에서 return으로 함수를 빠져나가는 방법은 실제 프로그래밍에서 자주 사용

# 10. 지역 변수와 전역 변수 사용 방법  
# 함수 안에서 선언한 변수의 효력 범위
    # 지역 변수와 전역 변수

a = 1
def vartest(a):
    a = a + 1
    print(a) 
    # vartest의 a는 함수 안에서 사용하는 변수일 뿐, 함수 밖의 변수 a와는 전혀 상관없다.

vartest(2) # 지역 변수 a가 사용되어 3 출력
print(a) # 전역 변수 a가 출력되어 1 출력

# 함수 안에서 함수 밖의 변수를 변경하는 법
    # return 사용하기 
b = 1
def vartest01(b):
    b = b + 1
    return b

b = vartest(b) # 리턴값이 대입된다
print(b)
# 하지만 vertest01의 b와 b=1의 b는 다르다

    # global 명령어 사용하기
c = 1
def vartest02():
    global c
    c = c + 1

vartest02()
print(c)
# 프로그래밍을 할 때 global 명령어는 사용하지 않는 것이 좋다.
# 함수는 독립적으로 존재하는 것이 좋기 때문이다.

# lambda 예약어
    # lambda는 함수를 생성할 때 사용하는 예약어

# 함수 이름 = lambda 파라미터1, 파라미터2.. : 파라미터를 이용한 표현식
add = lambda a, b: a+b
result = add(3,4)
print(result)