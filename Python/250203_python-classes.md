# Python Class

## 클래스 구조

파이썬에서 클래스는 객체 지향 프로그래밍을 지원하는 기본 단위입니다. 클래스는 객체를 생성하기 위한 청사진 역할을 합니다.

### 생성자 메서드 (__init__)

생성자 메서드는 클래스가 인스턴스화될 때 호출되는 특별한 메서드입니다. 주로 객체의 초기 상태를 설정하는 데 사용됩니다.

```python
class MyClass:
    def __init__(self, value):
        self.value = value

# 클래스 인스턴스 생성
obj = MyClass(10)
print(obj.value)  # 출력: 10
```

위 예제에서 `__init__` 메서드는 `value`라는 인스턴스 변수를 초기화합니다.

### 인스턴스 변수

인스턴스 변수는 클래스의 각 인스턴스에 대해 개별적으로 유지되는 변수입니다. `self` 키워드를 사용하여 정의됩니다.

```python
class MyClass:
    def __init__(self, value):
        self.value = value

# 클래스 인스턴스 생성
obj = MyClass(20)
print(obj.value)  # 출력: 20
```

여기서 `self.value`는 인스턴스 변수입니다.

### self

`self`는 클래스의 인스턴스 자체를 참조하는 변수입니다. 클래스 내의 메서드에서 인스턴스 변수와 다른 메서드에 접근할 때 사용됩니다.

```python
class MyClass:
    def __init__(self, value):
        self.value = value

    def display_value(self):
        print(self.value)

# 클래스 인스턴스 생성 및 메서드 호출
obj = MyClass(30)
obj.display_value()  # 출력: 30
```

위 예제에서 `self.value`와 `self.display_value()`는 모두 `self`를 통해 접근됩니다.

## 메서드
### 인스턴스 메서드

인스턴스 메서드는 클래스의 인스턴스에서 호출되는 메서드입니다. 첫 번째 매개변수로 항상 `self`를 받으며, 이를 통해 인스턴스 변수와 다른 인스턴스 메서드에 접근할 수 있습니다.

```python
class MyClass:
    def __init__(self, value):
        self.value = value

    def display_value(self):
        print(self.value)

# 클래스 인스턴스 생성 및 메서드 호출
obj = MyClass(40)
obj.display_value()  # 출력: 40
# MyClass.display_value(obj) # 내부적으로는 이와 같이 수행한다.
```

위 예제에서 `display_value`는 인스턴스 메서드입니다. `self`를 통해 인스턴스 변수 `value`에 접근합니다.

### 클래스 메서드

클래스 메서드는 클래스 자체에서 호출되는 메서드입니다. 첫 번째 매개변수로 `cls`를 받으며, 이를 통해 클래스 변수와 다른 클래스 메서드에 접근할 수 있습니다. 클래스 메서드는 `@classmethod` 데코레이터로 정의됩니다.

```python
class MyClass:
    class_variable = 'Hello, World!'

    @classmethod
    def display_class_variable(cls):
        print(cls.class_variable)

# 클래스 메서드 호출
MyClass.display_class_variable()  # 출력: Hello, World!
```

위 예제에서 `display_class_variable`은 클래스 메서드입니다. `cls`를 통해 클래스 변수 `class_variable`에 접근합니다.

### 스태틱 메서드

스태틱 메서드는 클래스나 인스턴스와는 무관하게 호출되는 메서드입니다. 첫 번째 매개변수로 `self`나 `cls`를 받지 않습니다. 스태틱 메서드는 `@staticmethod` 데코레이터로 정의됩니다.

```python
class MyClass:
    @staticmethod
    def add(a, b):
        return a + b

# 스태틱 메서드 호출
result = MyClass.add(5, 7)
print(result)  # 출력: 12
```

위 예제에서 `add`는 스태틱 메서드입니다. 클래스나 인스턴스와는 무관하게 동작합니다.

### 메서드의 차이점과 사용 이유

- **인스턴스 메서드**: 인스턴스 변수에 접근하거나 인스턴스 상태를 변경할 때 사용됩니다.
- **클래스 메서드**: 클래스 변수에 접근하거나 클래스 레벨의 동작을 정의할 때 사용됩니다.
- **스태틱 메서드**: 클래스나 인스턴스와 무관한 독립적인 기능을 정의할 때 사용됩니다.

각 메서드는 특정 상황에서 유용하게 사용될 수 있으며, 객체 지향 프로그래밍의 유연성을 높여줍니다.

## 매직 메서드

매직 메서드는 특별한 이름을 가진 메서드로, 파이썬의 특정 동작을 정의하거나 변경할 수 있습니다. 주로 두 개의 밑줄(`__`)로 시작하고 끝납니다.

### 주요 매직 메서드

- `__init__(self, ...)`: 객체 초기화 메서드로, 인스턴스 생성 시 호출됩니다.
- `__str__(self)`: 객체의 문자열 표현을 반환하며, `print()` 함수 호출 시 사용됩니다.
- `__repr__(self)`: 객체의 공식 문자열 표현을 반환하며, 주로 디버깅에 사용됩니다.
- `__len__(self)`: 객체의 길이를 반환하며, `len()` 함수 호출 시 사용됩니다.
- `__eq__(self, other)`: 두 객체의 동등성을 비교하며, `==` 연산자 호출 시 사용됩니다.

### 예제

```python
class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'MyClass with value {self.value}'

    def __eq__(self, other):
        return self.value == other.value

obj1 = MyClass(10)
obj2 = MyClass(10)
print(obj1)  # 출력: MyClass with value 10
print(obj1 == obj2)  # 출력: True
```

위 예제에서 `__str__` 메서드는 객체의 문자열 표현을 정의하고, `__eq__` 메서드는 두 객체의 동등성을 비교합니다.

매직 메서드는 객체의 동작을 커스터마이징하고, 파이썬의 다양한 기능을 활용할 수 있게 해줍니다.

## 데코레이터

데코레이터는 함수를 수정하거나 확장할 때 사용되는 함수입니다. 데코레이터는 다른 함수를 인수로 받아서 새로운 함수를 반환합니다. 주로 함수나 메서드의 동작을 변경하거나 확장하는 데 사용됩니다.

### 데코레이터 작성법

데코레이터는 함수를 중첩하여 작성할 수 있습니다. 아래는 간단한 데코레이터 예제입니다.

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

위 예제에서 `my_decorator`는 `say_hello` 함수를 감싸서 추가 동작을 수행합니다.

### 기본적으로 정의되어 있는 데코레이터

파이썬에는 몇 가지 기본적으로 정의된 데코레이터가 있습니다.

#### @staticmethod

스태틱 메서드를 정의하는 데 사용됩니다. 클래스나 인스턴스와 무관하게 동작합니다.

```python
class MyClass:
    @staticmethod
    def my_static_method():
        print("This is a static method.")
```

#### @classmethod

클래스 메서드를 정의하는 데 사용됩니다. 첫 번째 매개변수로 `cls`를 받습니다.

```python
class MyClass:
    @classmethod
    def my_class_method(cls):
        print("This is a class method.")
```

#### @property

프로퍼티를 정의하는 데 사용됩니다. 객체의 속성처럼 접근할 수 있는 메서드를 정의합니다.

```python
class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value
```

위 예제에서 `value`는 프로퍼티로 정의되어, `obj.value`와 같은 방식으로 접근할 수 있습니다.

데코레이터는 코드의 재사용성을 높이고, 함수나 메서드의 동작을 쉽게 변경할 수 있게 해줍니다.