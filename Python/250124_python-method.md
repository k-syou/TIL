# Python Method 정리

## Method와 Function의 차이점

- **Function**: 독립적으로 호출될 수 있는 코드 블록입니다. 입력값을 받아서 특정 작업을 수행하고 결과를 반환합니다.
- **Method**: 특정 객체에 속한 함수로, 객체의 상태를 변경하거나 객체와 관련된 작업을 수행합니다. 메서드는 항상 객체를 통해 호출됩니다.

## 대표적인 자료형의 Method

### 📜 문자열 (str)

- **`str.upper()`**: 문자열을 모두 대문자로 변환합니다.
    ```python
    text = "hello"
    print(text.upper())  # "HELLO"
    ```

- **`str.lower()`**: 문자열을 모두 소문자로 변환합니다.
    ```python
    text = "HELLO"
    print(text.lower())  # "hello"
    ```

- **`str.replace(old, new)`**: 문자열 내의 특정 부분을 다른 문자열로 교체합니다.
    ```python
    text = "hello world"
    print(text.replace("world", "Python"))  # "hello Python"
    ```

### 🔢 정수 (int)

- **`int.bit_length()`**: 정수를 2진수로 나타냈을 때 필요한 비트 수를 반환합니다.
    ```python
    number = 10
    print(number.bit_length())  # 4
    ```

- **`int.to_bytes(length, byteorder)`**: 정수를 지정된 길이와 바이트 순서로 바이트 객체로 변환합니다.
    ```python
    number = 1024
    print(number.to_bytes(2, byteorder='big'))  # b'\x04\x00'
    ```

### 📋 리스트 (list)

- **`list.append(item)`**: 리스트의 끝에 항목을 추가합니다.
    ```python
    fruits = ["apple", "banana"]
    fruits.append("cherry")
    print(fruits)  # ["apple", "banana", "cherry"]
    ```

- **`list.remove(item)`**: 리스트에서 첫 번째로 일치하는 항목을 제거합니다.
    ```python
    fruits = ["apple", "banana", "cherry"]
    fruits.remove("banana")
    print(fruits)  # ["apple", "cherry"]
    ```

- **`list.pop([index])`**: 지정된 인덱스의 항목을 제거하고 반환합니다. 인덱스를 지정하지 않으면 마지막 항목을 제거하고 반환합니다.
    ```python
    fruits = ["apple", "banana", "cherry"]
    fruit = fruits.pop()
    print(fruit)  # "cherry"
    print(fruits)  # ["apple", "banana"]
    ```

- **`list.sort()`**: 리스트를 정렬합니다. 원본 리스트를 변경합니다.
    ```python
    numbers = [3, 1, 2]
    numbers.sort()
    print(numbers)  # [1, 2, 3]
    ```

- **`sorted(list)`**: function 이며, 리스트를 정렬한 새로운 리스트를 반환합니다. 원본 리스트는 변경되지 않습니다.
    ```python
    numbers = [3, 1, 2]
    sorted_numbers = sorted(numbers)
    print(sorted_numbers)  # [1, 2, 3]
    print(numbers)  # [3, 1, 2]
    ```



이와 같이 Python의 다양한 자료형에는 유용한 메서드들이 많이 존재합니다. 각 자료형의 메서드를 잘 활용하면 더 효율적이고 간결한 코드를 작성할 수 있습니다.