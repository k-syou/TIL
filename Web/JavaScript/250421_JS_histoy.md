# JavaScript History

## JavaScript 역사 타임라인

### 1995 – 탄생: 브렌던 아이크(Brendan Eich)

- **회사:** 넷스케이프 (Netscape)
- **목표:** 웹 페이지에 동적인 기능을 추가하기 위한 스크립트 언어 개발
- **개발 과정 중 이름:** Mocha → LiveScript → **JavaScript**
- *주의: Java와는 관계 없는 언어지만, 당시 Java의 인기를 고려한 마케팅 전략으로 명명됨.*

### 1996 – Microsoft의 JScript 출시

- Internet Explorer에 Microsoft의 자체 JavaScript 구현 버전인 JScript 탑재
- 브라우저 간 호환성 문제 및 표준화 필요성 대두

### 1997 – ECMAScript 표준화 (ES1)

- 브라우저별 JavaScript 구현 차이 해소를 위해 ECMA International에서 표준화 진행
- 표준 명칭: **ECMAScript(ES)**

### 1999 – ES3

- `try...catch`, 정규표현식, `switch`, `do...while` 등 주요 기능 추가
- 당시 웹 환경에서 널리 사용된 버전

### 2000~2007 – 언어 발전 정체기

- **AJAX** 기술 등장 외 큰 변화는 없었음
- JavaScript는 주로 **폼 유효성 검사, 간단한 UI 조작** 등에 제한적으로 사용됨

### 2008 – Google V8 엔진 등장

- Google Chrome 브라우저와 함께 고성능 JavaScript 엔진 **V8** 출시
- **JIT(Just-In-Time) 컴파일** 도입으로 실행 속도 향상
- **Node.js** 개발의 기반 마련

### 2009 – Node.js 출시

- V8 엔진 기반의 서버사이드 JavaScript 런타임 환경
- JavaScript를 이용한 서버 개발 및 풀스택 개발 가능성 제시
- 비동기 I/O, 이벤트 기반 모델 특징

### 2015 – ES6 (ECMAScript 2015)

- 대규모 언어 업데이트
- 주요 추가 기능:
  - `let`, `const` (변수 선언)
  - 화살표 함수 (`arrow function`)
  - `class` (클래스 문법)
  - `Promise` (비동기 처리)
  - 모듈 시스템 (`import`/`export`)
  - `Map`, `Set` 등
- 현대 JavaScript 개발 패러다임의 시작

### 2016~현재 – 연 단위 업데이트 (ES7, ES8...)

- ECMAScript는 매년 새로운 버전 발표
- 주요 추가 기능 예시:
  - ES7 (2016): `Array.prototype.includes()`, 거듭제곱 연산자 (`**`)
  - ES8 (2017): `async/await` (비동기 함수)
  - ES9 (2018) 이후: Optional Chaining (`?.`), Nullish Coalescing (`??`), Top-level `await` 등

### 현재 – JavaScript 적용 분야 확장

- 웹 프론트엔드 (SPA 등)
- 웹 백엔드 (Node.js)
- 모바일 앱 개발 (React Native 등)
- 데스크탑 애플리케이션 (Electron 등)
- 머신러닝 (TensorFlow.js 등)
- 기타: IoT, 게임 개발, 브라우저 확장 프로그램 등

## 요약 타임라인

| 연도 | 주요 이벤트                                   |
|------|-----------------------------------------------|
| 1995 | JavaScript 탄생 (Netscape, Brendan Eich)      |
| 1997 | ECMAScript 표준화 시작 (ES1)                  |
| 1999 | ES3 출시 (주요 기능 추가)                     |
| 2008 | Google Chrome 및 V8 엔진 출시                 |
| 2009 | Node.js 출시 (서버사이드 JS)                |
| 2015 | ES6 (ES2015) 출시 (대규모 업데이트)           |
| 2016~ | 매년 ECMAScript 신규 버전 발표              |
| 현재 | 웹 전반 및 다양한 애플리케이션 분야에서 활용 |

## JavaScript 구현 언어

> JavaScript 언어 자체는 **고급 스크립트 언어**로 설계되었으며, 이 언어를 해석하고 실행하는 **JavaScript 엔진**은 주로 **C++**로 구현됩니다.

### 대표적인 JavaScript 엔진

| 엔진 이름        | 주요 사용처              | 구현 언어 | 특징                             |
|----------------|------------------------|-----------|----------------------------------|
| **V8**         | Chrome, Edge, Node.js  | C++       | 빠른 실행 속도, JIT 컴파일        |
| **SpiderMonkey** | Firefox                | C++       | 최초의 JavaScript 엔진           |
| **JavaScriptCore** | Safari                 | C++       | Apple에서 개발 (Nitro 엔진)     |
| **Chakra (Legacy)** | Internet Explorer (구) | C++       | 현재는 V8 기반으로 전환됨       |

### JavaScript 코드 실행 과정 (엔진 내부)

1. JavaScript 코드 파싱 (Parsing)
2. 추상 구문 트리 (AST) 생성
3. 바이트코드 (Bytecode) 변환
4. JIT 컴파일을 통해 기계어 코드 생성 (필요시)
5. 실행 (Execution)

> *이 과정은 C/C++로 구현된 엔진 내부에서 처리됩니다.*

## 요약

> JavaScript는 C++ 등으로 구현된 **실행 엔진** 위에서 동작하는 **고급 스크립트 언어**입니다.

---
