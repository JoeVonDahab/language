# Egyptian Hieroglyph Converter 𓀀

A Python tool that converts English text to Egyptian hieroglyphs with pronunciation guides!

## Features

- **Text to Hieroglyphs**: Convert any English text to authentic Unicode Egyptian hieroglyphs
- **Pronunciation Guide**: Get phonetic pronunciation for the converted text
- **Interactive Mode**: Use the CLI for interactive conversions
- **Command Line Mode**: Convert text directly from command line arguments

## Installation

No dependencies required! Just Python 3.6+

```bash
# Clone the repository
git clone <repository-url>
cd language

# Make the script executable (optional)
chmod +x hieroglyph_converter.py
```

## Usage

### Interactive Mode

Run the script without arguments to enter interactive mode:

```bash
python3 hieroglyph_converter.py
```

Then type any English text to convert:

```
Enter text to convert: hello world
```

### Command Line Mode

Pass text as command line arguments:

```bash
python3 hieroglyph_converter.py hello world
```

Or with quotes for longer text:

```bash
python3 hieroglyph_converter.py "Egypt is amazing"
```

## Examples

### Example 1: Simple Word

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
  𓀀𓂣𓃭𓃭𓃾

Pronunciation Guide:
  huh-eh-l-l-oh

============================================================
```

### Example 2: Sentence

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

============================================================
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

## Limitations

- This is a simplified phonetic conversion, not a true linguistic translation
- Ancient Egyptian hieroglyphs represented consonants primarily; vowels were often implied
- The pronunciation guide is approximated for English speakers
- Not all punctuation is supported

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
