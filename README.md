# 📔 오늘의 자아 로그 (Today's Self Journal)

> **당신의 하루를 기록하면, AI가 감정을 읽어줍니다**
>
> 파스텔 톤의 따뜻한 감정 저널 앱으로 자신의 마음을 들여다보세요.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.12%2B-brightgreen)
![Chainlit](https://img.shields.io/badge/Chainlit-0.7.0%2B-purple)

---

## 🎯 프로젝트 소개

**'오늘의 자아 로그'**는 사용자의 일상을 한 줄로 기록하면, AI가 감정을 분석하고 성찰 질문을 던져주는 **감정 저널 앱**입니다.

단순한 기록을 넘어, **3단계 깊이의 성찰 질문**을 통해 자신의 마음을 더 깊이 있게 이해할 수 있습니다.

### ✨ 핵심 특징

- 🎭 **6가지 감정 인식**: 지침, 회피, 성취, 기대, 불안, 고요
- 💬 **3단계 성찰 질문**: 표면 → 의미 → 존재로 심화되는 질문
- 🎨 **3가지 톤 선택**: 파스텔(부드러움) / 시적(은유) / 철학적(깊음)
- 📊 **감정 트렌드 추적**: 주간 감정 흐름 & 패턴 분석
- 💾 **로컬 저장**: 프라이버시 보호 (클라우드 불필요)
- 🤖 **AI 기반 분석**: Groq Llama 모델 지원

---

## 🚀 빠른 시작

### 설치

```bash
# 저장소 복제
git clone https://github.com/Lunorsun/mcp-realtime-chainlit.git
cd mcp-realtime-chainlit

# 가상 환경 생성
python3 -m venv .venv
source .venv/bin/activate

# 의존성 설치
pip install -r requirements.txt
```

### 환경 설정

`.env` 파일 생성 후 Groq API 키 설정:

```bash
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-2-13b-chat
```

Groq API 키는 [Groq 콘솔](https://console.groq.com)에서 발급받으세요.

### 실행

```bash
chainlit run journal_ui.py
```

브라우저에서 `http://localhost:8000` 접속

---

## 📖 사용 가이드

### 1️⃣ 시작하기

앱 실행 후 **톤 선택** 버튼이 표시됩니다:

- **따뜻하고 부드러운 (기본)**: 위로가 담긴 질문
- **시적이고 은유적인**: 시적 표현의 질문
- **깊고 철학적인**: 존재적 의미 탐구 질문

### 2️⃣ 감정 기록

한 줄로 감정을 적어주세요:

```
예시:
"오늘 프로젝트가 완료돼서 너무 뿌듯해"
"회사에서 시험 때문에 너무 긴장했어"
"혼자 있는 시간이 편했어"
```

### 3️⃣ 분석 결과 확인

입력 후 **4개 카드** 표시:

| 카드 | 내용 |
|------|------|
| 📌 감정 시그니처 | 감정 유형, 강도, 방향 |
| 📌 사건 흐름 | 하루의 주요 사건들 |
| 📌 성찰 질문 | 3단계 깊이 있는 질문 |
| 📌 에필로그 + 권장사항 | 감정별 조언 |

### 4️⃣ 명령어 사용

| 명령어 | 기능 |
|--------|------|
| `/help` 또는 `/도움` | 전체 안내 보기 |
| `/주간` | 주간 감정 요약 |
| `/흐름` | 최근 감정 흐름 |
| `/통찰` | 주간 통찰 메시지 |
| `/톤변경` | 톤 다시 선택 |

---

## 📁 프로젝트 구조

```
mcp-realtime-chainlit/
├── journal_ui.py              # 메인 Chainlit UI
├── analyzer.py                # 감정 분석 엔진
├── event_mapper.py            # 사건 구조화
├── questions.py               # 성찰 질문 생성
├── patterns.py                # 기록 저장 & 패턴 분석
├── emotion_trends.py          # 감정 트렌드 분석
├── tone_config.py             # 톤 설정 & 시각화
├── recommendations.py         # 맞춤 권장사항
├── groq_client.py             # Groq API 클라이언트
├── .env                       # 환경 변수
├── requirements.txt           # 의존성
├── README.md                  # 이 파일
├── README_KO.md               # 한글 상세 가이드
├── README-en.md               # 영문 가이드
└── data/
    ├── patterns.json          # 사용자 기록
    └── emotion_trends.json    # 감정 트렌드
```

---

## 🔍 감정 분류

| 감정 | 이모지 | 설명 |
|------|--------|------|
| 성취 | ◆ | 목표 달성의 기쁨 |
| 기대 | ▲ | 미래에 대한 긍정 |
| 불안 | ▼ | 불확실함에 대한 두려움 |
| 고요 | ★ | 마음의 안정감 |
| 회피 | ● | 어려움으로부터의 회피 |
| 지침 | ○ | 방향을 잃은 상태 |

---

## 🛠️ 기술 스택

- **프레임워크**: Chainlit
- **언어**: Python 3.12+
- **AI 모델**: Groq Llama-2-13b-chat
- **저장소**: 로컬 JSON

---

## 📚 문서

- [한글 상세 가이드](README_KO.md)
- [English Guide](README-en.md)

---

## 🔐 개인정보 보호

✅ 모든 데이터는 로컬에만 저장됩니다 (클라우드 전송 없음)

---

## 📄 라이센스

MIT License

---

**오늘의 자아 로그와 함께 당신의 마음을 들여다보세요 🌙**


## 설치

1. 저장소를 클론합니다:
   ```bash
   git clone <repository-url>
   cd mcp-realtime-chainlit
   ```

2. uv를 사용하여 Python 의존성을 설치합니다 (현대적인 Python 패키지 매니저):
   ```bash
   uv sync
   ```
   
   참고: uv가 설치되어 있지 않다면, 먼저 설치하세요:
   ```bash
   curl -sSf https://install.ultraviolet.rs | sh
   ```

3. Azure OpenAI 자격 증명으로 `.env` 파일을 생성합니다:
   ```
   AZURE_OPENAI_API_KEY=your_api_key
   AZURE_OPENAI_ENDPOINT=your_endpoint
   AZURE_OPENAI_DEPLOYMENT=your_deployment_name
   ```

### Groq (Llama) 사용

Groq의 Llama 모델을 사용하려면 `.env`에 Groq 관련 환경 변수를 추가하세요:

```
GROQ_API_KEY=your_groq_api_key_here
GROQ_PROJECT_ID=your_groq_project_id_here
GROQ_REGION=your_groq_region_here
GROQ_MODEL=llama-2-13b-chat
```

1. `requirements.txt`를 통해 의존성을 설치합니다:
```bash
pip install -r requirements.txt
```

2. `groq_client.py`는 Groq API로 텍스트 생성 요청을 보내는 간단한 래퍼입니다. 환경 변수를 설정하면 애플리케이션에서 이를 사용하도록 통합할 수 있습니다.

참고: Groq의 API 스펙(요청/응답 형식)은 모델과 API 버전에 따라 달라질 수 있으므로, 실제 배포 전 Groq 문서를 확인하고 `groq_client.py`의 페이로드를 조정하세요.

## 사용법

### 옵션 1: Groq Llama 채팅 모드

```bash
chainlit run chat.py
```

Groq API를 사용한 간단한 텍스트 생성 모드입니다.

### 옵션 2: 오늘의 자아 로그 (파스텔 감정 성찰 저널)

```bash
chainlit run journal_ui.py
```

부드럽고 문학적인 파스텔 톤의 감정 분석 및 성찰 질문 생성 모드입니다:
- **감정 시그니처**: 한 줄 입력에서 감정 카테고리, 강도(1-5), 방향(내부/외부) 자동 분석
- **사건 지도**: 하루의 사건들을 구조화하고 감정 흐름 추적
- **3단계 질문**: 표면 → 의미 → 존재 수준의 성찰 질문 자동 생성
- **패턴 추적**: 저장된 항목에서 반복되는 감정·선택 패턴 감지
- **에필로그**: 부드러운 마무리 문장으로 하루를 감싸주기

웹 인터페이스는 일반적으로 http://localhost:8000에서 접속할 수 있습니다.

### 챗봇과 상호작용하기

- **텍스트 모드**: 에어비앤비 목록, 가격, 위치 등에 대한 질문을 입력하세요.
- **음성 모드**: 마이크 버튼을 클릭하여 말하기를 시작하면, 시스템이 음성 입력을 처리합니다.

## 프로젝트 구조

- `mcp_service.py`: MCP 서버와 통신하기 위한 MCP 서비스 클라이언트 구현
- `realtime.py`: OpenAI 실시간 API에 대한 WebSocket 연결 관리
- `chat.py`: 텍스트와 오디오를 위한 핸들러가 포함된 Chainlit 인터페이스 구현
- `chainlit_config.py`: 다국어 지원을 위한 설정
- `locales/`: 다양한 언어의 번역 파일

## 작동 원리

1. Chainlit 애플리케이션이 시작되고 Azure OpenAI의 실시간 API에 연결을 설정합니다
2. MCP 서비스가 초기화되고 에어비앤비 MCP 서버에 연결됩니다
3. 사용자가 메시지(텍스트 또는 오디오)를 보낼 때:
   - 텍스트인 경우: 메시지가 모델에 직접 전송됩니다
   - 오디오인 경우: 오디오가 실시간 전사를 위해 모델로 스트리밍됩니다
4. 모델은 MCP 도구를 통해 에어비앤비 데이터에 액세스하여 입력을 처리합니다
5. 응답이 사용자에게 스트리밍됩니다 (텍스트 및/또는 오디오)

## 개발

### 새로운 MCP 도구 추가하기

새로운 MCP 서버를 추가하려면:

1. `MCPService.initialize()` 메서드에 서버 설정을 추가합니다
2. MCP 서버에 필요한 npm 패키지를 설치합니다

## 라이선스

MIT 라이선스 (MIT)

## 감사의 말

- 이 프로젝트는 채팅 인터페이스를 위해 [Chainlit](https://github.com/Chainlit/chainlit) 프레임워크를 사용합니다
- 실시간 스트리밍 구현은 [openai-realtime-console](https://github.com/openai/openai-realtime-console)에서 파생되었습니다
- 에어비앤비 데이터는 [@openbnb/mcp-server-airbnb](https://www.npmjs.com/package/@openbnb/mcp-server-airbnb)를 통해 제공됩니다
