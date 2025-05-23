# ❌ 해당 프로젝트는 중단되어, 자동화 테스트 스크립트 유지보수 및 추가를 하지않습니다.


# 테스트 자동화 프로젝트
> 이 프로젝트는 솔루션 Motion M GUI 체크리스트 자동화 기능 검증 수행하기 위해 구성된 테스트 자동화 저장소입니다.


# 테스트 목적 및 범위
- 프로그램 실행
- 회원가입
- 로그인
  - 정상계정 로그인
  - 미가입 계정 로그인
  - 잠금 계정 로그인
  - 미승인 계정 로그인
  - 비밀번호 초기화 계정 로그인
- 홈
  - 프로필 정보
  - 프로필 사진 UI 비교
  - 계정 알림/자동응답 등 설정 확인
- 메시지
  - 메시지 대화 동작 확인
- 조직도
  - 직원 리스트 확인

# 사용 기술 및 도구
```
언어: Python
사용 라이브러리: Appium,  Pywinauto, pyautogui, functools, PIL
구조 분석 툴: InspectX

Inspect 다운로드(필수아님)
https://github.com/yinkaisheng/Python-UIAutomation-for-Windows/tree/master/inspect
> 해당 프로그램 관리자 권한으로 실행(Motion 진입 불가)

```

# 테스트 실행 방법
- 기기에 Motion M apk 파일을 가지고있어야 합니다.
1. android studio Emulator 실행
2. main.py 파일 실행

