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

# Form Recongizer 
1. 搜尋 Document intelligence -> 選擇剛剛建立的資源群組 -> 選擇免費帳戶建立
2. 點擊資源管理 -> 金鑰與端點 -> 存取金鑰、位置與端點
3. 
4. 
5. 
