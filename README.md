# SmartQuery – Application de Traitement du Signal et d’IA Conversationnelle

## Description
**SmartQuery** est une application de bureau interactive qui combine **traitement du signal**, **intelligence artificielle** et **interface graphique**.  
Elle permet :  
- La **reconnaissance vocale** pour interagir par la voix,  
- La **génération de réponses** avec l’API Google Generative AI (PaLM),  
- La **conversion texte en parole (TTS)** pour une interaction naturelle,  
- Une **interface Tkinter personnalisée** avec affichage enrichi en HTML/Markdown.  

Cette application illustre l’utilisation conjointe de la reconnaissance vocale, de l’IA générative et de la synthèse vocale dans un cadre ergonomique.  

## Fonctionnalités
- **Reconnaissance vocale** en anglais (via Google Speech Recognition API).  
- **Chat IA** avec Google PaLM configuré comme assistant développeur.  
- **Synthèse vocale (TTS)** avec `pyttsx3`.  
- **Interface utilisateur Tkinter** avec affichage HTML grâce à `tkhtmlview`.  
- **Multithreading** pour fluidifier les interactions (parole, affichage, IA).  
- **Authentification biométrique vocale** (concept démonstratif).  

## Technologies utilisées
- **Tkinter** → Interface graphique.  
- **SpeechRecognition + PyAudio** → Reconnaissance vocale.  
- **Google Generative AI (PaLM API)** → Génération de réponses IA.  
- **Markdown2 + BeautifulSoup** → Conversion et affichage Markdown/HTML.  
- **pyttsx3** → Synthèse vocale hors-ligne.  

## Installation et exécution

### Cloner le projet
```bash
git clone https://github.com/thiernodaoudaly/smartquery.git
cd SmartQuery
```

### Créer et activer un environnement virtuel

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### Installer les dépendances

```bash
pip install -r requirements.txt
```

### Lancer l’application

```bash
python window.py
```

## Aperçu

* Page d’accueil avec authentification biométrique vocale.
* Interface principale avec champ texte, boutons microphone et affichage interactif.
* Interaction fluide avec l’IA générative et retour audio en temps réel.

## Améliorations futures

* Ajouter le support multilingue (FR, EN, etc.).
* Enrichir l’authentification biométrique vocale avec un modèle ML.
* Intégrer une base de connaissances locale pour un assistant personnalisé.


