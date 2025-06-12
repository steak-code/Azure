FROM --platform=linux/amd64 python:3.14-rc-slim

# 安裝系統依賴（build-essential、libffi-dev 等）
RUN apt update && apt install -y --no-install-recommends \
    build-essential \
    libffi-dev \
    gcc \
    libssl-dev \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

# 建立工作目錄
WORKDIR /app

# 複製檔案
COPY requirements.txt /app/
COPY example.py /app/
COPY templates /app/templates
COPY .env /app/

# 安裝 Python 套件
RUN pip install --no-cache-dir -r requirements.txt

# 容器開放的埠
EXPOSE 8080

# 啟動入口
ENTRYPOINT ["python", "example.py"]
