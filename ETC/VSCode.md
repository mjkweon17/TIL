### Preferences: Open Workspace Settings (JSON)
- 현재 워크스페이스에 특화된 설정을 포함하는 `settings.json` 파일을 열어줌.
- VSCode에서는 전역 설정과 워크스페이스 설정을 구분하여 관리할 수 있으며, 이 명령어는 후자에 속함

### settings.json 설정
- "editor.formatOnSave": true
    - 코드 파일을 저장할 때 자동으로 코드 포맷팅을 실행하도록 VSCode에 지시
    - 파일을 저장하는 순간에 설정된 코드 포매팅 도구(예: Prettier, Black, autopep8 등)가 자동으로 실행되어, 코드 스타일 규칙에 따라 코드가 정리됨
    - 사용 사례 및 이점
        - 코드 일관성 유지
        - 수동 포맷팅의 필요성 감고
        - 팀 프로젝트의 스타일 가이드 준수

