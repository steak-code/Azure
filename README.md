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
