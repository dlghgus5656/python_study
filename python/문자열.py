# \ = 역슬래쉬를 사용하면 문자열에 'hi\'s' 이런식으로 써도 정상 출력이 가능하다.
# \n = 문자열에 줄바꿈 기능을 사용할 수 있다.
# """ = 로 묶으면 위 처럼 이스케이프 문자를 사용 안하고 줄바꿈이나 띄어쓰기를 문자 그대로 나타낼 수 있다.
# 문자열은 + 기호로 연결할 수 있다., *를 사용하면 안녕 * 100 하면 안녕을 100번 출력한다.

from unicodedata import name


a = "123456789"

print(type(a))
print(a[0])  # 인덱싱을 사용할 수 있다. -1은 맨 뒤를 의미한다.
# a[0:0:0] 첫번쨰 자리부터 0이상 0미만 간격은 0씩 을 의미한다. 첫 자리를 비어놓으면 처음부터 시작한다는 의미이다.
print(a[:8])  # 첫 글자부터 시작해 8번 인덱스 전 까지 출력하라는 의미이다.
print(a[::2])  # 처음부터 끝까지 2칸씩 이동하며 출력하라는 의미이다.
print(a[::-2])  # 끝부터 처음까지 2칸식 이동하며 출력하나는 의미이다.

# 포맷팅 기능을 이용한 예
number = 10
day = "three"
b = "I eat %d apples. so I was sick for %s days." % (number, day)
# %s=문자열, %c=문자1개, %d=정수, %f=소수 등등 %s 는 모든것을 문자열로 바꿔 출력해주기 때문에 만능으로 편리하게 사용할 수 있다.
print(b)

c = "Hi my name is {}".format("jon")
d = "Hi my name is {name} {age}".format(name="son", age="20")  # 이처럼 변수로 줄수도있다.
# 파이썬 3.6버전 이상부터 사용할 수 있는 예
name = "int"
e = f"나의 이름은 {name}입니다."  # 문자열 앞에 f를 사용하면 미리 선언한 변수를 .format사용없이 출력 가능하다.

print(c)
print(d)
print(e)

# 소수점 제한하는법
f = "%0.2f" % 3.12345677  # 소수점 2자리까지 출력한다. ("%0.1" = "%간격.소수점남기는 자리 수")

print(f)

# 문자 수 세기, 문자 위치 찾기
g = "happy"

print(g.count('p'))  # g변수에서 p가 몇 개 있는지(2 출력)
print(g.find('s'))  # 없는 문자를 찾을 경우 -1이 출력된다.
print(g.find('y'))
# g변수에서 y가 어느 자리에 위치해 있는지(4 출력, 같은 문자가 존재 할 경우 가장 앞에있는 문자 위치만 알려주고 끝남.)

# join
h = ",".join("abcdefg")  # 각 단어를 ,로 나눠서 출력해준다.

print(h)

# replace, split
i = "Life:is: too: short"

print(i.replace("short", "long"))  # short를 long로 교체한다.
print(i.split())  # 기준이 없으면 띄어쓰기 기준으로 리스트로 만들고 기준을 주면 기준으로 리스트를 만든다.
print(i.split(":"))
