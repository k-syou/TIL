# python module

## math
```python
import math

# 사용 예시
print(math.sqrt(16))  # 4.0
print(math.pi)        # 3.141592653589793
```

## random
```python
import random

# 사용 예시
print(random.randint(1, 10))  # 1에서 10 사이의 랜덤 정수
print(random.choice(['apple', 'banana', 'cherry']))  # 리스트에서 랜덤 선택
```

## collections
```python
from collections import deque, Counter, defaultdict, namedtuple

# 사용 예시

## deque
d = deque([1, 2, 3])
d.append(4)
d.appendleft(0)
print(d)  # deque([0, 1, 2, 3, 4])
d.pop()
d.popleft()
print(d)  # deque([1, 2, 3])

## Counter
counter = Counter('hello world')
print(counter)  # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

## defaultdict
default_dict = defaultdict(int)
default_dict['key'] += 1
print(default_dict)  # defaultdict(<class 'int'>, {'key': 1})

## namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p)  # Point(x=1, y=2)
```

## itertools
```python
import itertools

# 사용 예시

## permutations
for item in itertools.permutations([1, 2, 3]):
    print(item)  # (1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)

## combinations
for item in itertools.combinations([1, 2, 3], 2):
    print(item)  # (1, 2), (1, 3), (2, 3)

## product
for item in itertools.product([1, 2], repeat=2):
    print(item)  # (1, 1), (1, 2), (2, 1), (2, 2)

## accumulate
for item in itertools.accumulate([1, 2, 3, 4]):
    print(item)  # 1, 3, 6, 10

## chain
for item in itertools.chain([1, 2, 3], ['a', 'b', 'c']):
    print(item)  # 1, 2, 3, 'a', 'b', 'c'

## islice
for item in itertools.islice([0, 1, 2, 3, 4, 5], 2, 5):
    print(item)  # 2, 3, 4
```

## 직접 정의한 모듈
```python
# my_module.py 파일 생성
def greet(name):
    return f"Hello, {name}!"

# 사용 예시
import my_module
print(my_module.greet('World'))  # Hello, World!
```

## 코드 명시도
- `import` 문을 사용하여, 명시적으로 표현하는 것을 권장
- `from` 절을 사용하면 변수 충돌이 날 수 있다.