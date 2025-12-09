from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


@app.get("/update")
def get_update():
    """
    Endpoint de update compatível com o Tauri.
    Retorna a nova versão disponível exclusivamente para Windows.
    """

    return {
        # AQUI SEMPRE COLOQUE UMA VERSÃO MAIOR QUE A INSTALADA
        "version": "1.0.1",

        "notes": "Correções de bugs e melhorias de estabilidade.",

        # DATA É OBRIGATÓRIA PARA O TAURI
        "pub_date": datetime.utcnow().isoformat() + "Z",

        # FORMATO CORRETO EXIGIDO PELO TAURI
        "platforms": {
            "windows-x86_64": {
                "url": "https://sgp.finderbit.com.br/update/releases/windows/SGP_1.0.1_x64.msi",

                # ASSINATURA BASE64 GERADA PELO `tauri signer sign`
                "signature": (
                    "dW50cnVzdGVkIGNvbW1lbnQ6IHJzaWduIGVuY3J5cHRlZCBzZWNyZXQga2V5ClJXUlRZ"
                    "MEl5aWp4RmpXSUZGbVR6aG9mV3dhT201RE45cFAySjdWVnBLL0NpOEZvSEVIa0FBQkFB"
                    "QUFBQUFBQUFBQUlBQUFBQXF3QUJSSUJjVXVUcGRCU1MweGYxWHpaM1BvcFU2WHBJcm9P"
                    "WThTUTlwUkdZZ2pGZU93WlJwbEdxcmFEYk9PbFNLTGRDWHJQdk9UV0pFdjVoYVNXcjJK"
                    "MWtPaDk5Snk3NWFqLzE1dVc5ZnV6dHI1YVRzSFNyQmpjc3hJN3E2UWxHbDhlUnh0U3A5"
                    "S1E9Cg=="
                )
            }
        }
    }
