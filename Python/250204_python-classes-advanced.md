# Python 상속

## 1. 기본적인 상속 방법, 사용이유
상속은 기존 클래스(부모 클래스)의 속성과 메서드를 새로운 클래스(자식 클래스)가 물려받아 사용하는 것을 의미합니다. 이를 통해 코드의 재사용성을 높이고, 중복 코드를 줄일 수 있습니다.

```python
class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def display_age(self):
        print(f"I am {self.age} years old")

child = Child("Alice", 20)
child.greet()  # Hello, my name is Alice
child.display_age()  # I am 20 years old
```

## 2. 오버라이딩, 오버로딩에 대한 설명
- **오버라이딩**: 자식 클래스가 부모 클래스의 메서드를 재정의하는 것을 의미합니다. 이를 통해 자식 클래스에서 부모 클래스의 메서드를 덮어쓸 수 있습니다.

```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        print("Hello from Child")

child = Child()
child.greet()  # Hello from Child
```

- **오버로딩**: Python에서는 메서드 오버로딩을 직접 지원하지 않지만, 기본 인자를 사용하여 비슷한 효과를 낼 수 있습니다.

```python
class Example:
    def greet(self, name=None):
        if name:
            print(f"Hello, {name}")
        else:
            print("Hello")

example = Example()
example.greet()  # Hello
example.greet("Alice")  # Hello, Alice
```

## 3. 다중상속, 다중상속 시 메서드나 변수 호출 순서
다중상속은 여러 부모 클래스로부터 상속받는 것을 의미합니다. Python에서는 메서드나 변수 호출 순서를 **MRO(Method Resolution Order)**에 따라 결정합니다.

```python
class A:
    def greet(self):
        print("Hello from A")

class B:
    def greet(self):
        print("Hello from B")

class C(A, B):
    pass

c = C()
c.greet()  # Hello from A
print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
```

### MRO(Method Resolution Order) 자세한 내용

MRO(Method Resolution Order)는 다중 상속 시 메서드나 속성을 찾는 순서를 정의하는 규칙입니다. Python에서는 C3 선형화 알고리즘을 사용하여 MRO를 결정합니다. MRO는 클래스의 `__mro__` 속성을 통해 확인할 수 있습니다.

#### 다이아몬드 상속 구조

다이아몬드 상속 구조는 다음과 같이 부모 클래스가 중복되는 다중 상속 구조를 의미합니다.

```python
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")

class C(A):
    def greet(self):
        print("Hello from C")

class D(B, C):
    pass

d = D()
d.greet()  # Hello from B
print(D.__mro__)  # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
```

위 예제에서 클래스 `D`는 `B`와 `C`를 상속받고, `B`와 `C`는 `A`를 상속받습니다. 이 경우 MRO는 `D -> B -> C -> A -> object` 순서로 결정됩니다. 따라서 `d.greet()` 호출 시 `B` 클래스의 `greet` 메서드가 호출됩니다.

C3 선형화 알고리즘은 다음과 같은 규칙을 따릅니다:
1. 자식 클래스가 부모 클래스보다 먼저 온다.
2. 부모 클래스의 순서는 자식 클래스 정의에 명시된 순서를 따른다.
3. 중복되는 부모 클래스는 한 번만 나타난다.

이 규칙을 통해 다중 상속 시 메서드나 속성의 호출 순서를 명확하게 정의할 수 있습니다.


## 4. super() 사용방법 및 사용이유
`super()`는 부모 클래스의 메서드를 호출할 때 사용됩니다. 이를 통해 자식 클래스에서 부모 클래스의 메서드를 재사용할 수 있습니다.

```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello from Child")

child = Child()
child.greet()
# Hello from Parent
# Hello from Child
```

## 5. super() 사용시 상속받은 클래스가 없는 경우
`super()`를 사용했을 때 상속받은 클래스가 없으면 `super()`는 기본적으로 `object` 클래스를 호출합니다. 따라서 에러가 발생하지 않습니다.

```python
class Singleton:
    def __init__(self):
        super().__init__()  # Calls object.__init__()

singleton = Singleton()
```

## 6. 다중상속 시 super() 사용방법

다중상속 시 `super()`를 사용하면 MRO에 따라 부모 클래스의 메서드가 호출됩니다. 이를 통해 다중상속에서도 부모 클래스의 메서드를 호출할 수 있습니다.

```python
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        super().greet()
        print("Hello from B")

class C(A):
    def greet(self):
        super().greet()
        print("Hello from C")

class D(B, C):
    def greet(self):
        super().greet()
        print("Hello from D")

d = D()
d.greet()
# Hello from A
# Hello from C
# Hello from B
# Hello from D
b = B()
b.greet()
# Hello from A
# Hello from B
print(D.__mro__)  # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
```
