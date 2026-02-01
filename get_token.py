import requests

def get_flow_token():
    canal = "Somos_Norte"
    url_inicial = f"https://chromecast.cvattv.com.ar/live/c6eds/{canal}/SA_Live_dash_enc_C/{canal}.mpd"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Origin": "https://portal.app.flow.com.ar",
        "Referer": "https://portal.app.flow.com.ar/"
    }
    try:
        response = requests.get(url_inicial, headers=headers, timeout=15)
        if "tok_" in response.url:
            with open("enlace.txt", "w") as f:
                f.write(response.url)
            print("Enlace guardado!")
        else:
            print("No se encontró el token")
    except:
        print("Error de conexión")

if __name__ == "__main__":
    get_flow_token()
