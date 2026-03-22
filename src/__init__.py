from WhalesAnalyzer import analyze
from config import SYMBOLS
from image_recorder import save_whale_detection_plot

for symbol in SYMBOLS:
    # Analyse des transactions et détection des Whales
    df, whales = analyze(symbol)

    # Enregistrement du graphique
    save_whale_detection_plot(df, whales, symbol)

    # Affichage console des plus grosses transactions
    print(f"\n--- Dernières Whales détectées sur {symbol} ---")
    print(whales[['price_eur', 'qty', 'value_eur', 'side']].tail(5))
