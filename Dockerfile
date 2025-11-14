FROM python:3.12-slim

WORKDIR /app

# 시스템 패키지 설치
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Python 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 앱 코드 복사
COPY . .

# 데이터 디렉토리 생성
RUN mkdir -p data

# Chainlit 실행 (Hugging Face Spaces 포트: 7860)
CMD ["chainlit", "run", "journal_ui.py", "--host", "0.0.0.0", "--port", "7860"]
