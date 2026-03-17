# SmartQuery – Signal Processing and Conversational AI Application

## Description
**SmartQuery** is an interactive desktop application that combines **signal processing**, **artificial intelligence**, and a **graphical user interface**.  
It enables:  
- **Speech recognition** for voice interaction,  
- **Response generation** using the Google Generative AI API (PaLM),  
- **Text-to-speech (TTS)** for natural interaction,  
- A **custom Tkinter interface** with enhanced HTML/Markdown rendering.  

This application demonstrates the integration of speech recognition, generative AI, and speech synthesis in an ergonomic environment.

## Features
- **Speech recognition** in English (via Google Speech Recognition API).  
- **AI chat** powered by Google PaLM configured as a developer assistant.  
- **Text-to-speech (TTS)** using `pyttsx3`.  
- **Tkinter user interface** with HTML rendering via `tkhtmlview`.  
- **Multithreading** for smooth interactions (speech, display, AI).  
- **Voice biometric authentication** (proof-of-concept).  

## Technologies Used
- **Tkinter** → Graphical user interface  
- **SpeechRecognition + PyAudio** → Speech recognition  
- **Google Generative AI (PaLM API)** → AI response generation  
- **Markdown2 + BeautifulSoup** → Markdown to HTML conversion and rendering  
- **pyttsx3** → Offline text-to-speech  

## Installation and Setup

### Clone the repository
```bash
git clone https://github.com/thiernodaoudaly/smartquery.git
cd SmartQuery
```
### Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```
### Install dependencies
```bash
pip install -r requirements.txt
```
### Run the application
```bash
python window.py
```

## Preview
- Home screen with voice biometric authentication
- Main interface with text input, microphone buttons, and interactive display
- Smooth interaction with generative AI and real-time audio feedback

## Future Improvements
- Add multilingual support (FR, EN, etc.)
- Enhance voice biometric authentication with a machine learning model
- Integrate a local knowledge base for a personalized assistant

## Contributors
- Michel Junior DELANOUE
- Thierno Daouda LY
- Ndeye Fatou NIASSY