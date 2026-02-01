import requests

def get_flow_token():
    canal = "Somos_Norte"
    url_inicial = f"https://chromecast.cvattv.com.ar/live/c6eds/{canal}/SA_Live_dash_enc_C/{canal}.mpd"
    
    # Inventamos una IP residencial de Argentina (de Telecom)
    ip_falsa_ar = "181.15.154.156" 

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/121.0.0.0",
        "X-Forwarded-For": ip_falsa_ar,
        "Client-IP": ip_falsa_ar,
        "Via": ip_falsa_ar,
        "Origin": "https://portal.app.flow.com.ar",
        "Referer": "https://portal.app.flow.com.ar/"
    }

    try:
        # Bajamos el timeout para que no se quede colgado si está bloqueado
        response = requests.get(url_inicial, headers=headers, timeout=10)
        with open("enlace.txt", "w") as f:
            f.write(response.url)
    except Exception as e:
        with open("enlace.txt", "w") as f:
            f.write(f"Sigue bloqueado. Error: {str(e)}")

if __name__ == "__main__":
    get_flow_token()
