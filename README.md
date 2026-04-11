# SmartQuery — Voice-Enabled AI Assistant Desktop App

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-FF6B6B?style=flat-square)
![Google PaLM](https://img.shields.io/badge/Google-PaLM%20API-4285F4?style=flat-square&logo=google&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

**Desktop assistant that understands voice, queries Google PaLM, renders structured Markdown responses, and reads them back aloud — all in a custom Tkinter interface.**

</div>

## Overview

SmartQuery is a desktop application combining speech recognition, generative AI, and text-to-speech in a single Tkinter window. Users can interact via text or microphone — the app sends the query to Google's PaLM API (configured as a developer assistant), converts the Markdown response to HTML, renders it inline, and reads it back with speech synthesis.

## Features

- **Speech-to-text** — records from microphone via Google Speech Recognition API (English)
- **AI chat** — multi-turn conversation with Google PaLM, configured as a developer assistant that returns structured Markdown
- **Markdown → HTML rendering** — `markdown2` converts PaLM's response, `tkhtmlview` renders it inline in the Tkinter window with proper code blocks and formatting
- **Text-to-speech** — `pyttsx3` reads every AI response aloud (offline, female voice, 150 wpm)
- **Multithreading** — speech recognition and TTS run in separate threads to keep the UI responsive
- **Voice biometric authentication** — home screen proof-of-concept with microphone authentication before accessing the main interface

## Architecture

```
window.py
│
├── Home screen (Tkinter)
│   └── Voice biometric button → opens main window
│
└── Main window (Tkinter 1000×800)
    ├── HTMLLabel (tkhtmlview)     ← renders Markdown AI responses as HTML
    ├── Text input (Tkinter Text)  ← typed or voice-filled query
    ├── Search button              → calls chat() → PaLM API → update display + TTS
    ├── Microphone button          → Thread: listen() → Google STT → fill input
    └── TTS engine (pyttsx3)       → Thread: reads response aloud
```

**Conversation flow:**

```
User input (text or voice)
        │
        ▼
   palm.chat().reply(msg)          ← multi-turn PaLM conversation
        │
        ▼
   markdown2.Markdown().convert()  ← Markdown → HTML
        │
   ┌────┴────────────────────┐
   ▼                         ▼
HTMLLabel.set_html()     BeautifulSoup.get_text()
(render in window)       (strip HTML for TTS)
                              │
                              ▼
                         pyttsx3.say()  ← read aloud in thread
```

## Tech Stack

| Component | Technology |
|---|---|
| GUI | Tkinter + Canvas |
| HTML rendering | `tkhtmlview` — `HTMLLabel` |
| Speech recognition | `SpeechRecognition` + Google Speech API |
| AI responses | Google Generative AI — PaLM (`google-generativeai`) |
| Markdown conversion | `markdown2` |
| HTML parsing (for TTS) | `BeautifulSoup4` |
| Text-to-speech | `pyttsx3` (offline) |
| Concurrency | Python `threading.Thread` |

---

## Setup & Usage

**Prerequisites:** Python 3.x, a working microphone, a Google PaLM API key

```bash
# Clone the repository
git clone https://github.com/thiernodaoudaly/smartquery.git
cd smartquery

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Linux / macOS
# venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt

# Run the application
python window.py
```

> **PyAudio installation note:** on some systems PyAudio requires a system-level dependency.
> - Linux: `sudo apt-get install portaudio19-dev` then `pip install pyaudio`
> - macOS: `brew install portaudio` then `pip install pyaudio`
> - Windows: `pip install pipwin && pipwin install pyaudio`

---

## Security Note

The current code contains a **hardcoded API key** directly in `window.py`. Before pushing to a public repository, move it to an environment variable:

```python
# Instead of:
palm.configure(api_key="AIzaSy...")

# Use:
import os
palm.configure(api_key=os.getenv("PALM_API_KEY"))
```

Then create a `.env` file (gitignored):
```env
PALM_API_KEY=your-key-here
```

## Roadmap

- [ ] Move API key to environment variable (`.env`)
- [ ] Add multilingual support (French, English, etc.)
- [ ] Replace PaLM with Gemini API (PaLM is deprecated)
- [ ] Implement real voice biometric authentication with a speaker recognition ML model
- [ ] Integrate a local knowledge base for a personalised assistant

## Contributors

**Thierno Daouda LY · Michel Junior DELANOUE · Ndeye Fatou NIASSY**

## License

MIT License — see [LICENSE](LICENSE) for details.