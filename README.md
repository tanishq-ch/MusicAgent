# 🎵 Voice Music Agent

A lightweight, voice-activated music agent for Windows. Press a hotkey, say the phrase, and your music folder opens and plays automatically — no Spotify, no streaming, no internet required (except for speech recognition).

---

## ✨ How It Works

```
Press Ctrl+Alt+M
      ↓
Microphone activates
      ↓
You say "I want to hear a song"
      ↓
AI detects music intent
      ↓
Music folder opens in Explorer + first song plays
```

---

## 🖥️ System Tray

The agent runs silently as a tray icon in the bottom-right of your taskbar. **Right-click it** to:

| Option | What it does |
|--------|-------------|
| ⏸ Pause agent | Temporarily disable the hotkey |
| ☐ Start with Windows | Toggle auto-start on boot |
| 📂 Open music folder | Open your folder directly |
| ❌ Quit | Shut down the agent |

Once you enable **"Start with Windows"**, the agent launches automatically every time you boot — no VS Code, no terminal needed.

---

## 🚀 Quick Start

### 1. Prerequisites

- **Windows 10 or 11**
- **Python 3.10+** → [Download here](https://python.org)
- A working **microphone**
- An **internet connection** (for Google Speech Recognition)

### 2. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/voice-music-agent.git
cd voice-music-agent
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> **Note for PyAudio on Windows:** If `pip install pyaudio` fails, download the pre-built wheel from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install with:
> ```bash
> pip install PyAudio‑0.2.13‑cpXX‑cpXX‑win_amd64.whl
> ```

### 4. Set your music folder

Open `src/config.py` and update:

```python
MUSIC_FOLDER = r"C:\Users\YourName\Music"   # ← change this
```

### 5. Run the agent

```bash
python src/music_agent.py
```

Or just double-click **`run.bat`**.

---

## 🎤 Usage

| Action | What to do |
|--------|-----------|
| Activate mic | Press `Ctrl + Alt + M` |
| Trigger music | Say one of the phrases below |
| Stop the agent | Press `Ctrl + C` in the terminal |

### Recognised phrases (any of these work)

- *"I want to hear a song"*
- *"Play some music"*
- *"Play a song"*
- *"I want to listen to music"*
- *"Put on some music"*
- *"Music please"*
- *"Start playing"*
- ...and more — see `src/config.py`

---

## ⚙️ Configuration

All settings are in **`src/config.py`** — you never need to edit the main script.

| Setting | Default | Description |
|---------|---------|-------------|
| `MUSIC_FOLDER` | `~/Music` | Path to your local music folder |
| `HOTKEY` | `ctrl+alt+m` | Key combo to activate the mic |
| `LISTEN_TIMEOUT` | `5` | Seconds to wait for speech |
| `AUDIO_EXTENSIONS` | mp3, wav, flac... | File types to look for |
| `TRIGGER_PHRASES` | *(list)* | Phrases that start music playback |

---

## 📁 Project Structure

```
voice-music-agent/
├── src/
│   ├── music_agent.py      # Main agent — run this
│   └── config.py           # All your settings live here
├── future/
│   ├── spotify_support.py      # 🔮 Planned
│   ├── youtube_music_support.py # 🔮 Planned
│   └── offline_recognition.py  # 🔮 Planned
├── requirements.txt
├── run.bat                 # Windows one-click launcher
├── .gitignore
└── README.md
```

---

## 🔮 Roadmap

These features are planned for future releases:

- [ ] **Offline speech recognition** — use [OpenAI Whisper](https://github.com/openai/whisper) locally, no internet needed
- [ ] **Spotify integration** — detect and control Spotify via the Web API
- [ ] **YouTube Music support** — open and play via browser
- [ ] **Shuffle / random song** — instead of always playing the first file
- [ ] **macOS & Linux support** — cross-platform hotkeys and playback
- [ ] **System tray icon** — run silently in background with a tray UI

Contributions welcome! Open an issue or a PR.

---

## 🛠 Troubleshooting

**`PyAudio` install fails**
→ Download the `.whl` file manually from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)

**"No speech detected"**
→ Make sure your mic is set as the default recording device in Windows Sound settings

**"Could not understand audio"**
→ Speak clearly and closer to the mic; reduce background noise

**Music folder not found**
→ Update `MUSIC_FOLDER` in `src/config.py` to the exact path of your music

**Songs not playing**
→ Make sure you have a default app set for `.mp3` files (e.g. VLC or Windows Media Player)

---

## 📄 License

MIT — free to use, modify, and share.

---

> Built with Python, `SpeechRecognition`, `keyboard`, and a love for local music libraries.
