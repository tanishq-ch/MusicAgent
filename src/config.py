"""
🎵 Voice Music Agent — Configuration
--------------------------------------
Edit this file to customise the agent for your setup.
No need to touch music_agent.py at all.
"""

from pathlib import Path

# ── Music Folder ───────────────────────────────────────────────────────────────
# Where your music lives. Defaults to C:\Users\YourName\Music
# Change this if your music is stored somewhere else, e.g.:
MUSIC_FOLDER = r"E:\songs"
#   MUSIC_FOLDER = r"C:\Users\YourName\Downloads\Songs"

# MUSIC_FOLDER = str(Path.home() / "Music")


# ── Audio File Types ───────────────────────────────────────────────────────────
# Searched in this order — the first match is played.

AUDIO_EXTENSIONS = [
    "*.mp3",
    "*.wav",
    "*.flac",
    "*.m4a",
    "*.ogg",
    "*.aac",
    "*.wma",
]


# ── Hotkey ─────────────────────────────────────────────────────────────────────
# Key combo to activate the microphone.
# Examples: "ctrl+alt+m", "ctrl+shift+s", "f9"

HOTKEY = "ctrl+alt+m"


# ── Listen Timeout ─────────────────────────────────────────────────────────────
# How many seconds to wait for speech before giving up.

LISTEN_TIMEOUT = 5


# ── Trigger Phrases ────────────────────────────────────────────────────────────
# If ANY of these are detected in your speech, music will play.
# Add your own phrases in your own language too!

TRIGGER_PHRASES = [
    "i want to hear a song",
    "i want to listen to music",
    "play some music",
    "play a song",
    "play music",
    "start music",
    "open music",
    "i want music",
    "put on some music",
    "play something",
    "music please",
    "start playing",
]
