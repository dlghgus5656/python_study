''' 메소드 (Method)
        = 클래스 내에 정의된 어떤 동작, 기능을 하는 고드들의 묶음

    문자열.메소드(...)
'''


letter = 'how are YOU?'

# 모든 내용을 소문자로
print(letter.lower())

# 모든 내용을 대문자로
print(letter.upper())

# 첫 글자만 대문자로
print(letter.capitalize())

# 각 단어들의 첫 글자만 대문자로
print(letter.title())

# 대소문자를 뒤바꾸려면
print(letter.swapcase())

# 문자열을 나누려면
print(letter.split())

# 단어가 몇 번 쓰였는지 알려면
print(letter.count('how'))
