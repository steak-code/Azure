from flask import Flask, render_template, request, redirect
from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Azure 設定
connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
container_name = os.getenv("AZURE_CONTAINER_NAME")
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

form_endpoint = os.getenv("AZURE_FORM_ENDPOINT")
form_key = os.getenv("AZURE_FORM_KEY")
form_client = DocumentAnalysisClient(endpoint=form_endpoint, credential=AzureKeyCredential(form_key))

# 上傳並擷取文字
@app.route("/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files["file"]
        blob_name = f"upload-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}.pdf"

        # 上傳 PDF
        pdf_blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        pdf_blob_client.upload_blob(file, overwrite=True)

        # OCR 分析（重新定位檔案流）
        file.stream.seek(0)
        poller = form_client.begin_analyze_document("prebuilt-document", document=file)
        result = poller.result()

        extracted_text = ""
        for page in result.pages:
            for line in page.lines:
                extracted_text += line.content + "\n"

        # 上傳 .txt
        txt_blob_name = blob_name.replace(".pdf", ".txt")
        txt_blob_client = blob_service_client.get_blob_client(container=container_name, blob=txt_blob_name)
        txt_blob_client.upload_blob(extracted_text.encode("utf-8"), overwrite=True)

        # ➜ 顯示上傳後辨識結果頁
        return render_template("upload_result.html", pdf_name=blob_name, txt_name=txt_blob_name, extracted_text=extracted_text)

    return render_template("upload.html")

# 列出 blob
@app.route("/blobs")
def show_blobs():
    container_client = blob_service_client.get_container_client(container_name)
    blobs = []
    for blob in container_client.list_blobs():
        sas_token = generate_blob_sas(
            account_name=blob_service_client.account_name,
            container_name=container_name,
            blob_name=blob.name,
            account_key=blob_service_client.credential.account_key,
            permission=BlobSasPermissions(read=True),
            expiry=datetime.utcnow() + timedelta(minutes=15)
        )
        blob_url = f"https://{blob_service_client.account_name}.blob.core.windows.net/{container_name}/{blob.name}?{sas_token}"
        blobs.append((blob.name, blob.size, blob.last_modified, blob_url))

    return render_template("blobs.html", blobs=blobs)

if __name__ == "__main__":
    app.run(debug=True)