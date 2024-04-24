### Authentication 서비스의 localID
- 사용자의 고유 식별자

### 사용자 정보 export하는 법
- Firebase CLI 설치
- 명령어: firebase auth:export users.json --format=JSON --project your_project_id

### 윈도우에 firebase CLI 설치하는 법
1. https://firebase.google.com/docs/cli?hl=ko#install-cli-windows 으로 들어간다
    - (Node.js가 설치되지 않았으면)독립 실행형 바이너리 파일을 다운받는다
        - 문제점: 터미널을 종료했다가 다시 실행하면 firebase cli가 열리지 않음
2. (Node.js가 설치되지 않았으면)NVM을 사용해서 Node.js를 설치한다
    - npm install -g firebase-tools
    - deprecated된 것들이 있다고 WARN이 뜨지만 ERROR가 아니므로 무시해도 됨
    - firebase 명령어를 입력하면 '이 시스템에서 스크립트를 실행할 수 없으므로' 경고가 뜨면서 실행이 되지 않음. 보안 오류와 UnauthorizedAccess
    - Get-ExecutionPolicy 명령어로 현재 실행 정책 확인 -> Restrited라고 설정돼있으면 Set-ExecutionPolicy RemoteSigned로 실행 정책 변경
3. 설치가 끝나면 Firebase에 로그인한다: firebase login
4. 프로젝트 나열: firebase projects:list

### FastAPI OAuth 2.0 구현 단계
- FastAPI authentication scheme setup
- Data access protection configuration
- Access authorization
    - https://dev.to/spaceofmiah/implementing-authorization-in-fastapi-a-step-by-step-guide-for-securing-your-web-applications-3b1l