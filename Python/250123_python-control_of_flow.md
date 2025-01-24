# Python의 반복문과 조건문

## 조건문 (Conditional Statements)

조건문은 주어진 조건에 따라 코드 블록을 실행하거나 실행하지 않도록 제어하는 데 사용됩니다. Python에서 조건문은 `if`, `elif`, `else` 키워드를 사용하여 작성합니다.

### 기본 구조

```python
if 조건식:
    # 조건식이 참일 때 실행할 코드
elif 다른_조건식:
    # 다른_조건식이 참일 때 실행할 코드
else:
    # 위의 모든 조건이 거짓일 때 실행할 코드
```

### 예제

```python
x = 10

if x > 0:
    print("x는 양수입니다.")
elif x == 0:
    print("x는 0입니다.")
else:
    print("x는 음수입니다.")
```

## 반복문 (Loops)

반복문은 특정 코드 블록을 여러 번 실행하는 데 사용됩니다. Python에서 반복문은 `for`와 `while` 두 가지가 있습니다.

### `for` 반복문

`for` 반복문은 시퀀스(리스트, 튜플, 문자열 등)의 각 요소에 대해 반복합니다.

#### 기본 구조

```python
for 변수 in 시퀀스:
    # 각 요소에 대해 실행할 코드
```

#### 예제

```python
# range
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# list
fruits = ["apple", "banana", "cherry"]
numbers = [4, 6, 10, -8, .5]

for fruit in fruits:
    print(fruit)  # apple, banana, cherry

for idx in range(len(numbers)):
    numbers[idx] *= 2
print(numbers) # [8, 12, 20, -16, 1.0]

# str
name = 'John'
for s in name:
    print(s)  # J, o, h, n

# dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}

## 키와 값을 모두 출력
for key, value in person.items():
    print(f"{key}: {value}")  # name: Alice, age: 25, city: New York

## 키만 출력
for key in person.keys():
    print(key)  # name, age, city
for key in person:
    print(key)  # name, age, city

## 값만 출력
for value in person.values():
    print(value)  # Alice, 25, New York
```
### 2중 `for` 문

2중 `for` 문은 반복문 안에 또 다른 반복문을 포함하는 구조입니다. 주로 2차원 리스트나 행렬을 처리할 때 사용됩니다.

#### 기본 구조

```python
for 변수1 in 시퀀스1:
    for 변수2 in 시퀀스2:
        # 각 요소에 대해 실행할 코드
```

#### 예제

```python
# 2차원 리스트의 모든 요소 출력
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for element in row:
        print(element, end=' ')
    print()  # 줄 바꿈
    # 1 2 3
    # 4 5 6
    # 7 8 9
```

위 예제에서는 2차원 리스트 `matrix`의 각 요소를 출력합니다. 첫 번째 `for` 문은 각 행을 반복하고, 두 번째 `for` 문은 각 행의 요소를 반복합니다.


### `while` 반복문

`while` 반복문은 조건식이 참인 동안 계속해서 코드 블록을 실행합니다.

#### 기본 구조

```python
while 조건식:
    # 조건식이 참일 때 실행할 코드
```

#### 예제

```python
count = 0

while count < 5:
    print(count) # 0, 1, 2, 3, 4
    count += 1
```

### 반복문 제어

반복문 내에서 `break`, `continue`, 그리고 `pass` 키워드를 사용하여 반복문을 제어할 수 있습니다.

- `break`: 반복문을 즉시 종료합니다.
- `continue`: 현재 반복을 건너뛰고 다음 반복을 시작합니다.
- `pass`: 아무 작업도 수행하지 않고 넘어갑니다. 주로 코드 블록이 필요하지만, 실행할 코드가 없을 때 사용됩니다.

#### 예제

```python
for i in range(10):
    if i == 5:
        break
    print(i)
# 결과: 0, 1, 2, 3, 4

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
# 결과: 1, 3, 5, 7, 9

for i in range(10):
    if i % 2 == 0:
        pass
    else:
        print(i)
# 결과: 1, 3, 5, 7, 9

count = 0
while count < 10:
    if count == 5:
        break
    print(count)
    count += 1
# 결과: 0, 1, 2, 3, 4

count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(count)
# 결과: 1, 3, 5, 7, 9

count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        pass
    else:
        print(count)
# 결과: 1, 3, 5, 7, 9
```

## 리스트 컴프리헨션 (List Comprehension)

리스트 컴프리헨션은 간결하고 효율적으로 리스트를 생성하는 방법입니다. 기존 리스트를 기반으로 새로운 리스트를 생성하거나, 조건을 만족하는 요소들로 리스트를 생성할 때 유용합니다.

### 기본 구조

```python
[표현식 for 항목 in 반복 가능한 객체 if 조건]
```

- `표현식`: 리스트의 각 요소가 될 값입니다.
- `항목`: 반복 가능한 객체의 각 요소를 나타냅니다.
- `반복 가능한 객체`: 리스트, 문자열, 튜플 등 반복 가능한 객체입니다.
- `조건` (선택 사항): 각 항목에 대해 조건을 검사하여, 조건을 만족하는 항목만 리스트에 포함됩니다.

### 예제

1. 1부터 10까지의 숫자 중 짝수만 포함하는 리스트를 생성합니다.

```python
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)  # [2, 4, 6, 8, 10]
```

2. 주어진 리스트의 각 요소를 제곱한 값을 포함하는 새로운 리스트를 생성합니다.

```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)  # [1, 4, 9, 16, 25]
```

3. 문자열 리스트에서 길이가 3 이하인 문자열만 포함하는 새로운 리스트를 생성합니다.

```python
words = ["apple", "banana", "cherry", "date"]
short_words = [word for word in words if len(word) <= 3]
print(short_words)  # ['date']
```

리스트 컴프리헨션을 사용하면 코드가 간결해지고 가독성이 높아집니다. 단, 너무 복잡한 리스트 컴프리헨션은 오히려 가독성을 해칠 수 있으므로 적절히 사용하는 것이 중요합니다.
