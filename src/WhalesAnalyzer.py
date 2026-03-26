import pandas as pd
from binance.client import Client
from sklearn.ensemble import IsolationForest
from config import PRICE_THRESHOLDS

client = Client()

def analyze(symbol="BTCEUR"):

    threshold = PRICE_THRESHOLDS.get(symbol, 0)
    
    trades = client.get_aggregate_trades(symbol=symbol, limit=10000)
    
    df = pd.DataFrame(trades)
    
    # Nettoyage et typage
    df['price'] = df['p'].astype(float)

    df['qty'] = df['q'].astype(float)
    df['value_eur'] = df['price'] * df['qty']
    # 'm' est True si c'est une vente (market taker sell)
    df['side'] = df['m'].apply(lambda x: 'VENTE' if x else 'ACHAT')

    # Filtrer les transactions en dessous du seuil de prix
    df = df[df['value_eur'] > threshold]

    if (len(df) == 0):
        print(f"⚠️ Aucune transaction au-dessus du seuil de {threshold} EUR pour {symbol}.")
        return df, pd.DataFrame()  # Retourner un DataFrame vide si aucune transaction ne dépasse le seuil

    # On isole les 1.5% de transactions les plus volumineuses
    model = IsolationForest(contamination=0.015, random_state=42)
    df['anomaly'] = model.fit_predict(df[['value_eur']])
    
    # Détection des Whales (Anomalies)
    whales = df[df['anomaly'] == -1]

    return df, whales