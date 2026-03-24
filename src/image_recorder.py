import matplotlib.pyplot as plt


def save_whale_detection_plot(df, whales, symbol):

    # Visualisation
    plt.figure(figsize=(12, 6))
    
    # Transactions classiques
    normal = df[df['anomaly'] == 1]
    plt.scatter(normal.index, normal['qty'], c='#3498db', alpha=0.4, label='Trades Standards')
    
    # Distinction Achat/Vente pour les Whales
    for side, color, marker in [('ACHAT', '#2ecc71', '^'), ('VENTE', '#e74c3c', 'v')]:
        subset = whales[whales['side'] == side]
        plt.scatter(subset.index, subset['qty'], 
                    c=color, label=f'Whale {side}', 
                    s=120, marker=marker, edgecolors='black')

    plt.title(f"Détection de Whales en Direct EUR - {symbol}")
    plt.ylabel("Valeur de la transaction (€)")
    plt.xlabel("Flux des 1000 dernières transactions")
    plt.legend()
    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    plt.savefig(f"whales_detection_{symbol}.png", dpi=100, bbox_inches='tight')
    plt.close()
