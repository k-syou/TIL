# Git 및 Bash 기초

## Git 명령어

- `git init`: 새로운 Git 저장소 초기화
- `git status`: 작업 디렉토리 상태 표시
- `git commit -m "message"`: 메시지와 함께 변경 사항 커밋
- `git log --oneline --graph --decorate --all`: 모든 로그 확인
    - `--oneline`: 각 커밋을 한 줄로 표시합니다.
    - `--graph`: 커밋 간의 관계를 그래프로 표시합니다.
    - `--decorate`: 브랜치, 태그 등의 레퍼런스를 함께 표시합니다.
    - `--all`: 모든 브랜치의 커밋을 표시합니다.

## Bash 명령어

- `pwd`: 현재 작업 디렉토리 출력
- `ls`: 디렉토리 내용 목록 표시
- `cd <directory>`: 현재 디렉토리 변경
- `mkdir <directory>`: 새 디렉토리 생성
- `rm <file>`: 파일 삭제
- `rm -rf <folder>`: 폴더 삭제
- `cp <source> <destination>`: 파일 또는 디렉토리 복사
- `mv <source> <destination>`: 파일 또는 디렉토리 이동 또는 이름 변경
- `echo <text> >> <file>`: 텍스트를 파일에 추가  
    - `>`: 파일을 새로 생성하고 텍스트를 추가합니다. 기존 파일이 있을 경우 내용을 덮어씁니다.
    - `>>`: 파일이 존재하지 않으면 새로 생성하고, 파일이 존재하면 텍스트를 파일 끝에 추가합니다.
- `cat <file>`: 파일 내용 출력