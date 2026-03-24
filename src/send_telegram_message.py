import requests
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

def notify(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    title = "Whales tracker"
    full_message = f"{title}\n{message}"

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": full_message,
        "parse_mode": "Markdown"
    }
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print("Erreur envoi Telegram :", e)

def send_image(image_path, caption=""):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto"
    
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "caption": caption,
        "parse_mode": "Markdown"
    }
    try:
        with open(image_path, 'rb') as image_file:
            files = {'photo': image_file}
            response = requests.post(url, data=payload, files=files)
            if response.status_code != 200:
                print(f"Erreur envoi image Telegram: {response.text}")
    except Exception as e:
        print("Erreur envoi image Telegram :", e)