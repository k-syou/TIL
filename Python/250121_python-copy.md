# Python의 깊은 복사와 얕은 복사

Python에서 객체를 복사하는 방법에는 얕은 복사(shallow copy)와 깊은 복사(deep copy)가 있습니다.

## 얕은 복사 (Shallow Copy)

얕은 복사는 객체의 최상위 레벨만 복사하고, 중첩된 객체들은 원본 객체와 참조를 공유합니다. 얕은 복사는 `copy` 모듈의 `copy` 함수를 사용하여 수행할 수 있습니다.

```python
import copy

original_list = [1, 2, [3, 4]]
shallow_copied_list = copy.copy(original_list)

print(original_list)  # [1, 2, [3, 4]]
print(shallow_copied_list)  # [1, 2, [3, 4]]

shallow_copied_list[2][0] = 'changed'
print(original_list)  # [1, 2, ['changed', 4]]
print(shallow_copied_list)  # [1, 2, ['changed', 4]]
```

## 깊은 복사 (Deep Copy)

깊은 복사는 객체와 그 객체가 참조하는 모든 객체를 재귀적으로 복사합니다. 따라서 원본 객체와 복사된 객체는 완전히 독립적입니다. 깊은 복사는 `copy` 모듈의 `deepcopy` 함수를 사용하여 수행할 수 있습니다.

```python
import copy

original_list = [1, 2, [3, 4]]
deep_copied_list = copy.deepcopy(original_list)

print(original_list)  # [1, 2, [3, 4]]
print(deep_copied_list)  # [1, 2, [3, 4]]

deep_copied_list[2][0] = 'changed'
print(original_list)  # [1, 2, [3, 4]]
print(deep_copied_list)  # [1, 2, ['changed', 4]]
```

얕은 복사와 깊은 복사를 적절히 사용하여 코드의 성능과 메모리 사용을 최적화할 수 있습니다.