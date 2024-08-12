# 규칙1 : http:\\ 부분은 제위 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e'갯수 + "!"로 구성

web = "http:\\\\naver.com"
print(web)

my_str = web.replace("http:\\\\", "")
print(my_str)

pswd = len(web)
print(pswd)

pswdn = web[7:12]
print(pswdn)
pswdnav = pswdn[0:3]
print(pswdnav)
pswdlen = len(pswdn)
print(pswdlen)
pswdecount = pswdn.count("e")
print(pswdecount)

print(pswdnav + str(pswdlen) + str(pswdecount) + "!")
