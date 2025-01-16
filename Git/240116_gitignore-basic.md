# .gitignore 파일

## 특징
- `.gitignore` 파일은 Git이 특정 파일이나 디렉토리를 추적하지 않도록 설정하는 파일입니다.
- 프로젝트의 루트 디렉토리에 위치하며, 하위 디렉토리에도 추가할 수 있습니다.
- 각 라인은 무시할 파일 패턴을 정의합니다.
- git에 추적되지 않으므로 추후 저장소에 저장되지 않음
- 주의사항 : 이미 추적된 파일은 .gitingnore에 추가해도 해제 되지 않아 명시적으로 파일을 해제해야 한다.
    - 이미 commit 한 경우에는 캐시에서 파일을 제거해도 이전 commit에는 남아있다.

## 사용 방법
1. `.gitignore` 파일 생성:
    ```sh
    touch .gitignore
    ```
2. 무시할 파일 패턴 추가:
    ```bash
    echo "a.txt" >> .gitignore
    echo "*.log" >> .gitignore
    echo "*.tmp" >> .gitignore
    echo "/build/" >> .gitignore
    echo "/node_modules/" >> .gitignore
    ```
    ### .gitignore 파일 예시
    ```plaintext
    a.txt
    *.log
    *.tmp
    /build/
    /node_modules/
    ```

## 이미 add 된 파일을 .gitignore에 추가할 때 처리 방법
1. `.gitignore` 파일에 무시할 파일 패턴 추가:
    ```plaintext
    # 예시
    secret.txt
    ```
2. 캐시에서 파일 제거:
    ```sh
    git rm --cached secret.txt
    ```
3. 변경 사항 커밋:
    ```sh
    git commit -m "Remove secret.txt from tracking"
    ```

## 패턴 사용 방법

`.gitignore` 파일에서 다양한 패턴을 사용할 수 있습니다:

1. `*` : 0개 이상의 문자를 대체합니다.
    ```plaintext
    *.log  # 모든 .log 파일 무시
    ```
2. `?` : 1개의 문자를 대체합니다.
    ```plaintext
    ?.txt  # a.txt, b.txt 등 1글자 이름의 .txt 파일 무시
    ```
3. `!` : 무시하지 않을 파일을 지정합니다.
    ```plaintext
    !important.log  # important.log 파일은 무시하지 않음
    ```
4. `**` : 디렉토리의 모든 하위 디렉토리를 포함합니다.
    ```plaintext
    **/temp  # 모든 temp 디렉토리 무시
    ```

### 예시
```plaintext
*.log
?.txt
!important.log
**/temp
```

## 참고 자료
- [Git 공식 문서](https://git-scm.com/docs/gitignore)
- [Pro Git 책](https://git-scm.com/book/en/v2)
