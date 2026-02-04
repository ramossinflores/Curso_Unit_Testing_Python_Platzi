# src/banxico.py
import requests

SERIE_FIX_USD_MXN = "SF43718"
BASE_URL = "https://www.banxico.org.mx/SieAPIRest/service/v1"

# Función "API, ¿estás viva?" devuelve True si “parece” que Banxico está respondiendo
def api_is_up(timeout=2.0) -> bool:
    try:
        r = requests.get(BASE_URL, timeout=timeout)
        return r.status_code == 200
    except requests.RequestException:
        return False

# Función para obtener el tipo de cambio FIX USD→MXN
def get_usd_mxn_fix(token: str) -> float:
    url = f"{BASE_URL}/series/{SERIE_FIX_USD_MXN}/datos/oportuno"  # <- SIEMPRE definida
    headers = {"Bmx-Token": token}
    r = requests.get(url, headers=headers, params={"mediaType": "json"}, timeout=10)
    data = r.json()

    serie = data["bmx"]["series"][0]  
