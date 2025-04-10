## ForeignKey

```python
from django.db import models
from django.conf import settings


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

1. User 객체의 경우 settings.AUTH_USER_MODEL (문자열) 형식으로 등록
2. Aritcle 과 같은 다른 객체의 경우 해당 객체 자체를 넣음
3. 필드명은 자동으로 <클래스명>_id 형태로 생성됨
4. 역참조의 경우 article.<클래스명>_set 으로 자동 설정됨

   * ForeignKey 속성 중 related_name 속성을 설정하면 역참조시 이름을 설정할 수 있음
5. on_delete 속성은 부모의 객체가 삭제 될때 어떻게 처리할 건지 속성을 지정함

   1. CASCADE : 부모 요소가 삭제되면 자기 자신(row)도 삭제함
   2. PROTECT : 해당 요소가 같이 삭제되지 않도록 Proteced Error를 발생
   3. SET_NULL : 부모 요소가 삭제되면 해당 필드를 NULL 값으로 설정
   4. SET_DEFAULT : 부모 요소가 삭제되면 해당 필드의 default 값으로 설정
      * 단, default 값이 설정되어 있어야 함
   5. SET(func) : 부모 요소가 삭제되면 func을 실행하여 키로 설정함
      * 해당 함수의 반환값은 부모 요소여야 함
   6. DO_NOTHING : 부모 요소가 삭제되어도 유지
      * 무결성을 해칠 위험이 있어 잘 사용하지 않는다

## Decorator

1. `@login_required`

   * 로그인이 되어있지 않은 상태에서 요청 시 로그인 페이지로 이동
   * accounts:login
2. `@require_http_methods`

   * `@require_http_methods([<method>...])` 형태로 사용
   * 정의된 method 형태로만 요청이 가능하며 다른 요청이 들어오면 405 에러 발생
3. `@require_safe`

   * GET, HEAD method 형태로만 요청이 가능
4. `@require_POST`

   * POST method 형태로만 요청이 가능
5. `@require_GET`

   * GET method 형태로만 요청이 가능
   * 해당 데코레이터 대신 `require_safe`를 사용하는 것을 권장

```python
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_GET, require_POST, require_safe

@login_required
# @require_safe
@require_http_methods(['GET', 'POST'])
def index(request):
    ...
```
