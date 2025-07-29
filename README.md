# Zotero BibTeX API for GPT Integration

Este proyecto implementa una API Flask que permite consultar tu biblioteca personal de Zotero y generar citas en formato BibTeX, diseñada para integrarse con asistentes GPT personalizados en OpenAI.

---

## 🚀 ¿Qué hace esta API?

- Consulta referencias por título, autor o año (`/zotero/search?q=...`).
- Devuelve citas completas en formato BibTeX (`/zotero/bib?q=...`).
- Se conecta exclusivamente con tu biblioteca Zotero usando tu User ID y clave API.

---

## 🛠 Requisitos

- Python 3.8+
- Cuenta en [Zotero](https://zotero.org)
- Clave API de solo lectura desde [https://www.zotero.org/settings/keys](https://www.zotero.org/settings/keys)

---

## 🔐 Seguridad

**⚠️ No subas tu clave API directamente al repositorio.**

En lugar de eso:

1. Crea un archivo `.env` con tu clave:
   ```bash
   ZOTERO_API_KEY=tu_clave_zotero
   ```

2. Usa `python-dotenv` para cargarla automáticamente:
   ```python
   from dotenv import load_dotenv
   import os
   load_dotenv()
   ZOTERO_API_KEY = os.getenv("ZOTERO_API_KEY")
   ```

3. Añade `.env` a tu `.gitignore`:

   ```
   .env
   ```

---

## 🧪 Uso

Una vez desplegado (local o en Render):

- Buscar JSON:
  ```
  GET /zotero/search?q=Cardona
  ```

- Obtener BibTeX:
  ```
  GET /zotero/bib?q=Cardona
  ```

---

## 🧠 Integración con GPT personalizado

Puedes registrar esta API como función externa (`Actions`) en tu GPT con:

```json
{
  "name": "consultarZoteroBib",
  "description": "Devuelve una cita BibTeX desde tu biblioteca Zotero.",
  "parameters": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "Autor, año o título parcial"
      }
    },
    "required": ["query"]
  },
  "url": "https://TU-DOMINIO/zotero/bib",
  "method": "GET",
  "query_parameters": ["query"]
}
```

---

## 🧾 Licencia

MIT. Puedes reutilizarlo, adaptarlo y compartirlo citando este repositorio.

