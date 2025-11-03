# Egyptian Hieroglyph Converter 𓀀 🔊

A Python tool that converts English text to Egyptian hieroglyphs with **REAL AUDIO PRONUNCIATION**!

## Features

- **Text to Hieroglyphs**: Convert any English text to authentic Unicode Egyptian hieroglyphs
- **🔊 Audio Pronunciation**: Hear the pronunciation spoken aloud using text-to-speech
- **Pronunciation Guide**: Get written phonetic pronunciation for the converted text
- **Interactive Mode**: Use the CLI for interactive conversions with audio
- **Command Line Mode**: Convert text directly from command line arguments
- **Multiple TTS Options**: Supports pyttsx3, gTTS, and system TTS (espeak, say, PowerShell)

## Installation

### Basic Installation (Python 3.6+)

```bash
# Clone the repository
git clone https://github.com/JoeVonDahab/language.git
cd language

# Make the script executable (optional)
chmod +x hieroglyph_converter.py
```

### Audio Pronunciation Setup

To enable **audio pronunciation**, install one of these TTS options:

#### Option 1: pyttsx3 (Offline, Recommended)

```bash
# Install pyttsx3
pip install pyttsx3

# Linux: Also install espeak
sudo apt-get install espeak espeak-data libespeak-dev

# macOS: Built-in 'say' command works automatically
# Windows: Built-in PowerShell TTS works automatically
```

#### Option 2: gTTS (Google TTS, Requires Internet)

```bash
# Install gTTS
pip install gTTS

# Linux: Also install an audio player
sudo apt-get install mpg123

# macOS: Built-in 'afplay' works automatically
# Windows: Built-in media player works automatically
```

#### Option 3: System TTS (Fallback)

- **Linux**: Install `espeak` (sudo apt-get install espeak)
- **macOS**: Built-in `say` command (no installation needed)
- **Windows**: Built-in PowerShell TTS (no installation needed)

#### Quick Install All Dependencies

```bash
# Install all Python dependencies
pip install -r requirements.txt

# Linux only
sudo apt-get install espeak espeak-data mpg123
```

## Usage

### Interactive Mode with Audio 🔊

Run the script without arguments to enter interactive mode with audio pronunciation:

```bash
python3 hieroglyph_converter.py
```

Then type any English text to convert and hear it pronounced:

```
Enter text to convert: hello world
```

**Interactive Mode Commands:**
- Type any text to convert and hear pronunciation
- Type `silent` to toggle audio on/off
- Type `quit` or `exit` to stop

### Command Line Mode

Pass text as command line arguments:

```bash
# With audio pronunciation
python3 hieroglyph_converter.py hello world

# Without audio (silent mode)
python3 hieroglyph_converter.py "Egypt is amazing" --silent
python3 hieroglyph_converter.py "thank you" --no-audio
```

## Examples

### Example 1: Simple Word with Audio

```bash
$ python3 hieroglyph_converter.py hello
```

Output:
```
============================================================
EGYPTIAN HIEROGLYPH CONVERTER
============================================================

Original Text:
  hello

Hieroglyphs:
  𓅖𓀂ll𓅓

Pronunciation Guide:
  huh-eh-l-l-oh

🔊 Playing pronunciation...
(Audio: "huh eh l l oh" is spoken aloud)

============================================================
```

### Example 2: Sentence with Audio

```bash
$ python3 hieroglyph_converter.py "Welcome to Egypt"
```

Output:
```
============================================================
EGYPTIAN HIEROGLYPH CONVERTER
============================================================

Original Text:
  Welcome to Egypt

Hieroglyphs:
  𓅱𓂣𓃭𓀀𓃾𓅓𓂣  𓏏𓃾  𓂣𓎼𓇌𓊪𓏏

Pronunciation Guide:
  wah-eh-l-kuh-oh-muh-eh tuh eh-guh-yee-puh-tuh

🔊 Playing pronunciation...
(Audio: pronunciation is spoken aloud)

============================================================
```

### Example 3: Interactive Mode

```bash
$ python3 hieroglyph_converter.py

============================================================
EGYPTIAN HIEROGLYPH CONVERTER WITH AUDIO 🔊
============================================================

Convert English text to Egyptian hieroglyphs!
Commands:
  - Type any text to convert and hear pronunciation
  - Type 'silent' to toggle audio on/off
  - Type 'quit' or 'exit' to stop

Enter text to convert: thank you
(Displays hieroglyphs and plays audio pronunciation)

Enter text to convert: silent
🔊 Audio pronunciation disabled

Enter text to convert: hello
(Displays hieroglyphs without audio)
```

## How It Works

The converter uses a phonetic mapping system that translates English letters to their closest Egyptian hieroglyph equivalents:

- **Vowels**: Mapped to Egyptian semi-vowels and vowel indicators
- **Consonants**: Mapped to phonetically similar hieroglyphic symbols
- **Pronunciation**: Generates a phonetic guide showing how to pronounce the hieroglyphs

### Hieroglyph Mapping Examples

| Letter | Hieroglyph | Symbol Description |
|--------|------------|-------------------|
| a | 𓀀 | Vulture (glottal stop) |
| i | 𓂣 | Reed leaf |
| m | 𓃾 | Forearm |
| n | 𓃻 | Water |
| r | 𓂋 | Mouth |
| s | 𓊃 | Folded cloth |
| t | 𓏏 | Bread loaf |

## Technical Details

- Uses Unicode Egyptian Hieroglyphs block (U+13000–U+1342F)
- Phonetic-based conversion system
- Handles common English digraphs (th, ch, sh, ph)
- Case-insensitive conversion
- **Multiple TTS backends**:
  - pyttsx3 (offline, cross-platform)
  - Google TTS (online, high quality)
  - System TTS fallbacks (espeak/say/PowerShell)
- Automatic TTS backend selection
- Cross-platform audio support (Linux, macOS, Windows)

## Audio Troubleshooting

If audio doesn't work:

1. **Install dependencies**: Run `pip install pyttsx3` or `pip install gTTS`
2. **Linux users**: Install espeak with `sudo apt-get install espeak`
3. **Check system audio**: Make sure your speakers/headphones are working
4. **Use silent mode**: Add `--silent` flag to skip audio

The tool will show helpful error messages if audio setup is needed.

## Limitations

- This is a simplified phonetic conversion, not a true linguistic translation
- Ancient Egyptian hieroglyphs represented consonants primarily; vowels were often implied
- The pronunciation guide is approximated for English speakers
- Not all punctuation is supported
- Audio pronunciation is phonetic, not authentic ancient Egyptian

## Contributing

Feel free to improve the hieroglyph mappings or add new features!

## License

Open source - feel free to use and modify!

## Fun Facts

- Egyptian hieroglyphs were used for over 3,000 years
- The word "hieroglyph" comes from Greek meaning "sacred carvings"
- There are over 1,000 distinct hieroglyphic characters
- Hieroglyphs can be read left-to-right, right-to-left, or top-to-bottom!

---

Made with ❤️ for Ancient Egypt enthusiasts!

𓋹𓈖𓆑𓂋𓊪 (snfrw - "May you be beautiful/happy")
