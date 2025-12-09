# Update API

API simples para atualizações de aplicações Tauri.

## Instalação

```bash
uv run pip install -r requirements.txt
```

## Execução

```bash
uv run uvicorn main:app --host 0.0.0.0 --port 8000
```

## Endpoints

### GET /latest/{platform}

Retorna a última versão disponível para a plataforma especificada (windows, linux ou macos).

**Resposta:**
```json
{
  "version": "1.0.0",
  "notes": "Initial release",
  "pub_date": "2025-01-01T00:00:00Z",
  "url": "https://meuservidor.com/releases/windows/app-1.0.0.msi",
  "signature": "string-base64"
}
```

### POST /upload

Faz upload de um arquivo de release.

**Headers:**
- `X-API-Key`: CHAVE_AQUI (definida em main.py)

**Form Data:**
- `file`: Arquivo binário
- `version`: Versão (ex: "1.0.3")
- `notes`: Notas da versão
- `platform`: windows|linux|macos
- `signature`: Assinatura base64

### GET /releases/{platform}/{filename}

Baixa um arquivo de release específico.

## Configuração

Edite `API_KEY` no arquivo `main.py` para definir sua chave de API.

Ajuste `base_url` na função `upload_file` para o URL do seu servidor.

