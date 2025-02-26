### OOCSS (Object-Oriented CSS)

OOCSS(Object-Oriented CSS)는 CSS를 모듈화하고 재사용성을 높이기 위한 방법론입니다. OOCSS는 스타일을 객체 단위로 나누어 관리함으로써 코드의 중복을 줄이고 유지보수를 쉽게 합니다. 주요 원칙은 다음과 같습니다:

1. **구조와 스킨의 분리**: 레이아웃과 디자인을 분리하여 각각 독립적으로 관리합니다.
2. **컨테이너와 콘텐츠의 분리**: 컨테이너와 그 안의 콘텐츠를 분리하여 재사용성을 높입니다.

이 방법론을 통해 CSS 코드의 일관성을 유지하고, 확장성과 유지보수성을 향상시킬 수 있습니다.

### 예시

다음은 OOCSS의 원칙을 적용한 예시입니다.

#### HTML
```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    /* 기본 Card 구조 */
    .card {
      border: 1px solid #ccc;
      border-radius: 4px;
      padding: 16px;
      width: 50%;
    }

    /* Card 제목 */
    .card-title {
      font-size: 20px;
      font-weight: bold;
      margin-bottom: 8px;
    }

    /* Card 설명 */
    .card-description {
      font-size: 16px;
      margin-bottom: 16px;
    }

    /* 기본 버튼 구조 */
    .btn {
      display: inline-block;
      border-radius: 4px;
      padding: 8px 16px;
      font-size: 1rem;
      font-weight: 400;
      color: #212529;
      text-align: center;
      text-decoration: none;
      cursor: pointer;
    }

    /* 파란 배경 버튼 */
    .btn-blue {
      background-color: #007bff;
      color: #fff;
    }

    /* 빨간 배경 버튼 */
    .btn-red {
      background-color: #cb2323;
      color: #fff;
    }
  </style>
</head>

<body>
  <div class="">
    <p class="">Card Title</p>
    <p class="">This is a card description.</p>
    <button class="">Learn More</button>
    <button class="">Learn More</button>
  </div>
</body>

</html>

```