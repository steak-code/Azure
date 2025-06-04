# 📦 Azure Blob + 📄 Azure Form Recognizer 環境建置指南

## 📁 一、Azure Blob 儲存體設定
### 1. 建立資源群組
1. 登入 [Azure Portal](https://portal.azure.com/)
2. 搜尋並建立「資源群組」

### 2. 建立儲存體帳戶
1. 搜尋 `Blob` 或 `儲存體帳戶`
2. 建立儲存體帳戶：
   - 選擇已建立的資源群組
   - 命名儲存體帳戶（須唯一、全小寫）
   - 點選「建立」

### 3. 取得連線資訊
1. 前往儲存體帳戶 → 「安全性 + 網路」→「存取金鑰」
2. 複製以下資訊：
   - `連接字串`
   - `金鑰1`

### 4. 建立容器
1. 儲存體帳戶 → 「資料儲存」→「容器」
2. 點選「+ 容器」建立新的 Blob 容器
3. 命名容器（建議使用小寫英數）

---

## ⚙️ 二、測試環境設定
### 建立虛擬環境（建議）
```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

### Form Recognizer 
1. 搜尋 Document intelligence -> 選擇剛剛建立的資源群組 -> 選擇免費帳戶建立
2. 點擊資源管理 -> 金鑰與端點 -> 存取金鑰、位置與端點

---

### 安裝依賴套件
```bash
pip install -r requirements.txt
```

---

### 建立 .env 環境變數檔案
```bash
AZURE_STORAGE_CONNECTION_STRING=你的連接字串
AZURE_CONTAINER_NAME=容器名稱
AZURE_STORAGE_ACCOUNT_NAME=儲存體帳戶名稱
AZURE_STORAGE_ACCOUNT_KEY=複製的金鑰
```

---

## 🧠 三、Azure Form Recognizer（Document Intelligence）設定
### 1. 建立資源
1. 搜尋 Document Intelligence
2. 建立資源（可選擇免費帳戶），並選擇剛剛的資源群組

### 2. 取得金鑰與端點
1. 進入資源 → 「資源管理」→「金鑰與端點」
2. 複製以下資訊：
   - `金鑰`
   - `端點`
   - `位置`

---

## 🐳 四、Docker 容器化設定

### Dockerfile
```dockerfile
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
```

### requirements.txt
```txt
flask
python-dotenv
azure-storage-blob
azure-ai-formrecognizer
```

### example.py 設定
確保 `example.py` 最後一行為：
```python
app.run(host="0.0.0.0", port=8080, debug=True)
```

---

## 🚀 五、本地開發環境啟動

### 步驟 1：進入專案目錄
```bash
cd C:\Users\user\Downloads\finalfinal\finalfinal
```

### 步驟 2：建立虛擬環境
```bash
python -m venv venv
```

### 步驟 3：啟動虛擬環境
```bash
# Windows
. venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 步驟 4：安裝依賴套件
```bash
pip install -r requirements.txt
```

---

## 🐳 六、Docker 容器化部署

### 步驟 1：確保 Docker 已啟動
請先打開 Docker Desktop 或確保 Docker 服務已運行

### 步驟 2：建立 Docker 映像檔
```bash
docker image build -t azure_final:latest .
```

### 步驟 3：運行 Docker 容器
```bash
docker container run -d --name azure_final -p 8080:8080 azure_final:latest
```

### 步驟 4：本地測試運行
```bash
python example.py
```

---

## ✅ 驗證部署
- **本地訪問**：http://localhost:8080
- **Docker 容器訪問**：http://localhost:8080
- **檢查容器狀態**：`docker ps`
- **查看容器日誌**：`docker logs azure_final`

---

## 🚨 注意事項

### 環境變數設定
- 確保 `.env` 檔案包含所有必要的 Azure 設定
- Docker 容器中需要正確讀取環境變數

### 端口設定
- 本地開發：使用 `localhost:8080`
- Docker 容器：映射到 `8080:8080`
- 確認防火牆未阻擋該端口

### 檔案權限
- Windows 環境下注意路徑格式
- 確保 Docker 有權限訪問專案資料夾
