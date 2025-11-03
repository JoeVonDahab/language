#!/usr/bin/env python3
"""
Egyptian Hieroglyph Converter
Converts English text to Egyptian hieroglyphs with audio pronunciation
"""

import sys
import os
import platform
import subprocess
import tempfile
from pathlib import Path

# Try to import TTS libraries (optional)
try:
    import pyttsx3
    HAS_PYTTSX3 = True
except ImportError:
    HAS_PYTTSX3 = False

try:
    from gtts import gTTS
    HAS_GTTS = True
except ImportError:
    HAS_GTTS = False

# Unicode Egyptian Hieroglyph mappings
# Using phonetic approach - mapping English sounds to hieroglyphs

HIEROGLYPH_MAP = {
    # Vowels and semi-vowels
    'a': '\U00013000',  # Egyptian hieroglyph A001 (vulture) - glottal stop/a
    'i': '\U00013002',  # Egyptian hieroglyph A003 (reed leaf) - i/y sound
    'y': '\U00013002',  # Same as i
    'e': '\U00013002',  # Map to i sound
    'o': '\U00013153',  # Egyptian hieroglyph D053 (winding wall) - o sound
    'u': '\U00013154',  # Egyptian hieroglyph D054 (quail chick) - w/u sound
    'w': '\U00013154',

    # Consonants
    'b': '\U000130B9',  # Egyptian hieroglyph D058 (foot/leg) - b sound
    'p': '\U00013170',  # Egyptian hieroglyph D170 (stool) - p sound
    'f': '\U00013004',  # Egyptian hieroglyph A006 (horned viper) - f sound
    'm': '\U00013153',  # Egyptian hieroglyph D036 (forearm) - m sound
    'n': '\U00013142',  # Egyptian hieroglyph D021 (water) - n sound
    'r': '\U000130B8',  # Egyptian hieroglyph D021 (mouth) - r sound
    'h': '\U00013156',  # Egyptian hieroglyph D156 (shelter) - h sound
    'k': '\U00013190',  # Egyptian hieroglyph D019 (basket) - k sound
    'g': '\U00013191',  # Egyptian hieroglyph D021 (stand) - g sound
    's': '\U00013008',  # Egyptian hieroglyph D036 (cloth/folded) - s sound
    't': '\U0001317F',  # Egyptian hieroglyph D046 (bread) - t sound
    'd': '\U000130BA',  # Egyptian hieroglyph D046 (hand) - d sound
    'j': '\U00013002',  # Map to y/i sound
    'c': '\U00013190',  # Map to k sound (hard c)
    'q': '\U00013190',  # Map to k sound
    'v': '\U00013004',  # Map to f sound
    'x': '\U00013190',  # Map to ks sound, use k
    'z': '\U00013008',  # Map to s sound

    # Special characters
    ' ': '\U00013190',  # Cartouche/separator
    '.': '𓏤',  # Stroke/separator
    ',': '𓏤',
    '!': '𓀀',  # Seated man (emphasis)
    '?': '𓁶',  # Question/face
}

PRONUNCIATION_MAP = {
    'a': 'ah',
    'e': 'eh',
    'i': 'ee',
    'o': 'oh',
    'u': 'oo',
    'y': 'yee',
    'w': 'wah',
    'b': 'buh',
    'p': 'puh',
    'f': 'fuh',
    'm': 'muh',
    'n': 'nuh',
    'r': 'ruh',
    'h': 'huh',
    'k': 'kuh',
    'g': 'guh',
    's': 'suh',
    't': 'tuh',
    'd': 'duh',
    'j': 'juh',
    'c': 'kuh',
    'q': 'kwuh',
    'v': 'vuh',
    'x': 'ks',
    'z': 'zuh',
    ' ': ' ',
}


