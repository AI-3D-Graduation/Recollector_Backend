# Recollector_Backend


2D 이미지를 3D 모델로 변환하는 서비스의 FastAPI 백엔드입니다. 외부 AI 서비스를 비동기적으로 호출하고, 생성 과정을 관리하며, 결과물을 제공하는 API를 갖추고 있습니다.


## 📁 파일 구조

```
/
├── app/
│   ├── api/
│   │   └── endpoints/
│   │       └── generation.py   # API 엔드포인트
│   ├── core/
│   │   └── config.py         # 설정 관리
│   ├── services/
│   │   └── ai_pipeline.py    # 핵심 비즈니스 로직
│   ├── schemas/
│   │   └── generation.py     # 데이터 유효성 검사 모델
│   └── main.py             # FastAPI 앱 시작점
│
├── static/
│   └── models/               # 최종 3D 모델 파일 저장 (.glb)
│
├── .env                      # 환경 변수 설정
└── requirements.txt          # 의존성 패키지 목록
```

-----

## 📖 API 엔드포인트

| HTTP Method | Endpoint                | 설명                                                     |
| :---------- | :---------------------- | :------------------------------------------------------- |
| `POST`      | `/api/generate`         | 이미지로 3D 모델 생성을 시작하고 작업 ID를 받습니다.       |
| `GET`       | `/api/status/{task_id}` | 작업 ID로 생성 상태와 진행률을 조회합니다.               |
| `DELETE`    | `/api/tasks/{task_id}`  | 특정 작업과 관련된 모든 파일 및 데이터를 삭제합니다.     |