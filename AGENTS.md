# 마인갤러리 프로젝트 작업 규칙

작업 시작 전 README.md와 docs/STATUS.md를 읽는다.

- 사용자 요청에 맞춰 개별 체험 예약을 우선한다. 일정 추천과 패키지는 별도 요청 시 진행한다.
- 실제 PG 결제·지급·인증이 연결되기 전에는 예시 동작임을 명확히 표시한다.
- 웹 원본은 consumer-web/dist/, 배포본은 releases/, 도구는 scripts/, 문서는 docs/에 둔다.
- 비밀번호·토큰·API 키·PG 인증정보·예약자 개인정보는 커밋하지 않는다.
- 작업 완료 시 docs/STATUS.md에 날짜, 변경 내용, 확인 결과, 남은 작업을 기록한다.
- 관련 코드와 문서를 같은 커밋에 포함하고 이해하기 쉬운 제목을 사용한다.
- 커밋과 원격 업로드는 사용자가 승인한 작업 범위 안에서 수행하고 업로드 결과를 확인한다.
- 다른 작업의 변경을 덮어쓰거나 강제 푸시하지 않는다.
- 오프라인 버전을 변경하면 python scripts/build-offline.py로 배포본을 갱신한다.
- 적절한 경우 node scripts/check-consumer.cjs 및 node scripts/check-consumer.cjs --offline으로 확인한다.
