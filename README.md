# anuvaad-rev

A Python package for Indian language translation using [AI4Bharat's IndicTrans2](https://ai4bharat.iitm.ac.in/) API service. This package provides an easy-to-use interface for translating text between English and various Indian languages, with automatic language detection.

## Acknowledgment

This package uses the IndicTrans2 translation service provided by AI4Bharat. All translation capabilities are powered by AI4Bharat's API. Visit [AI4Bharat's website](https://ai4bharat.iitm.ac.in/) for more information about their services.

## Features

- Support for 23 Indian languages
- Automatic language detection
- Language information utilities
- User agent rotation to avoid rate limits
- Automatic session refresh
- Retry mechanism for failed requests
- Error handling and input validation
- Easy to integrate into existing projects

## Installation

```bash
pip install anuvaad-rev
```

## Quick Start

```python
from anuvaad_rev import IndicTranslator

# Create translator instance
translator = IndicTranslator()

# Auto-detect language and translate
text = "नमस्ते, कैसे हैं आप?"
translation = translator.translate(text, target_lang="en")
print(translation)  # Output: Hello, how are you?

# Get language information
languages = translator.get_supported_languages()
print(languages)
```

## Language Detection and Information

```python
# Detect language
text = "வணக்கம், எப்படி இருக்கிறீர்கள்?"
detected = translator.detect_language(text)
print(detected)  # Output: ta

# Get language name
lang_name = translator.get_language_name("ta")
print(lang_name)  # Output: Tamil

# Get confidence scores
confidence = translator.detect_language_confidence(text)
for lang, score in confidence:
    print(f"{lang}: {score:.2%}")

# Get language code from name
code = translator.get_language_code("Hindi")
print(code)  # Output: hi

# List all supported languages
codes = translator.get_supported_language_codes()
names = translator.get_supported_language_names()
```

## Advanced Translation

```python
# Create translator with custom settings
translator = IndicTranslator(
    max_retries=3,              # Number of retries for failed requests
    session_refresh_interval=3600  # Refresh session every hour
)

# Batch translation with auto-detection
texts = [
    "Hello world!",
    "नमस्ते दुनिया!",
    "வணக்கம் உலகம்!"
]

for text in texts:
    # Source language will be auto-detected
    translation = translator.translate(text, target_lang="hi")
    print(f"Original: {text}")
    print(f"Hindi: {translation}\n")
```

## Supported Languages

| Language | Code | Language | Code |
|----------|------|----------|------|
| Assamese | as | Malayalam | ml |
| Bengali | bn | Manipuri | mni |
| Bodo | brx | Marathi | mr |
| Dogri | doi | Nepali | ne |
| English | en | Odia | or |
| Gujarati | gu | Punjabi | pa |
| Hindi | hi | Sanskrit | sa |
| Kannada | kn | Santali | sat |
| Kashmiri | ks | Sindhi | sd |
| Konkani | kok | Tamil | ta |
| Maithili | mai | Telugu | te |
| | | Urdu | ur |

## API Reference

### IndicTranslator

```python
class IndicTranslator:
    def translate(self, text, target_lang, source_lang=None):
        """
        Translate text with optional auto-detection
        
        Args:
            text: Text to translate
            target_lang: Target language code
            source_lang: Source language code (if None, will be auto-detected)
            
        Returns:
            Translated text if successful, None otherwise
        """
    
    def detect_language(self, text):
        """
        Detect the language of input text
        
        Returns:
            Detected language code
        """
    
    def detect_language_confidence(self, text):
        """
        Detect language with confidence scores
        
        Returns:
            List of (language_code, confidence_score) tuples
        """
    
    def get_language_name(self, lang_code):
        """Get language name from code"""
    
    def get_language_code(self, language_name):
        """Get language code from name"""
    
    def get_supported_languages(self):
        """Get dictionary of supported languages"""
    
    def get_supported_language_codes(self):
        """Get list of supported language codes"""
    
    def get_supported_language_names(self):
        """Get list of supported language names"""
```

## Examples

The package includes several example scripts demonstrating various features:
- Basic translation usage
- Batch translation with rate limit handling
- Language detection and information features

## License

This package is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This is an unofficial package that uses AI4Bharat's IndicTrans2 API service. Users must ensure their usage complies with AI4Bharat's terms of service and guidelines. This package is not affiliated with or endorsed by AI4Bharat.

## Credits

Translation service provided by [AI4Bharat](https://ai4bharat.iitm.ac.in/).