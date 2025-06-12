from flask import Flask, render_template, request, redirect
from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv
from datetime import datetime, timedelta
import os, uuid

# Load .env
load_dotenv()

app = Flask(__name__)

# Azure Blob
blob_conn_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
account_name = os.getenv("AZURE_STORAGE_ACCOUNT_NAME")
account_key = os.getenv("AZURE_STORAGE_ACCOUNT_KEY")
container_name = os.getenv("AZURE_CONTAINER_NAME")
blob_service_client = BlobServiceClient.from_connection_string(blob_conn_str)

# Azure Form Recognizer
form_endpoint = os.getenv("AZURE_FORM_ENDPOINT")
form_key = os.getenv("AZURE_FORM_KEY")
form_client = DocumentAnalysisClient(endpoint=form_endpoint, credential=AzureKeyCredential(form_key))

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = f"upload-{uuid.uuid4()}.pdf"
            blob_client = blob_service_client.get_blob_client(container=container_name, blob=filename)
            blob_client.upload_blob(file)

            # 使用 SAS token 生成可下載的 blob URL
            sas_token = generate_blob_sas(
                account_name=account_name,
                container_name=container_name,
                blob_name=filename,
                account_key=account_key,
                permission=BlobSasPermissions(read=True),
                expiry=datetime.utcnow() + timedelta(minutes=10)
            )
            blob_url = f"https://{account_name}.blob.core.windows.net/{container_name}/{filename}?{sas_token}"

            # 呼叫 Form Recognizer
            poller = form_client.begin_analyze_document_from_url("prebuilt-document", blob_url)
            result = poller.result()

            extracted = []
            for page in result.pages:
                for line in page.lines:
                    extracted.append(line.content)

            return render_template('index.html', extracted=extracted, blob_url=blob_url)

    return render_template('index.html', extracted=None)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
