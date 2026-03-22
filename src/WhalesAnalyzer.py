import pandas as pd
from binance.client import Client
from sklearn.ensemble import IsolationForest
from image_recorder import save_whale_detection_plot

client = Client()

def analyze(symbol="BTCEUR"):
    
    trades = client.get_aggregate_trades(symbol=symbol, limit=10000)
    
    df = pd.DataFrame(trades)
    
    # Nettoyage et typage
    df['price_eur'] = df['p'].astype(float)
    df['qty'] = df['q'].astype(float)
    df['value_eur'] = df['price_eur'] * df['qty']
    # 'm' est True si c'est une vente (market taker sell)
    df['side'] = df['m'].apply(lambda x: 'VENTE' if x else 'ACHAT')

    # On isole les 1.5% de transactions les plus volumineuses
    model = IsolationForest(contamination=0.015, random_state=42)
    df['anomaly'] = model.fit_predict(df[['value_eur']])
    
    # Détection des Whales (Anomalies)
    whales = df[df['anomaly'] == -1]

    # Enregistrement du graphique
    save_whale_detection_plot(df, whales, symbol)

    # Affichage console des plus grosses transactions
    print(f"\n--- Dernières Whales détectées sur {symbol} ---")
    print(whales[['price_eur', 'qty', 'value_eur', 'side']].tail(5))