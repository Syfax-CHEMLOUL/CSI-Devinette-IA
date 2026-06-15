# 🤖 CSI — Devinette IA

> Projet réalisé pour le **Club Scientifique d'Informatique (CSI)**  
> Université Mouloud Mammeri de Tizi-Ouzou — UMMTO

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange.svg)](https://docs.python.org/3/library/tkinter.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Jeu de devinette interactif de type **Akinator**, où une IA tente de deviner à quoi vous pensez en posant des questions Oui/Non. L'IA utilise l'**entropie informationnelle** pour choisir à chaque tour la question la plus intelligente possible.

---

## 🎮 Démonstration

```
L'IA pose des questions...

  ❓ Est-ce vivant ?          → OUI
  ❓ Est-ce un humain ?       → OUI
  ❓ Est-il scientifique ?    → OUI
  ❓ Est-ce un personnage historique ? → OUI

  🎯 Tu pensais à : Albert Einstein
     Trouvé en 4 questions !
```

---

## 🧠 Comment ça marche ?

À chaque tour, l'IA ne pose pas une question au hasard. Elle calcule le **gain d'information** de chaque question possible et choisit celle qui divise le mieux les candidats restants — principe directement issu de la **théorie de l'information de Shannon**.

### Formule d'entropie

```
H(p) = -p · log₂(p) - (1-p) · log₂(1-p)
```

Plus l'entropie d'une question est élevée, plus elle est informative. L'IA sélectionne toujours la question au **gain d'information maximal**, ce qui lui permet de converger vers la bonne réponse en un minimum de questions.

### Exemple

Avec 19 candidats au départ :
- La question "Est-ce vivant ?" divise en 13 vivants / 6 non-vivants → très informative
- L'IA la pose en **premier** automatiquement

---

## 📦 Dataset

**19 éléments** répartis en 4 catégories :

| Catégorie | Exemples |
|-----------|----------|
| 👤 Personnages historiques | Einstein, Marie Curie, Napoléon, Newton... |
| 🐾 Animaux | Chat, Aigle, Requin |
| 💻 Objets | Smartphone, Avion, Ordinateur portable |
| 📖 Imaginaires | Superman, Dragon, Sabre laser |

**34 attributs binaires** : vivant, humain, scientifique, historique, sportif, nocturne, vole, électronique, imaginaire...

---

## ✨ Fonctionnalités

- 🔬 **Moteur d'inférence bayésien** — sélection de question par entropie maximale
- 🎨 **Interface graphique dark** — thème cyberpunk avec animations fluides
- 📊 **Barre de progression** — visualisation du processus d'élimination en temps réel
- 📜 **Historique des questions** — panel scrollable avec toutes les réponses
- 🔄 **Nouvelle partie** — reset complet en un clic
- 📋 **Liste des candidats restants** — dropdown mis à jour à chaque question

---

## 🚀 Lancer le projet

### Prérequis

- Python 3.x
- **Aucune dépendance externe** — uniquement la bibliothèque standard Python

### Installation

```bash
# Cloner le repo
git clone https://github.com/ton-username/csi-devinette-ia.git
cd csi-devinette-ia

# Lancer directement
python main.py
```

---

## 📁 Structure

```
csi-devinette-ia/
├── main.py       # Code source complet (IA + interface graphique)
└── README.md
```

---

## 🛠️ Tech Stack

- **Python 3.x** — langage principal
- **tkinter / ttk** — interface graphique native
- **math** — calcul d'entropie (log₂)
- Zéro dépendance externe — tourne sur n'importe quelle machine avec Python installé

---

## 📝 Licence

Ce projet est sous licence MIT — voir [LICENSE](LICENSE).

---

## 👤 CHEMLOUL Syfax

Projet développé dans le cadre des activités du **Club Scientifique d'Informatique (CSI)** — UMMTO, Tizi-Ouzou.
