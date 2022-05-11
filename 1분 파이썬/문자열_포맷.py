
# 문자열 출력

python = "파이썬"
java = '자바'

print(python, java)

# 문자열 포맷

# 1. {} + format
print('개발 언어에는 {}, {} 등이 있어요'.format(python, java))

# 2. {숫자} + format
print('개발 언어에는 {1}, {0} 등이 있어요'.format(python, java))

# 3. f-string
print(f'개발 언어에는 {python}, {java} 등이 있어요')
