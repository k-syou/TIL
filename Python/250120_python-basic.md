# Python의 특징 및 강점

Python은 다음과 같은 특징과 강점을 가지고 있습니다:

- **쉬운 문법**: Python은 문법이 간단하고 직관적이어서 초보자도 쉽게 배울 수 있습니다.
- **풍부한 라이브러리**: 다양한 표준 라이브러리와 외부 라이브러리를 제공하여 개발 생산성을 높여줍니다.
- **다양한 용도**: 웹 개발, 데이터 분석, 인공지능, 자동화 스크립트 등 다양한 분야에서 사용됩니다.
- **플랫폼 독립성**: 운영체제에 상관없이 동일한 코드가 실행될 수 있습니다.
- **강력한 커뮤니티**: 활발한 커뮤니티가 있어 다양한 자료와 도움을 쉽게 구할 수 있습니다.

## 자료형

### int
정수를 나타내는 자료형입니다. 양수, 음수, 0을 포함합니다.
```python
a = 10
b = -5
c = 0
```

### float
실수를 나타내는 자료형입니다. 소수점을 포함한 숫자를 표현합니다.
```python
a = 10.5
b = -3.14
c = 0.0
```

### str
문자열을 나타내는 자료형입니다. 작은 따옴표(')나 큰 따옴표(")로 감싸서 표현합니다.
```python
a = 'Hello, World!'
b = "Python is fun"
c = "12345"
```

## 주소값

Python에서 변수는 객체를 가리키는 레퍼런스(참조)입니다. 각 객체는 메모리 주소를 가지고 있으며, `id()` 함수를 사용하여 해당 객체의 메모리 주소를 확인할 수 있습니다.
```python
a = 10
print(id(a))  # 변수 a가 가리키는 객체의 메모리 주소 출력

b = "Python"
print(id(b))  # 변수 b가 가리키는 객체의 메모리 주소 출력
```
주소값을 통해 변수들이 실제로 메모리에서 어떻게 관리되는지 이해할 수 있습니다.
