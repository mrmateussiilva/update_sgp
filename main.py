from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Montar o diretório de releases para servir arquivos estáticos
app.mount("/releases", StaticFiles(directory="releases"), name="releases")

@app.get("/update")
def get_update():
    """
    Endpoint de atualização compatível com o Tauri Updater.
    Editar versão, URL e assinatura conforme necessário.
    """
    # URL base da API - os arquivos serão servidos através do mount /releases
    base_url = "https://sgp.finderbit.com.br"  # Ajuste conforme necessário
    
    return {
        "version": "1.0.1",  # AQUI: versão nova
        "notes": "Atualização automática funcionando.",
        "pub_date": "2025-01-01T00:00:00Z",

        "platforms": {
            "windows-x86_64": {
                "url": f"{base_url}/releases/windows/SGP_1.0.1_x64.msi",
                "signature": "dW50cnVzdGVkIGNvbW1lbnQ6IHJzaWduIGVuY3J5cHRlZCBzZWNyZXQga2V5ClJXUlRZMEl5aWp4RmpXSUZGbVR6aG9mV3dhT201RE45cFAySjdWVnBLL0NpOEZvSEVIa0FBQkFBQUFBQUFBQUFBQUlBQUFBQXF3QUJSSUJjVXVUcGRCU1MweGYxWHpaM1BvcFU2WHBJcm9PWThTUTlwUkdZZ2pGZU93WlJwbEdxcmFEYk9PbFNLTGRDWHJQdk9UV0pFdjVoYVNXcjJKMWtPaDk5Snk3NWFqLzE1dVc5ZnV6dHI1YVRzSFNyQmpjc3hJN3E2UWxHbDhlUnh0U3A5S1E9Cg=="
            }
        }
    }

@app.get("/download/{platform}/{filename}")
async def download_file(platform: str, filename: str):
    """
    Endpoint direto para download de arquivos de atualização.
    Exemplo: /download/windows/SGP_1.0.1_x64.msi
    """
    file_path = f"releases/{platform}/{filename}"
    if os.path.exists(file_path):
        return FileResponse(
            file_path,
            filename=filename,
            media_type='application/octet-stream'
        )
    raise HTTPException(status_code=404, detail="Arquivo não encontrado")