class HieroglyphConverter:
    """Convert English text to Egyptian hieroglyphs with audio pronunciation"""

    def __init__(self):
        self.hieroglyph_map = HIEROGLYPH_MAP
        self.pronunciation_map = PRONUNCIATION_MAP
        self.tts_engine = None
        self._init_tts()

    def _init_tts(self):
        """Initialize text-to-speech engine"""
        if HAS_PYTTSX3:
            try:
                self.tts_engine = pyttsx3.init()
                # Set properties for better pronunciation
                self.tts_engine.setProperty('rate', 150)  # Speed
                self.tts_engine.setProperty('volume', 0.9)  # Volume
            except Exception as e:
                print(f"Warning: Could not initialize pyttsx3: {e}")
                self.tts_engine = None

    def _play_audio_system(self, text):
        """Use system TTS commands as fallback"""
        system = platform.system()

        try:
            if system == "Darwin":  # macOS
                subprocess.run(['say', text], check=True)
                return True
            elif system == "Linux":
                # Try espeak
                subprocess.run(['espeak', text], check=True,
                             stderr=subprocess.DEVNULL)
                return True
            elif system == "Windows":
                # Use PowerShell for Windows
                ps_command = f'Add-Type -AssemblyName System.Speech; $speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; $speak.Speak("{text}")'
                subprocess.run(['powershell', '-Command', ps_command], check=True)
                return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False

        return False

    def pronounce(self, text, method='auto'):
        """
        Pronounce text using text-to-speech

        Args:
            text: Text to pronounce
            method: TTS method ('auto', 'pyttsx3', 'gtts', 'system')

        Returns:
            True if pronunciation succeeded, False otherwise
        """
        pronunciation_text = self.text_to_pronunciation(text)

        # Remove hyphens for better TTS pronunciation
        speech_text = pronunciation_text.replace('-', ' ')

        if method == 'auto':
            # Try methods in order of preference
            methods = ['pyttsx3', 'system', 'gtts']
        else:
            methods = [method]

        for m in methods:
            if m == 'pyttsx3' and self.tts_engine:
                try:
                    self.tts_engine.say(speech_text)
                    self.tts_engine.runAndWait()
                    return True
                except Exception as e:
                    print(f"pyttsx3 error: {e}")
                    continue

            elif m == 'system':
                if self._play_audio_system(speech_text):
                    return True

            elif m == 'gtts' and HAS_GTTS:
                try:
                    # Create temporary file for audio
                    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as f:
                        temp_file = f.name

                    tts = gTTS(text=speech_text, lang='en', slow=False)
                    tts.save(temp_file)

                    # Play the audio file
                    system = platform.system()
                    if system == "Darwin":
                        subprocess.run(['afplay', temp_file], check=True)
                    elif system == "Linux":
                        for player in ['mpg123', 'mpg321', 'play', 'ffplay']:
                            try:
                                subprocess.run([player, temp_file], check=True,
                                             stderr=subprocess.DEVNULL)
                                break
                            except (subprocess.CalledProcessError, FileNotFoundError):
                                continue
                    elif system == "Windows":
                        os.startfile(temp_file)

                    # Clean up
                    try:
                        os.unlink(temp_file)
                    except:
                        pass

                    return True
                except Exception as e:
                    print(f"gTTS error: {e}")
                    continue

        return False

    def text_to_hieroglyphs(self, text):
        """Convert English text to hieroglyphs"""
        text = text.lower()
        hieroglyphs = []

        for char in text:
            if char in self.hieroglyph_map:
                hieroglyphs.append(self.hieroglyph_map[char])
            elif char.isspace():
                hieroglyphs.append('  ')  # Word separator
            else:
                # For unknown characters, keep as is
                hieroglyphs.append(char)

        return ''.join(hieroglyphs)

    def text_to_pronunciation(self, text):
        """Convert text to pronunciation guide"""
        text = text.lower()
        pronunciation = []

        i = 0
        while i < len(text):
            char = text[i]

            # Check for common digraphs
            if i < len(text) - 1:
                digraph = text[i:i+2]
                if digraph == 'th':
                    pronunciation.append('thuh')
                    i += 2
                    continue
                elif digraph == 'ch':
                    pronunciation.append('chuh')
                    i += 2
                    continue
                elif digraph == 'sh':
                    pronunciation.append('shuh')
                    i += 2
                    continue
                elif digraph == 'ph':
                    pronunciation.append('fuh')
                    i += 2
                    continue

            if char in self.pronunciation_map:
                pronunciation.append(self.pronunciation_map[char])
            elif char.isspace():
                pronunciation.append(' ')
            else:
                pronunciation.append(char)

            i += 1

        return '-'.join(pronunciation).replace('- -', ' ').replace('--', '-')

    def convert(self, text, show_pronunciation=True):
        """
        Convert text to hieroglyphs with optional pronunciation

        Args:
            text: English text to convert
            show_pronunciation: Whether to show pronunciation guide

        Returns:
            Dictionary with hieroglyphs and pronunciation
        """
        hieroglyphs = self.text_to_hieroglyphs(text)
        pronunciation = self.text_to_pronunciation(text) if show_pronunciation else None

        return {
            'original': text,
            'hieroglyphs': hieroglyphs,
            'pronunciation': pronunciation
        }

    def print_conversion(self, text, play_audio=True):
        """Print formatted conversion output"""
        result = self.convert(text)

        print("\n" + "="*60)
        print("EGYPTIAN HIEROGLYPH CONVERTER")
        print("="*60)
        print(f"\nOriginal Text:")
        print(f"  {result['original']}")
        print(f"\nHieroglyphs:")
        print(f"  {result['hieroglyphs']}")
        print(f"\nPronunciation Guide:")
        print(f"  {result['pronunciation']}")

        if play_audio:
            print(f"\n🔊 Playing pronunciation...")
            success = self.pronounce(text)
            if not success:
                print("⚠️  Audio not available. Install dependencies:")
                print("   pip install pyttsx3")
                print("   or: pip install gTTS")
                print("   or: install espeak (Linux)")

        print("\n" + "="*60 + "\n")


def main():
    """Main CLI interface"""
    converter = HieroglyphConverter()

    # Parse command line arguments
    args = sys.argv[1:]
    silent = '--silent' in args or '--no-audio' in args
    if silent:
        args = [a for a in args if a not in ['--silent', '--no-audio']]

    if args:
        # Convert text from command line arguments
        text = ' '.join(args)
        converter.print_conversion(text, play_audio=not silent)
    else:
        # Interactive mode
        print("\n" + "="*60)
        print("EGYPTIAN HIEROGLYPH CONVERTER WITH AUDIO 🔊")
        print("="*60)
        print("\nConvert English text to Egyptian hieroglyphs!")
        print("Commands:")
        print("  - Type any text to convert and hear pronunciation")
        print("  - Type 'silent' to toggle audio on/off")
        print("  - Type 'quit' or 'exit' to stop\n")

        audio_enabled = True

        while True:
            try:
                text = input("Enter text to convert: ").strip()

                if text.lower() in ['quit', 'exit', 'q']:
                    print("\nGoodbye! 𓋹𓈖𓆑𓂋𓊪\n")
                    break

                if text.lower() == 'silent':
                    audio_enabled = not audio_enabled
                    status = "enabled" if audio_enabled else "disabled"
                    print(f"\n🔊 Audio pronunciation {status}\n")
                    continue

                if not text:
                    continue

                converter.print_conversion(text, play_audio=audio_enabled)

            except KeyboardInterrupt:
                print("\n\nGoodbye! 𓋹𓈖𓆑𓂋𓊪\n")
                break
            except Exception as e:
                print(f"\nError: {e}\n")


if __name__ == "__main__":
    main()
