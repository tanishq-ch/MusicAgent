<div align="center">

# 🎵 Voice Music Agent

**A voice-activated local music agent for Windows.**
Press a hotkey, speak a phrase, and your music plays — instantly, automatically, no streaming apps needed.

<br/>

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Windows%2010%2F11-0078D6?style=for-the-badge&logo=windows&logoColor=white)](https://microsoft.com/windows)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-22c55e?style=for-the-badge)]()

<br/>

> 🎤 Press `Ctrl+Alt+M` → Say *"Play some music"* → Done.

</div>

---

## 📖 Table of Contents

- [How It Works](#-how-it-works)
- [System Tray](#%EF%B8%8F-system-tray)
- [Quick Start](#-quick-start)
- [Usage](#-usage)
- [Configuration](#%EF%B8%8F-configuration)
- [Project Structure](#-project-structure)
- [Roadmap](#-roadmap)
- [Troubleshooting](#-troubleshooting)
- [License](#-license)

---

## ✨ How It Works

<div align="center">

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│   Press  Ctrl + Alt + M                             │
│              │                                      │
│              ▼                                      │
│   🎤  Microphone activates                          │
│              │                                      │
│              ▼                                      │
│   🗣️  You say  "I want to hear a song"              │
│              │                                      │
│              ▼                                      │
│   🧠  AI detects music intent                       │
│              │                                      │
│              ▼                                      │
│   📂  Music folder opens  +  🎵 Song plays          │
│                                                     │
└─────────────────────────────────────────────────────┘
```

</div>

The agent runs silently in your **system tray** 24/7 — even after you close VS Code or restart your PC. No streaming, no Spotify, no subscriptions. Just your local music files.

---

## 🖥️ System Tray

The agent lives as a small **music note icon** in your taskbar (bottom-right corner). Right-click it for full control:

<div align="center">

| Option | Description |
|:-------|:------------|
| ⏸ **Pause agent** | Temporarily disable the hotkey |
| ✅ **Start with Windows** | Auto-launch on every boot |
| 📂 **Open music folder** | Browse your songs instantly |
| ❌ **Quit** | Shut the agent down |

</div>

> 💡 **Tip:** Enable **"Start with Windows"** once and you'll never have to manually launch it again.

---

## 🚀 Quick Start

### Prerequisites

Before you begin, make sure you have:

| Requirement | Details |
|:------------|:--------|
| 🪟 **Windows 10 or 11** | Required OS |
| 🐍 **Python 3.10+** | [Download from python.org](https://python.org) |
| 🎙️ **Working microphone** | Built-in or external |
| 🌐 **Internet connection** | For Google Speech Recognition |

---

### Step 1 — Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/voice-music-agent.git
cd voice-music-agent
```

---

### Step 2 — Install dependencies

```bash
pip install -r requirements.txt
```

> ⚠️ **PyAudio failing on Windows?** Use `pipwin` instead — it's much easier:
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```

---

### Step 3 — Set your music folder

Open `src/config.py` and point it to where your music lives:

```python
# Example paths:
MUSIC_FOLDER = r"C:\Users\YourName\Music"
MUSIC_FOLDER = r"D:\My Songs"
MUSIC_FOLDER = r"C:\Users\YourName\Downloads\Music"
```

---

### Step 4 — Launch the agent

```bash
# Option A — via terminal
python src/tray_app.py

# Option B — just double-click
run.bat
```

A 🎵 icon will appear in your system tray. You're live!

---

## 🎤 Usage

### Controls

| Action | How |
|:-------|:----|
| **Activate microphone** | Press `Ctrl + Alt + M` |
| **Play music** | Say any trigger phrase |
| **Pause / Resume agent** | Right-click tray icon |
| **Quit** | Right-click tray → Quit |

---

### 🗣️ Trigger Phrases

Say any of these after pressing the hotkey:

```
"I want to hear a song"        "Play some music"
"Play a song"                  "I want to listen to music"
"Put on some music"            "Music please"
"Start playing"                "Play something"
"I want music"                 "Start music"
```

> ✏️ Add your own phrases (even in other languages!) in `src/config.py` under `TRIGGER_PHRASES`.

---

## ⚙️ Configuration

Everything is controlled from **`src/config.py`** — you never need to touch the main agent code.

```python
# 📁 Where your music lives
MUSIC_FOLDER = str(Path.home() / "Music")

# ⌨️ Hotkey to activate the mic
HOTKEY = "ctrl+alt+m"

# ⏱️ Seconds to wait for you to speak
LISTEN_TIMEOUT = 5

# 🎵 File types to scan (in priority order)
AUDIO_EXTENSIONS = ["*.mp3", "*.wav", "*.flac", "*.m4a", "*.ogg", "*.aac", "*.wma"]

# 🗣️ Phrases that trigger playback
TRIGGER_PHRASES = [
    "i want to hear a song",
    "play some music",
    # ... add your own here
]
```

---

## 📁 Project Structure

```
voice-music-agent/
│
├── 📂 src/
│   ├── 🤖 music_agent.py        ← Core AI agent logic
│   ├── 🖥️  tray_app.py           ← System tray interface
│   └── ⚙️  config.py             ← All your settings
│
├── 📂 future/                    ← Planned features (coming soon)
│   ├── 🟢 spotify_support.py
│   ├── 🔴 youtube_music_support.py
│   └── 🔵 offline_recognition.py
│
├── 📄 requirements.txt
├── 🦇 run.bat                    ← Windows one-click launcher
├── 🙈 .gitignore
└── 📖 README.md
```

---

## 🔮 Roadmap

Here's what's coming in future versions:

| Feature | Status |
|:--------|:-------|
| 🎙️ Offline speech recognition (OpenAI Whisper) | 🟡 Planned |
| 🟢 Spotify integration via Web API | 🟡 Planned |
| 🔴 YouTube Music browser support | 🟡 Planned |
| 🔀 Shuffle / random song playback | 🟡 Planned |
| 🍎 macOS & Linux support | 🟡 Planned |
| 🗂️ Play by genre / folder name | 🟡 Planned |

Have an idea? [Open an issue](https://github.com/YOUR_USERNAME/voice-music-agent/issues) or submit a PR — contributions are welcome!

---

## 🛠️ Troubleshooting

<details>
<summary><b>❌ PyAudio install fails</b></summary>

Use `pipwin` instead of pip directly:
```bash
pip install pipwin
pipwin install pyaudio
```
</details>

<details>
<summary><b>❌ "No speech detected" error</b></summary>

- Check that your mic is set as the **default recording device**
- Go to: Windows Settings → Sound → Input → choose your mic
- Test it with the volume meter — make sure it reacts when you speak
</details>

<details>
<summary><b>❌ "Could not understand audio"</b></summary>

- Speak **clearly and a bit louder** than normal
- Move closer to the microphone
- Reduce background noise (fans, TV, etc.)
- Make sure you have a stable internet connection
</details>

<details>
<summary><b>❌ Music folder not found</b></summary>

Open `src/config.py` and set the exact path:
```python
MUSIC_FOLDER = r"C:\Users\YourName\Music"
```
Use `r"..."` (raw string) to avoid backslash issues on Windows.
</details>

<details>
<summary><b>❌ Songs aren't playing</b></summary>

Make sure `.mp3` files have a **default app** assigned:
- Right-click any `.mp3` → Open With → Choose default
- Recommended: **VLC Media Player** or **Windows Media Player**
</details>

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and share.

---

<div align="center">

*For anyone who just wants to press a button and hear music.*

⭐ **Star this repo if it helped you!**

</div>