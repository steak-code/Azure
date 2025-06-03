📦 Azure Blob + 📄 Form Recognizer 環境建置與設定指南
📁 一、Azure Blob 儲存體設定
1. 建立資源群組
登入 Azure Portal

搜尋並建立「資源群組」

2. 建立儲存體帳戶
搜尋 Blob 或 儲存體帳戶

建立儲存體帳戶：

選擇剛剛建立的資源群組

命名儲存體帳戶（符合命名規則）

點選「建立」

3. 取得連線資訊
開啟儲存體帳戶 → 點選「安全性 + 網路」→「存取金鑰」

複製：

連接字串

金鑰1

4. 建立 Blob 容器
儲存體帳戶 → 資料儲存 → 容器

建立容器（取一個名稱，建議使用全小寫英數）

⚙️ 二、測試環境設定
建議使用虛擬環境
bash
複製
編輯
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
安裝依賴套件
bash
複製
編輯
pip install -r requirements.txt
建立 .env 環境變數檔案
新增 .env 檔並填入以下內容（根據你建立的資源）：

ini
複製
編輯
AZURE_STORAGE_CONNECTION_STRING=你的連接字串
AZURE_CONTAINER_NAME=容器名稱
AZURE_STORAGE_ACCOUNT_NAME=儲存體帳戶名稱
AZURE_STORAGE_ACCOUNT_KEY=複製的金鑰
🧠 三、Azure Form Recognizer（Document Intelligence）設定
1. 建立 Form Recognizer 資源
搜尋 Document Intelligence

建立資源：

選擇剛剛建立的資源群組

選擇「免費帳戶」

2. 取得金鑰與端點
前往建立好的資源 → 左側選單點選「金鑰與端點」

複製以下資訊：

金鑰

端點

位置

3. 加入 .env（如果需與程式整合）
ini
複製
編輯
AZURE_FORM_RECOGNIZER_KEY=你的 Form Recognizer 金鑰
AZURE_FORM_RECOGNIZER_ENDPOINT=你的端點 URL
AZURE_FORM_RECOGNIZER_REGION=你的資源所在區域（例如 eastus）
📂 專案目錄結構（範例）
bash
複製
編輯
.
├── .env
├── main.py
├── requirements.txt
├── README.md
└── ...

# Form Recongizer 
1. 搜尋 Document intelligence -> 選擇剛剛建立的資源群組 -> 選擇免費帳戶建立
2. 點擊資源管理 -> 金鑰與端點 -> 存取金鑰、位置與端點
3. 
4. 
5. 
