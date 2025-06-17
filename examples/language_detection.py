"""Example demonstrating language detection and language information features"""

from anuvaad_rev import IndicTranslator

def print_language_info(translator):
    """Print information about supported languages"""
    print("Supported Languages:")
    print("=" * 50)
    
    # Get all language information
    codes = translator.get_supported_language_codes()
    names = translator.get_supported_language_names()
    
    print(f"Total supported languages: {len(codes)}")
    print("\nLanguage Code -> Language Name")
    print("-" * 50)
    
    for code in sorted(codes):
        name = translator.get_language_name(code)
        print(f"{code:8} -> {name}")

def demonstrate_language_detection(translator):
    """Demonstrate language detection capabilities"""
    print("\nLanguage Detection:")
    print("=" * 50)
    
    # Test texts in different languages
    test_texts = {
        "Hello, how are you?": "English",
        "नमस्ते, कैसे हैं आप?": "Hindi",
        "வணக்கம், எப்படி இருக்கிறீர்கள்?": "Tamil",
        "ನಮಸ್ಕಾರ, ಹೇಗಿದ್ದೀರಾ?": "Kannada",
        "హలో, ఎలా ఉన్నారు?": "Telugu",
        "നമസ്കാരം, സുഖമാണോ?": "Malayalam"
    }
    
    for text, expected in test_texts.items():
        # Detect language
        detected = translator.detect_language(text)
        name = translator.get_language_name(detected)
        
        print(f"\nText: {text}")
        print(f"Detected: {name} ({detected})")
        print("Confidence scores:")
        
        # Show confidence scores
        confidences = translator.detect_language_confidence(text)
        for lang, score in confidences:
            lang_name = translator.get_language_name(lang) or lang
            print(f"- {lang_name}: {score:.2%}")

def translate_with_auto_detection(translator):
    """Demonstrate translation with automatic language detection"""
    print("\nAuto-detected Translation:")
    print("=" * 50)
    
    # Test translations with auto-detection
    texts = [
        "Hello, how are you?",
        "नमस्ते, कैसे हैं आप?",
        "வணக்கம், எப்படி இருக்கிறீர்கள்?",
        "ನಮಸ್ಕಾರ, ಹೇಗಿದ್ದೀರಾ?"
    ]
    
    target_lang = "hi"  # Translate everything to Hindi
    
    for text in texts:
        print(f"\nOriginal: {text}")
        
        # Detect source language
        detected = translator.detect_language(text)
        detected_name = translator.get_language_name(detected)
        print(f"Detected language: {detected_name} ({detected})")
        
        try:
            # Translate with auto-detected source language
            translation = translator.translate(text, target_lang)
            if translation:
                print(f"Hindi translation: {translation}")
        except Exception as e:
            print(f"Translation error: {str(e)}")

def main():
    # Create translator instance
    translator = IndicTranslator()
    
    # Print information about supported languages
    print_language_info(translator)
    
    # Demonstrate language detection
    demonstrate_language_detection(translator)
    
    # Demonstrate translation with auto-detection
    translate_with_auto_detection(translator)

if __name__ == "__main__":
    main()