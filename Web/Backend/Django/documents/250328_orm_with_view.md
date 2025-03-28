# ORM with View

## HTTP request methods

> - 데이터에 대해 수행을 원하는 작업을 나타내는 것
>   - 서버에게 원하는 작업의 종류를 알려주는 역할
> - 클라이언트가 웹 서버에 특정 동작을 요청하기 위해 사용하는 표준 명령어
> - 대표 메서드
>   - GET, POST, PUT, DELETE ...

### GET

> 서버로부터 데이터를 요청하고 받아오는데 사용
>
> - 조회, 검색 등

#### GET 메서드의 특징

1. 데이터 전송
   * URL의 쿼리 문자열을 통해 데이터 전송
   * http:// ... /?title=제목&content=내용
2. 데이터 제한
   * URL 길이 제한이 있어서 대량의 데이터 전송에 적합하지 않음
3. 브라우저 히스토리
   * 요청 URL이 브라우저 히스토리에 남음
   * 뒤로 가기 버튼이 사용가능
4. 캐싱
   * 브라우저는 GET 요청의 응답을 로컬에 저장할 수 있음
   * 동일한 URL로 다시 요청할 때, 서버에 접속하지 않고 저장된 결과를 사용
   * 페이지 로딩 시간을 단축

#### GET 메서드 사용 예시

1. 검색 쿼리 전송
2. 웹 페이지 요청
3. API에서 데이터 조회

### POST

> 서버에 데이터를 제출하여 리소스를 변경하는 데 사용
>
> - 생성, 수정, 삭제

#### POST 메서드의 특징

1. 데이터 전송
   * HTTP Body를 통해 데이터를 전송
2. 데이터 제한
   * GET에 비해 더 많은 양의 데이터를 전송할 수 있음
3. 브라우저 히스토리
   * POST 요청은 브라우저 히스토리에 남지 않음
4. 캐싱
   * POST 요청은 기본적으로 캐시 할 수 없음
   * POST 요청이 일반적으로 서버의 상태를 변경하는 작업을 수행하기 때문

#### POST 메서드 사용 예시

1. 로그인 정보 제출
2. 파일 업로드
3. 새 데이터 생성
4. API에서 데이터 변경  요청

#### CSRF

> 사이트 간 요청 위조 "Cross-Site-Request-Forgery"
>
> 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹 페이지를
> 보안에 취약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법

- 장고에서의 사용방법

```html
<!-- templates/articles/new.html -->
...
<h1>NEW</h1>
...
<from action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    ...
```

- `csrf_token` 을 사용하여 토큰을 발급

#### Redirect

> 데이터를 저장 한 후 페이지를 응답하는 것이 아닌 기존 페이지로 보내야 함
>
> "사용자를 보낸다." -> "사용자가 GET 요청을 한번 더 보내도록 해야 한다."
>
> *서버가 강제로 해당 URL로 GET 요청을 보낸다.*

```python
from django.shortcuts import redirect

def create(request):
    ...
    return redirect('articles:detail', article.pk)
```

- `redirect(URL, *arg)` 형태로 사용
- 동작원리
  1. `POST` 요청 : Client -> Server
  2. `redirect` 응답 : Server -> Client
  3. `GET` 요청 : Client -> Server
  4. `page` 응답 : Server -> Client
