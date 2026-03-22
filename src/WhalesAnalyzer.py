import pandas as pd
from binance.client import Client
from sklearn.ensemble import IsolationForest

client = Client()

def analyze(symbol="BTCEUR"):
    
    trades = client.get_aggregate_trades(symbol=symbol, limit=10000)
    
    df = pd.DataFrame(trades)
    
    # Nettoyage et typage
    df['price'] = df['p'].astype(float)
    df['qty'] = df['q'].astype(float)
    df['value_eur'] = df['price'] * df['qty']
    # 'm' est True si c'est une vente (market taker sell)
    df['side'] = df['m'].apply(lambda x: 'VENTE' if x else 'ACHAT')

    # On isole les 1.5% de transactions les plus volumineuses
    model = IsolationForest(contamination=0.015, random_state=42)
    df['anomaly'] = model.fit_predict(df[['value_eur']])
    
    # Détection des Whales (Anomalies)
    whales = df[df['anomaly'] == -1]

    return df, whales