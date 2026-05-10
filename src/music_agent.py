"""
🎵 Voice Music Agent — Core Agent
-----------------------------------
Press Ctrl+Alt+M → Speak → AI detects intent → Opens music folder & plays first song

Part of: voice-music-agent (github.com/YOUR_USERNAME/voice-music-agent)
"""

import os
import glob
import time
import threading
import subprocess
import speech_recognition as sr
import keyboard
from pathlib import Path
from config import (
    MUSIC_FOLDER,
    AUDIO_EXTENSIONS,
    HOTKEY,
    LISTEN_TIMEOUT,
    TRIGGER_PHRASES,
)


# ─────────────────────────────────────────────
# CORE LOGIC
# ─────────────────────────────────────────────

recognizer = sr.Recognizer()
is_listening = False  # prevents double-trigger on rapid hotkey press


def find_first_song() -> str | None:
    """Scan MUSIC_FOLDER and return the path to the first audio file found."""
    if not os.path.exists(MUSIC_FOLDER):
        print(f"[!] Music folder not found: {MUSIC_FOLDER}")
        print("    → Update MUSIC_FOLDER in src/config.py")
        return None

    for ext in AUDIO_EXTENSIONS:
        matches = sorted(
            glob.glob(os.path.join(MUSIC_FOLDER, "**", ext), recursive=True)
        )
        if matches:
            return matches[0]

    print("[!] No audio files found in:", MUSIC_FOLDER)
    return None


def open_music_folder() -> None:
    """Open the music folder in Windows Explorer."""
    if os.path.exists(MUSIC_FOLDER):
        subprocess.Popen(f'explorer "{MUSIC_FOLDER}"')
        print(f"[✓] Opened folder: {MUSIC_FOLDER}")
    else:
        print(f"[!] Music folder not found: {MUSIC_FOLDER}")


def play_song(filepath: str) -> None:
    """Play a file using the OS default media player (VLC, WMP, etc.)."""
    print(f"[♪] Playing: {os.path.basename(filepath)}")
    os.startfile(filepath)  # Windows: opens with default associated app


def is_music_intent(text: str) -> bool:
    """
    Return True if the spoken text matches a known music trigger phrase,
    or contains enough music-related keywords to be considered a match.
    """
    text = text.lower().strip()

    # Exact phrase match
    for phrase in TRIGGER_PHRASES:
        if phrase in text:
            return True

    # Fuzzy fallback: 2+ music keywords present
    keywords = ["music", "song", "play", "hear", "listen", "track", "audio"]
    matched = sum(1 for kw in keywords if kw in text)
    return matched >= 2


def listen_and_respond() -> None:
    """Activate microphone, transcribe speech, and act on music intent."""
    global is_listening
    if is_listening:
        return  # Already in a listening session

    is_listening = True
    _status("🎤 Listening... speak now!")

    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(
                source, timeout=LISTEN_TIMEOUT, phrase_time_limit=8
            )

        _status("🔄 Processing speech...")
        text = recognizer.recognize_google(audio)
        print(f'[👂] You said: "{text}"')

        if is_music_intent(text):
            print("[✓] Music intent detected!")
            _status("🎵 Opening music...")
            open_music_folder()
            time.sleep(0.5)  # let Explorer open first
            song = find_first_song()
            if song:
                play_song(song)
                _status(f"♪ Now playing: {os.path.basename(song)}")
            else:
                _status("⚠  No songs found in folder")
        else:
            print(f'[~] No music intent in: "{text}"')
            _status("💬 Command not recognised — try again")

    except sr.WaitTimeoutError:
        _status("⏱ No speech detected — try again")
    except sr.UnknownValueError:
        _status("❓ Couldn't understand audio — try again")
    except sr.RequestError as e:
        print(f"[!] Speech API error: {e}")
        _status("⚠  Recognition error (check internet)")
    except Exception as e:
        print(f"[!] Unexpected error: {e}")
        _status("⚠  Something went wrong")
    finally:
        is_listening = False


def _status(msg: str) -> None:
    print(f"    ── {msg}")


def on_hotkey() -> None:
    """Hotkey callback — spawns listener on a background thread."""
    thread = threading.Thread(target=listen_and_respond, daemon=True)
    thread.start()


# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────

def main() -> None:
    print("=" * 55)
    print("  🎵  Voice Music Agent")
    print("=" * 55)
    print(f"  Hotkey    : {HOTKEY.upper()}")
    print(f"  Music dir : {MUSIC_FOLDER}")
    print(f"  Engine    : Google Speech Recognition")
    print("=" * 55)
    print(f"\n  Press  {HOTKEY.upper()}  anywhere to activate.")
    print('  Say something like: "I want to hear a song"')
    print("  Press  Ctrl+C  to quit.\n")

    if not os.path.exists(MUSIC_FOLDER):
        print(f"  ⚠  WARNING: Music folder not found at:\n     {MUSIC_FOLDER}")
        print("     → Edit MUSIC_FOLDER in src/config.py\n")

    keyboard.add_hotkey(HOTKEY, on_hotkey)

    try:
        keyboard.wait()
    except KeyboardInterrupt:
        print("\n[✓] Agent stopped. Goodbye!")


if __name__ == "__main__":
    main()
