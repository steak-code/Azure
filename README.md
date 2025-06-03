# Blob
1. azure portal 建立資源群組
2. 搜尋blob -> 儲存體帳戶
3. 建立 儲存體帳戶(選擇資源群組) -> 命名儲存體帳戶 -> 建立
4. 儲存體帳戶的存取金鑰 -> 安全+網路 -> 複製機碼和連接字串
5. 儲存體帳戶 -> 資料儲存 -> 建立容器(取名)

測試環境設定
[建議] 先建立虛擬環境

在虛擬環境中安裝需要的套件
pip install -r requirements.txt

.env檔案需要:
AZURE_STORAGE_CONNECTION_STRING(連接字串)
AZURE_CONTAINER_NAME(容器名稱)
AZURE_STORAGE_ACCOUNT_NAME(儲存體帳戶名稱)
AZURE_STORAGE_ACCOUNT_KEY (複製機碼)


# Form Recongizer 
1. 搜尋 Document intelligence -> 選擇剛剛建立的資源群組 -> 選擇免費帳戶建立
2. 點擊資源管理 -> 金鑰與端點 -> 存取金鑰、位置與端點
3. 
4. 
5. 
