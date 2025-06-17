"""Advanced batch translation example with rate limit handling"""

from anuvaad_rev import IndicTranslator
import time
import json
from typing import List, Dict

def load_sample_data() -> List[Dict[str, str]]:
    """Load sample data for batch translation"""
    return [
        {
            "id": "001",
            "text": "Digital India is transforming the country through technology.",
            "target_languages": ["hi", "ta", "bn"]
        },
        {
            "id": "002",
            "text": "Indian culture is known for its rich diversity.",
            "target_languages": ["kn", "ml", "te"]
        },
        {
            "id": "003",
            "text": "Education empowers the future generation.",
            "target_languages": ["mr", "gu", "pa"]
        }
    ]

def batch_translate(translator: IndicTranslator, data: List[Dict[str, str]]) -> Dict[str, Dict[str, str]]:
    """
    Perform batch translation with rate limit handling
    
    Args:
        translator: IndicTranslator instance
        data: List of dictionaries containing text and target languages
        
    Returns:
        Dictionary containing translations for each text ID
    """
    results = {}
    
    for item in data:
        text_id = item["id"]
        text = item["text"]
        target_langs = item["target_languages"]
        
        results[text_id] = {
            "original": text,
            "translations": {}
        }
        
        print(f"\nProcessing Text ID: {text_id}")
        print(f"Original: {text}")
        
        for lang in target_langs:
            try:
                # Add delay to avoid rate limits
                time.sleep(1)
                
                translation = translator.translate(text, lang)
                if translation:
                    lang_name = translator.get_supported_languages()[lang]
                    results[text_id]["translations"][lang_name] = translation
                    print(f"{lang_name}: {translation}")
                    
            except Exception as e:
                print(f"Error translating to {lang}: {str(e)}")
                results[text_id]["translations"][lang] = f"Error: {str(e)}"
                
        print("-" * 50)
    
    return results

def save_results(results: Dict[str, Dict[str, str]], filename: str = "translation_results.json"):
    """Save translation results to JSON file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\nResults saved to {filename}")

def main():
    # Initialize translator with custom settings
    translator = IndicTranslator(
        max_retries=3,
        session_refresh_interval=1800  # Refresh session every 30 minutes
    )
    
    # Load sample data
    data = load_sample_data()
    
    print("Starting batch translation...")
    print("=" * 50)
    
    # Perform batch translation
    results = batch_translate(translator, data)
    
    # Save results
    save_results(results)

if __name__ == "__main__":
    main()