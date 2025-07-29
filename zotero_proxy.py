from flask import Flask, request, jsonify, Response
import requests

app = Flask(__name__)

ZOTERO_API_KEY = "2CVtgmulkLg4SDYMQkb1izUU"
ZOTERO_USER_ID = "3598779"
ZOTERO_BASE_URL = f"https://api.zotero.org/users/{ZOTERO_USER_ID}/items"

@app.route("/zotero/search")
def search_item():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "Falta el parámetro 'q'"}), 400

    headers = {"Zotero-API-Key": ZOTERO_API_KEY}
    params = {"q": query, "format": "json", "limit": 5}
    response = requests.get(ZOTERO_BASE_URL, headers=headers, params=params)

    if response.status_code == 200:
        return jsonify(response.json())
    return jsonify({"error": "Error en la consulta"}), response.status_code

@app.route("/zotero/bib")
def bibtex_output():
    query = request.args.get("q")
    if not query:
        return Response("Falta el parámetro 'q'", status=400)

    headers = {"Zotero-API-Key": ZOTERO_API_KEY}
    params = {"q": query, "format": "json", "limit": 1}
    response = requests.get(ZOTERO_BASE_URL, headers=headers, params=params)

    if response.status_code != 200:
        return Response("Error al consultar Zotero", status=response.status_code)

    items = response.json()
    if not items:
        return Response("No se encontraron resultados", status=404)

    item = items[0]["data"]
    entry_type = item.get("itemType", "article")
    key = f"{item.get('lastName','')}{item.get('date','')}".replace(" ", "")
    authors = item.get("creators", [])
    author_str = " and ".join(f"{a['lastName']}, {a['firstName']}" for a in authors if "lastName" in a)

    bib = f"@{entry_type}{{{key},\n"
    bib += f"  author = {{{author_str}}},\n"
    bib += f"  title = {{{item.get('title', '')}}},\n"
    if item.get("date"): bib += f"  year = {{{item['date'][:4]}}},\n"
    if item.get("DOI"): bib += f"  doi = {{{item['DOI']}}},\n"
    if item.get("publicationTitle"): bib += f"  journal = {{{item['publicationTitle']}}},\n"
    if item.get("url"): bib += f"  url = {{{item['url']}}},\n"
    bib += "}\n"

    return Response(bib, mimetype='text/plain')

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

