"""Test script for anuvaad-rev package"""

import time
from anuvaad_rev import IndicTranslator

def test_language_detection():
    """Test language detection functionality"""
    print("\nTesting Language Detection...")
    print("=" * 50)
    
    translator = IndicTranslator()
    test_cases = {
        "Hello, how are you?": "en",
        "नमस्ते, कैसे हैं आप?": "hi",
        "வணக்கம், எப்படி இருக்கிறீர்கள்?": "ta",
        "ನಮಸ್ಕಾರ, ಹೇಗಿದ್ದೀರಾ?": "kn",
        "హలో, ఎలా ఉన్నారు?": "te",
        "നമസ്കാരം, സുഖമാണോ?": "ml"
    }
    
    for text, expected in test_cases.items():
        detected = translator.detect_language(text)
        status = "✓" if detected == expected else "✗"
        print(f"{status} Detected '{detected}' for text: {text}")
        
        # Get confidence scores
        scores = translator.detect_language_confidence(text)
        print(f"  Confidence scores:")
        for lang, score in scores:
            print(f"  - {lang}: {score:.2%}")

def test_language_utils():
    """Test language utility functions"""
    print("\nTesting Language Utilities...")
    print("=" * 50)
    
    translator = IndicTranslator()
    
    # Test getting language name
    print("Testing get_language_name:")
    test_codes = ["hi", "ta", "kn", "te", "ml"]
    for code in test_codes:
        name = translator.get_language_name(code)
        print(f"✓ {code} -> {name}")
    
    # Test getting language code
    print("\nTesting get_language_code:")
    test_names = ["Hindi", "Tamil", "Kannada", "Telugu", "Malayalam"]
    for name in test_names:
        code = translator.get_language_code(name)
        print(f"✓ {name} -> {code}")
    
    # Test supported languages
    print("\nSupported Languages:")
    langs = translator.get_supported_languages()
    print(f"Total languages: {len(langs)}")
    for code, name in sorted(langs.items()):
        print(f"- {name} ({code})")

def test_translation():
    """Test translation functionality"""
    print("\nTesting Translation...")
    print("=" * 50)
    
    translator = IndicTranslator()
    
    # Test text in different languages
    test_cases = [
        {
            "text": "Welcome to India!",
            "source": "en",
            "targets": ["hi", "ta", "kn"]
        },
        {
            "text": "नमस्ते दुनिया!",
            "source": "hi",
            "targets": ["en", "ta", "ml"]
        },
        {
            "text": "வணக்கம் உலகம்!",
            "source": "ta",
            "targets": ["en", "hi", "te"]
        }
    ]
    
    for case in test_cases:
        print(f"\nOriginal [{case['source']}]: {case['text']}")
        for target in case['targets']:
            try:
                # Add delay to avoid rate limits
                time.sleep(2)
                translation = translator.translate(case['text'], target)
                if translation:
                    target_name = translator.get_language_name(target)
                    print(f"✓ {target_name}: {translation}")
                else:
                    print(f"✗ {target}: Translation failed")
            except Exception as e:
                print(f"✗ {target}: Error - {str(e)}")

def test_rate_limiting():
    """Test rate limit handling"""
    print("\nTesting Rate Limit Handling...")
    print("=" * 50)
    
    translator = IndicTranslator()
    text = "Hello, how are you?"
    
    print("Making rapid requests to test rate limiting...")
    for i in range(5):
        try:
            translation = translator.translate(text, "hi")
            print(f"Request {i+1}: Success - {translation}")
        except Exception as e:
            print(f"Request {i+1}: Error - {str(e)}")
        time.sleep(0.5)  # Small delay to not overwhelm

def main():
    """Run all tests"""
    print("Starting Anuvaad-Rev Tests...")
    print("\nNote: Some tests may fail due to API rate limits.")
    print("In production, use appropriate delays between requests.")
    
    # Run tests
    test_language_detection()
    test_language_utils()
    test_translation()
    test_rate_limiting()
    
    print("\nTests completed!")

if __name__ == "__main__":
    main()