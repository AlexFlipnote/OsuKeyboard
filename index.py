import ctypes
import os
import random
import sys

from utils import special_keys
from utils.playsound import playsound
from utils.pyhooked import Hook, KeyboardEvent


class OsuKeyboard:
    def __init__(self, s_folder: str = "sounds"):
        self.version = "1.0.4"
        self.s_folder = s_folder
        self.ignore_keys = special_keys.listing

        self.welcome_message()
        ctypes.windll.kernel32.SetConsoleTitleW("OsuKeyboard")
        self.hook_handler()

    def welcome_message(self):
        """ Welcome (to Osu!) """
        print(f"OsuKeyboard {self.version}\nCreated by: AlexFlipnote\n")

    def get_true_filename(self, filename):
        """ Get the assets files when used with .exe """
        try:
            base = sys._MEIPASS
        except Exception:
            base = os.path.abspath(".")
        return os.path.join(base, filename)

    def play(self, filename: str):
        """ Play sound in the background of Windows """
        return playsound(
            self.get_true_filename(f"{self.s_folder}/{filename}"),
            block=False
        )

    def handle_keys(self, key_code: int):
        """ Handle each key with their own events, as well as ignoring some keys """
        if key_code in self.ignore_keys:
            return None

        if key_code in [8, 46]:  # Backspace / Delete
            self.play("key-delete.mp3")
        elif key_code == 20:  # Caps key
            self.play("key-caps.mp3")
        elif key_code == 13:  # Enter key
            self.play("key-confirm.mp3")
        elif key_code in [37, 38, 39, 40]:
            self.play("key-movement.mp3")
        else:
            self.play(f"key-press-{random.randint(1, 4)}.mp3")

    def handle_events(self, args):
        """ Start listening to all key presses done on Windows """
        if isinstance(args, KeyboardEvent):
            if args.event_type == "key down":
                self.handle_keys(args.key_code)
                print(f"Key -> {args.current_key} | ASCII: {args.key_code}")

    def hook_handler(self):
        """ Hook script to Windows keyboard event """
        hk = Hook()
        hk.handler = self.handle_events
        hk.hook()


if __name__ == '__main__':
    OsuKeyboard()
