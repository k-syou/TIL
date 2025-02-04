# 절차지향과 객체지향의 차이점과 장단점

## 객체란 무엇인가?
객체는 데이터와 그 데이터를 조작하는 메서드를 하나로 묶은 프로그래밍 구성 요소입니다. 객체는 클래스의 인스턴스로, 클래스는 객체를 생성하기 위한 청사진 또는 템플릿 역할을 합니다. 객체는 상태(속성)와 행동(메서드)을 가지며, 이를 통해 프로그램의 구조와 동작을 정의합니다.

### 객체의 구성 요소
- **속성 (Attributes)**: 객체의 상태를 나타내는 변수입니다.
- **메서드 (Methods)**: 객체의 행동을 정의하는 함수입니다.

### 예시
```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The {self.year} {self.make} {self.model}'s engine has started.")

my_car = Car("Toyota", "Corolla", 2020)
my_car.start_engine()  # 출력: The 2020 Toyota Corolla's engine has started.
```
위 예시에서 `Car` 클래스는 `make`, `model`, `year`라는 속성과 `start_engine`이라는 메서드를 가진 객체를 생성합니다. `my_car`는 `Car` 클래스의 인스턴스입니다.

## 절차지향 프로그래밍
절차지향 프로그래밍은 순차적으로 명령을 실행하는 방식으로 프로그램을 작성하는 방법입니다.

### 장점
- 코드가 직관적이고 이해하기 쉽습니다.
- 작은 프로그램에 적합합니다.

### 단점
- 코드의 재사용성이 낮습니다.
- 유지보수가 어렵습니다.
- 대규모 프로그램에 적합하지 않습니다.

## 객체지향 프로그래밍
객체지향 프로그래밍은 객체를 중심으로 프로그램을 작성하는 방법입니다.

### 장점
- 코드의 재사용성이 높습니다.
- 유지보수가 용이합니다.
- 대규모 프로그램에 적합합니다.

### 단점
- 초기 설계에 많은 시간이 소요됩니다.
- 절차지향에 비해 복잡합니다.

# Python에서 절차지향과 객체지향 코드 예시

## 절차지향 코드 예시
```python
# 절차지향 방식으로 두 점 사이의 거리 계산
import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

x1, y1 = 0, 0
x2, y2 = 3, 4
distance = calculate_distance(x1, y1, x2, y2)
print(f"Distance: {distance}")
```

## 객체지향 코드 예시
```python
# 객체지향 방식으로 두 점 사이의 거리 계산
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)

point1 = Point(0, 0)
point2 = Point(3, 4)
distance = point1.distance_to(point2)
print(f"Distance: {distance}")
```

# Python에서의 객체지향 코드의 특이점과 장단점

## 특이점
- Python은 동적 타이핑 언어로, 객체의 속성과 메서드를 런타임에 추가할 수 있습니다.
- 다중 상속을 지원합니다.
- 메타클래스를 사용하여 클래스의 동작을 제어할 수 있습니다.

## 장점
- 코드의 재사용성과 유지보수성이 높습니다.
- 다형성과 상속을 통해 코드의 확장성이 뛰어납니다.
- 캡슐화를 통해 데이터의 은닉이 가능합니다.

## 단점
- 절차지향에 비해 초기 설계와 구현이 복잡합니다.
- 성능이 절차지향에 비해 떨어질 수 있습니다.
- 작은 프로그램에서는 오히려 비효율적일 수 있습니다.

## Python에서의 인스턴스와 메서드

### 인스턴스
- 클래스는 객체를 생성하기 위한 청사진이며, 인스턴스는 클래스에서 생성된 구체적인 객체입니다.
- 각 인스턴스는 클래스의 속성과 메서드를 상속받으며, 독립적인 상태를 가질 수 있습니다.

### 메서드
- 메서드는 클래스 내부에 정의된 함수로, 인스턴스의 상태를 조작하거나 동작을 정의합니다.
- 인스턴스 메서드는 첫 번째 매개변수로 항상 `self`를 받아, 호출된 인스턴스 자신을 참조합니다.

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof!")

my_dog = Dog("Buddy")
my_dog.bark()  # 출력: Buddy says woof!
```

## 기본 자료형에서의 인스턴스와 메서드

### str 인스턴스와 메서드
- `str` 클래스는 문자열을 나타내는 클래스입니다.
- 문자열 인스턴스는 다양한 메서드를 통해 조작할 수 있습니다.

```python
my_string = "Hello, World!"
print(my_string.upper())  # 출력: HELLO, WORLD!
print(my_string.replace("World", "Python"))  # 출력: Hello, Python!
```

### list 인스턴스와 메서드
- `list` 클래스는 리스트를 나타내는 클래스입니다.
- 리스트 인스턴스는 다양한 메서드를 통해 조작할 수 있습니다.

```python
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print(my_list)  # 출력: [1, 2, 3, 4, 5, 6]
my_list.remove(3)
print(my_list)  # 출력: [1, 2, 4, 5, 6]

[1,2,3].sort()
# ==> 리스트.정렬()
# ==> 객체.행동()
# ==> 인스턴스.메서드()
```
