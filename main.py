from fastapi import FastAPI

app = FastAPI()

@app.get("/update")
def get_update():
    """
    Endpoint de atualização compatível com o Tauri Updater.
    Editar versão, URL e assinatura conforme necessário.
    """

    return {
        "version": "1.0.1",  # AQUI: versão nova
        "notes": "Atualização automática funcionando.",
        "pub_date": "2025-01-01T00:00:00Z",

        "platforms": {
            "windows-x86_64": {
                "url": "https://sgp.finderbit.com.br/update/releases/windows/SGP_1.0.1_x64.msi",
                "signature": "dW50cnVzdGVkIGNvbW1lbnQ6IHJzaWduIGVuY3J5cHRlZCBzZWNyZXQga2V5ClJXUlRZMEl5aWp4RmpXSUZGbVR6aG9mV3dhT201RE45cFAySjdWVnBLL0NpOEZvSEVIa0FBQkFBQUFBQUFBQUFBQUlBQUFBQXF3QUJSSUJjVXVUcGRCU1MweGYxWHpaM1BvcFU2WHBJcm9PWThTUTlwUkdZZ2pGZU93WlJwbEdxcmFEYk9PbFNLTGRDWHJQdk9UV0pFdjVoYVNXcjJKMWtPaDk5Snk3NWFqLzE1dVc5ZnV6dHI1YVRzSFNyQmpjc3hJN3E2UWxHbDhlUnh0U3A5S1E9Cg=="
            }
        }
    }
