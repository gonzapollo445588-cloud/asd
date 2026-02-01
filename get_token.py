import requests
import os

def get_flow_token():
    canal = "Somos_Norte"
    url_inicial = f"https://chromecast.cvattv.com.ar/live/c6eds/{canal}/SA_Live_dash_enc_C/{canal}.mpd"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/121.0.0.0",
        "Origin": "https://portal.app.flow.com.ar",
        "Referer": "https://portal.app.flow.com.ar/"
    }

    try:
        print(f"Consultando canal: {canal}...")
        response = requests.get(url_inicial, headers=headers, timeout=15)
        url_final = response.url
        
        print(f"URL capturada: {url_final}")
        
        # Guardamos siempre, aunque no tenga el token, para ver qué devuelve
        with open("enlace.txt", "w") as f:
            f.write(url_final)
            
        if "tok_" in url_final:
            print("¡Éxito! Token encontrado.")
        else:
            print("Aviso: La URL no contiene 'tok_'. Posible bloqueo.")
            
    except Exception as e:
        print(f"Error crítico: {e}")
        # Creamos un archivo de error para que Git no falle al buscarlo
        with open("enlace.txt", "w") as f:
            f.write(f"Error: {str(e)}")

if __name__ == "__main__":
    get_flow_token()
