# Configuration
TELEGRAM_TOKEN = ""
TELEGRAM_CHAT_ID = ""

SYMBOLS = ['BTCEUR', 'ETHEUR', 'SOLEUR']

# Seuils de prix minimum par symbole (en EUR)
# Les whales en dessous de ce seuil seront ignorés
PRICE_THRESHOLDS = {
    'BTCEUR': 5000,  # Minimum 5000 EUR pour BTC
    'ETHEUR': 1500,   # Minimum 1500 EUR pour ETH
    'SOLEUR': 600,    # Minimum 600 EUR pour SOL
}