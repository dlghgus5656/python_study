from unittest import result


result = [x * y for x in range(2, 10) for y in range(1, 10)]

result = []
for x in range(2, 10):
    for y in range(1, 10):
        result.append(int(x * y))

print(result)
