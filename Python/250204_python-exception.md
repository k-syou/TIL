# Python Exception

## Exception이란?
Exception은 프로그램 실행 중에 발생하는 예외적인 상황을 의미합니다. 이러한 예외 상황이 발생하면 프로그램의 정상적인 흐름이 중단되고, 적절한 예외 처리를 통해 프로그램이 비정상적으로 종료되지 않도록 해야 합니다.

## 대표적인 Error 종류
1. **SyntaxError**: 문법 오류가 있을 때 발생합니다.
    ```python
    print("Hello World"
    ```

2. **NameError**: 존재하지 않는 변수를 참조할 때 발생합니다.
    ```python
    print(x)
    ```

3. **TypeError**: 잘못된 타입의 객체를 사용할 때 발생합니다.
    ```python
    len(5)
    ```

4. **IndexError**: 리스트의 인덱스가 범위를 벗어날 때 발생합니다.
    ```python
    my_list = [1, 2, 3]
    print(my_list[5])
    ```

5. **KeyError**: 딕셔너리에 존재하지 않는 키를 참조할 때 발생합니다.
    ```python
    my_dict = {'a': 1}
    print(my_dict['b'])
    ```

6. **ValueError**: 연산이나 함수에 잘못된 값을 사용할 때 발생합니다.
    ```python
    int('abc')
    ```

## try / except 사용 방법
Python에서는 `try`와 `except` 블록을 사용하여 예외를 처리할 수 있습니다. `try` 블록 안에 예외가 발생할 수 있는 코드를 작성하고, `except` 블록 안에 예외가 발생했을 때 실행할 코드를 작성합니다.

```python
try:
     # 예외가 발생할 수 있는 코드
     result = 10 / 0
except ZeroDivisionError:
     # 예외가 발생했을 때 실행할 코드
     print("0으로 나눌 수 없습니다.")
```

### 여러 예외 처리하기
여러 종류의 예외를 처리하려면 여러 개의 `except` 블록을 사용할 수 있습니다.

```python
try:
     # 예외가 발생할 수 있는 코드
     my_list = [1, 2, 3]
     print(my_list[5])
except IndexError:
     print("인덱스가 범위를 벗어났습니다.")
except ZeroDivisionError:
     print("0으로 나눌 수 없습니다.")
```

### 모든 예외 처리하기
모든 예외를 한꺼번에 처리하려면 `Exception` 클래스를 사용할 수 있습니다.

```python
try:
     # 예외가 발생할 수 있는 코드
     result = 10 / 0
except Exception as e:
     print(f"예외가 발생했습니다: {e}")
```

### else와 finally 블록
`try` 블록에서 예외가 발생하지 않으면 `else` 블록이 실행되고, `finally` 블록은 예외 발생 여부와 상관없이 항상 실행됩니다.

```python
try:
     result = 10 / 2
except ZeroDivisionError:
     print("0으로 나눌 수 없습니다.")
else:
     print("예외가 발생하지 않았습니다.")
finally:
     print("이 코드는 항상 실행됩니다.")
```