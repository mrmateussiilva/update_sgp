from fastapi import FastAPI

app = FastAPI()


@app.get("/update")
def get_update():
    """
    Retorna informações de atualização fixas.
    """
    return {
        # ALTERE A VERSÃO AQUI
        "version": "1.0.0",
        
        # ALTERE AS NOTAS AQUI
        "notes": "Primeira versão de update.",
        
        "windows": {
            # ALTERE A URL DO ARQUIVO AQUI
            "url": "https://sgp.finderbit.com.br/update/releases/windows/SGP_1.0.1_x64.msi",
            # ALTERE A ASSINATURA BASE64 AQUI
            "signature": "dW50cnVzdGVkIGNvbW1lbnQ6IHJzaWduIGVuY3J5cHRlZCBzZWNyZXQga2V5ClJXUlRZMEl5aWp4RmpXSUZGbVR6aG9mV3dhT201RE45cFAySjdWVnBLL0NpOEZvSEVIa0FBQkFBQUFBQUFBQUFBQUlBQUFBQXF3QUJSSUJjVXVUcGRCU1MweGYxWHpaM1BvcFU2WHBJcm9PWThTUTlwUkdZZ2pGZU93WlJwbEdxcmFEYk9PbFNLTGRDWHJQdk9UV0pFdjVoYVNXcjJKMWtPaDk5Snk3NWFqLzE1dVc5ZnV6dHI1YVRzSFNyQmpjc3hJN3E2UWxHbDhlUnh0U3A5S1E9Cg=="

        }
    }
