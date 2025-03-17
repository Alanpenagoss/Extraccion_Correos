import requests
import re
from bs4 import BeautifulSoup

url = "http://127.0.0.1:8000/victima.html"

try:
    resp = requests.get(url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    
    enlaces = [a["href"] for a in soup.find_all("a", href=True)]
    comentarios = [c for c in soup.find_all(string=lambda t: isinstance(t, type(soup).Comment))]
    correos = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", resp.text)
    
    print("Enlaces:", enlaces)
    print("Comentarios:", comentarios)
    print("Correos:", correos)

except requests.exceptions.RequestException as e:
    print("Error de conexión:", e)

