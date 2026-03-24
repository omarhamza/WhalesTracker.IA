from WhalesAnalyzer import analyze
from config import SYMBOLS
from image_recorder import save_whale_detection_plot
from send_telegram_message import send_image

for symbol in SYMBOLS:
    # Analyse des transactions et détection des Whales
    df, whales = analyze(symbol)

    # Enregistrement du graphique
    save_whale_detection_plot(df, whales, symbol)

    # Envoi de l'image via Telegram
    image_path = f"whales_detection_{symbol}.png"
    caption = f"🐋 Détection de Whales pour {symbol} 🐋"
    send_image(image_path, caption)