# 패키지와 라이브러리

## 패키지
- 패키지는 여러 모듈을 하나의 디렉토리로 묶은 것
- 패키지 디렉토리에는 `__init__.py` 파일이 포함되어 있어야 함
- 예시:
    ```
    my_package/
        __init__.py
        module1.py
        module2.py
        sub_package/
            module3.py
    play.py
    ```

    ```python
    # play.py
    import my_package # __init__.py
    from my_package import module1, module2
    from my_package.sub_package import module3
    from my_package import *
    
    # 위와 같은 방법으로 호출
    ```

## 라이브러리
- 라이브러리는 특정 기능을 제공하는 모듈이나 패키지의 모음
- 다양한 기능을 제공하는 표준 라이브러리와 서드파티 라이브러리가 있음
- 예시:
    - 표준 라이브러리: `math`, `random`, `collections`, `itertools` 등
    - 서드파티 라이브러리: `requests`, `numpy`, `pandas` 등
- 서드파티 라이브러리는 `pip` 명령어를 사용하여 설치 가능
    ```sh
    pip install 라이브러리명
    pip install 라이브러리명==ver
    pip install 라이브러리명>=ver
    ```
- 설치된 패키지 및 라이브러리 확인
    ```bash
    $pip list
    Package              Version
    -------------------- -----------
    asttokens            3.0.0
    cachetools           5.5.0
    certifi              2024.12.14
    ...
    ```

---
# 서드파티 라이브러리(패키지)

## requests
- 설치:
    ```sh
    pip install requests
    ```
- 사용법:
    ```python
    import requests

    response = requests.get('https://random-data-api.com/api/v2/users')
    print(response.status_code) # 200 or 40x 등
    print(response.json()) # dictionary
    ```

## numpy
- 설치:
    ```sh
    pip install numpy
    ```
- 사용법:
    ```python
    import numpy as np

    array = np.array([1, 2, 3, 4, 5])
    print(array)
    print(np.mean(array))
    ```

## pandas
- 설치:
    ```sh
    pip install pandas
    ```
- 사용법:
    ```python
    import pandas as pd

    data = {'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]}
    df = pd.DataFrame(data)
    print(df)
    print(df.describe())
    ```

