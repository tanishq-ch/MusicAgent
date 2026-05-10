"""
🎵 Voice Music Agent — System Tray App
----------------------------------------
Runs the agent silently in the Windows system tray.
Right-click the tray icon to see options.

Requires: pip install pystray pillow
"""

import threading
import sys
import os
import subprocess
import winreg
from pathlib import Path

import pystray
from PIL import Image, ImageDraw
import keyboard

# Import agent logic
sys.path.insert(0, os.path.dirname(__file__))
from music_agent import on_hotkey, HOTKEY
from config import MUSIC_FOLDER

# ── App identity ───────────────────────────────────────────────────────────────
APP_NAME   = "VoiceMusicAgent"
SCRIPT_PATH = str(Path(__file__).resolve())          # absolute path to this file
PYTHON_EXE  = sys.executable                          # python.exe that's running now

# ── Tray icon state ────────────────────────────────────────────────────────────
agent_active = True   # whether hotkey is currently registered


# ─────────────────────────────────────────────
# ICON — drawn with Pillow (no image file needed)
# ─────────────────────────────────────────────

def make_icon(active: bool) -> Image.Image:
    """Draw a simple musical-note icon. Green = active, grey = paused."""
    size   = 64
    img    = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw   = ImageDraw.Draw(img)
    color  = (52, 199, 89) if active else (150, 150, 150)   # green / grey

    # Note stem
    draw.rectangle([38, 10, 44, 44], fill=color)
    # Note head
    draw.ellipse([22, 38, 44, 54], fill=color)
    # Flag
    draw.line([44, 10, 58, 22], fill=color, width=4)

    return img


# ─────────────────────────────────────────────
# AUTOSTART HELPERS (Windows Registry)
# ─────────────────────────────────────────────

REG_PATH = r"Software\Microsoft\Windows\CurrentVersion\Run"

def is_autostart_enabled() -> bool:
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_READ)
        winreg.QueryValueEx(key, APP_NAME)
        winreg.CloseKey(key)
        return True
    except FileNotFoundError:
        return False


def enable_autostart() -> None:
    """Add registry entry so agent starts with Windows."""
    cmd = f'"{PYTHON_EXE}" "{SCRIPT_PATH}"'
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_SET_VALUE)
    winreg.SetValueEx(key, APP_NAME, 0, winreg.REG_SZ, cmd)
    winreg.CloseKey(key)


def disable_autostart() -> None:
    """Remove registry entry."""
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_SET_VALUE)
        winreg.DeleteValue(key, APP_NAME)
        winreg.CloseKey(key)
    except FileNotFoundError:
        pass


# ─────────────────────────────────────────────
# TRAY MENU ACTIONS
# ─────────────────────────────────────────────

def toggle_agent(icon: pystray.Icon, item) -> None:
    """Pause or resume the hotkey listener."""
    global agent_active
    if agent_active:
        keyboard.remove_hotkey(HOTKEY)
        agent_active = False
        print("[~] Agent paused.")
    else:
        keyboard.add_hotkey(HOTKEY, on_hotkey)
        agent_active = True
        print("[✓] Agent resumed.")
    icon.icon = make_icon(agent_active)
    icon.menu = build_menu(icon)


def toggle_autostart(icon: pystray.Icon, item) -> None:
    """Toggle Windows startup entry."""
    if is_autostart_enabled():
        disable_autostart()
        print("[~] Removed from Windows startup.")
    else:
        enable_autostart()
        print("[✓] Added to Windows startup.")
    icon.menu = build_menu(icon)


def open_music_folder_action(icon, item) -> None:
    """Open the music folder from the tray menu."""
    if os.path.exists(MUSIC_FOLDER):
        subprocess.Popen(f'explorer "{MUSIC_FOLDER}"')
    else:
        print(f"[!] Music folder not found: {MUSIC_FOLDER}")


def quit_agent(icon: pystray.Icon, item) -> None:
    """Clean shutdown."""
    print("[✓] Quitting Voice Music Agent...")
    keyboard.unhook_all_hotkeys()
    icon.stop()


def build_menu(icon: pystray.Icon) -> pystray.Menu:
    """Build the right-click tray menu dynamically."""
    pause_label    = "⏸  Pause agent" if agent_active else "▶️  Resume agent"
    autostart_tick = "✅" if is_autostart_enabled() else "☐ "
    hotkey_display = HOTKEY.upper().replace("+", " + ")

    return pystray.Menu(
        pystray.MenuItem(f"🎵 Voice Music Agent", None, enabled=False),
        pystray.MenuItem(f"    Hotkey: {hotkey_display}", None, enabled=False),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem(pause_label, lambda i, it: toggle_agent(i, it)),
        pystray.MenuItem(f"{autostart_tick}  Start with Windows", lambda i, it: toggle_autostart(i, it)),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem("📂  Open music folder", open_music_folder_action),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem("❌  Quit", quit_agent),
    )


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def main() -> None:
    print("=" * 50)
    print("  🎵  Voice Music Agent — Tray Mode")
    print("=" * 50)
    print(f"  Hotkey : {HOTKEY.upper()}")
    print(f"  Music  : {MUSIC_FOLDER}")
    print("  Running in system tray — check bottom-right.")
    print("=" * 50)

    # Register hotkey
    keyboard.add_hotkey(HOTKEY, on_hotkey)

    # Create tray icon
    icon = pystray.Icon(
        APP_NAME,
        icon=make_icon(active=True),
        title="Voice Music Agent",
    )
    icon.menu = build_menu(icon)

    # Run tray (blocks until quit)
    icon.run()


if __name__ == "__main__":
    main()
