# WhaleTracker.IA

WhaleTracker.IA est un outil d'analyse de flux en temps réel permettant de détecter les transactions « Whales » sur les marchés financiers/crypto, en utilisant l'apprentissage non supervisé.

## 🚀 Objectif

- Détecter automatiquement les transactions avec comportement anormal (volume/volatilité élevés).
- Alerter les opérateurs via Telegram.
- Fournir un pipeline simple pour l'enregistrement d'images, l'analyse et le suivi.

## ⚙️ Installation

1. Créer un environnement virtuel Python :

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Installer les dépendances :

```bash
pip install -r src/requirements.txt
```

## ▶️ Usage

- Modifier `src/config.py` pour renseigner les clefs API Telegram et la configuration du flux.
- Lancer le script principal (selon implémentation) ou exécuter un module d’analyse.

```bash
python __init__.py
```

## 📌 Notes

- Isolation Forest est adapté aux anomalies vectorielles, mais il faut surveiller le taux de faux positifs.
- Ajuster le seuil de sensibilité (`contamination`) selon le contexte de marché.
- Configurer les seuils personnalisés dans `src/config.py` pour affiner la détection des transactions Whales.

## 🤝 Contribution

Les contributions sont les bienvenues : forker et créer une PR avec des améliorations de stabilité, logging, monitoring ou interface utilisateur.
