"""Basic usage example of anuvaad-rev package"""

from anuvaad_rev import IndicTranslator
import time

def main():
    # Create translator instance with custom session refresh interval (1 hour)
    translator = IndicTranslator(max_retries=3, session_refresh_interval=3600)
    
    # Example text to translate
    texts = [
        "Welcome to India! This is a beautiful country.",
        "The weather is nice today.",
        "I love Indian cuisine.",
        "Technology is advancing rapidly.",
        "Education is very important."
    ]
    
    # Print available languages
    print("Available Languages:")
    print("------------------")
    for code, name in translator.get_supported_languages().items():
        print(f"- {name} ({code})")
    
    # Example translations to multiple languages
    target_languages = ["hi", "ta", "kn", "te", "ml"]
    
    print("\nTranslating multiple texts to multiple languages:")
    print("=" * 50)
    
    for text in texts:
        print(f"\nOriginal (English): {text}")
        for lang in target_languages:
            try:
                # Small delay to avoid overwhelming the API
                time.sleep(1)
                translation = translator.translate(text, lang)
                if translation:
                    lang_name = translator.get_supported_languages()[lang]
                    print(f"{lang_name}: {translation}")
            except Exception as e:
                print(f"Error translating to {lang}: {str(e)}")
                
        print("-" * 50)
            
if __name__ == "__main__":
    main()