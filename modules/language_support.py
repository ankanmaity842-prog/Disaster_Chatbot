def translate_input(text, target_lang):
    """
    Translate user input to English for processing
    Note: This is a simple keyword-based translation
    For production, consider using Google Translate API or similar
    """
    
    # Dictionary for common disaster-related terms
    translations = {
        'hi': {  # Hindi
            'भूकंप': 'earthquake',
            'बाढ़': 'flood', 
            'आग': 'fire',
            'चक्रवात': 'cyclone',
            'मदद': 'help',
            'सुरक्षा': 'safety',
            'क्या करें': 'what to do',
            'कैसे': 'how',
            'आपातकाल': 'emergency',
            'खतरा': 'danger',
            'बचाव': 'rescue',
            'तैयारी': 'preparation'
        },
        'bn': {  # Bengali
            'ভূমিকম্প': 'earthquake',
            'বন্যা': 'flood',
            'অগ্নি': 'fire', 
            'আগুন': 'fire',
            'ঘূর্ণিঝড়': 'cyclone',
            'সাহায্য': 'help',
            'নিরাপত্তা': 'safety',
            'কি করব': 'what to do',
            'কিভাবে': 'how',
            'জরুরী': 'emergency',
            'বিপদ': 'danger',
            'উদ্ধার': 'rescue',
            'প্রস্তুতি': 'preparation'
        },
        'ta': {  # Tamil
            'நிலநடுக்கம்': 'earthquake',
            'வெள்ளம்': 'flood',
            'தீ': 'fire',
            'சூறாவளி': 'cyclone',
            'உதவி': 'help',
            'பாதுகாப்பு': 'safety',
            'என்ன செய்வது': 'what to do',
            'எப்படி': 'how',
            'அவசரநிலை': 'emergency'
        },
        'te': {  # Telugu
            'భూకంపనలు': 'earthquake',
            'వరదలు': 'flood',
            'అగ్ని': 'fire',
            'తుఫాను': 'cyclone',
            'సహాయం': 'help',
            'భద్రత': 'safety',
            'ఏమి చేయాలి': 'what to do',
            'ఎలా': 'how',
            'అత్యవసర': 'emergency'
        },
        'mr': {  # Marathi
            'भूकंप': 'earthquake',
            'पूर': 'flood',
            'आग': 'fire',
            'चक्रीवादळ': 'cyclone',
            'मदत': 'help',
            'सुरक्षा': 'safety',
            'काय करावे': 'what to do',
            'कसे': 'how',
            'आपत्कालीन': 'emergency'
        },
        'gu': {  # Gujarati
            'ધરતીકંપ': 'earthquake',
            'પૂર': 'flood',
            'આગ': 'fire',
            'ચક્રવાત': 'cyclone',
            'મદદ': 'help',
            'સુરક્ષા': 'safety',
            'શું કરવું': 'what to do',
            'કેવી રીતે': 'how',
            'કટોકટી': 'emergency'
        }
    }
    
    if target_lang == 'en' or target_lang not in translations:
        return text  # Return as-is if English or unsupported language
    
    # Simple word-by-word translation
    words = text.split()
    translated_words = []
    
    for word in words:
        if word in translations[target_lang]:
            translated_words.append(translations[target_lang][word])
        else:
            translated_words.append(word)  # Keep original if no translation found
    
    return ' '.join(translated_words)


def translate_output(text, target_lang):
    """
    Translate output text to target language
    This is a simplified version - in production use proper translation API
    """
    
    if target_lang == 'en':
        return text
    
    # Basic translations for common response patterns
    translations = {
        'hi': {
            'EARTHQUAKE SAFETY': 'भूकंप सुरक्षा',
            'FLOOD SAFETY': 'बाढ़ सुरक्षा', 
            'FIRE SAFETY': 'आग की सुरक्षा',
            'CYCLONE SAFETY': 'चक्रवात सुरक्षा',
            'Drop, Cover, and Hold On immediately': 'तुरंत झुकें, छुपें और पकड़ें',
            'Move to higher ground immediately': 'तुरंत ऊंची जगह पर चले जाएं',
            'Call emergency services immediately': 'तुरंत आपातकालीन सेवाओं को कॉल करें',
            'Stay indoors and away from windows': 'घर के अंदर रहें और खिड़कियों से दूर रहें',
            'Hello! I am DisastraBot': 'नमस्ते! मैं DisastraBot हूं',
            'Ask me about': 'मुझसे पूछें',
            'For immediate emergencies, call': 'तत्काल आपातकाल के लिए कॉल करें',
            'earthquake': 'भूकंप',
            'flood': 'बाढ़',
            'fire': 'आग',
            'cyclone': 'चक्रवात',
            'safety': 'सुरक्षा'
        },
        'bn': {
            'EARTHQUAKE SAFETY': 'ভূমিকম্প সুরক্ষা',
            'FLOOD SAFETY': 'বন্যা সুরক্ষা',
            'FIRE SAFETY': 'অগ্নি সুরক্ষা',
            'CYCLONE SAFETY': 'ঘূর্ণিঝড় সুরক্ষা',
            'Drop, Cover, and Hold On immediately': 'অবিলম্বে নিচে নেমে আশ্রয় নিন',
            'Move to higher ground immediately': 'অবিলম্বে উঁচু জমিতে চলে যান',
            'Call emergency services immediately': 'অবিলম্বে জরুরী পরিষেবায় কল করুন',
            'Stay indoors and away from windows': 'ঘরের ভিতরে থাকুন এবং জানালা থেকে দূরে থাকুন',
            'Hello! I am DisastraBot': 'হ্যালো! আমি DisastraBot',
            'Ask me about': 'আমাকে জিজ্ঞাসা করুন',
            'For immediate emergencies, call': 'তাৎক্ষণিক জরুরী অবস্থার জন্য কল করুন',
            'earthquake': 'ভূমিকম্প',
            'flood': 'বন্যা',
            'fire': 'অগ্নি',
            'cyclone': 'ঘূর্ণিঝড়',
            'safety': 'নিরাপত্তা'
        }
    }
    
    if target_lang not in translations:
        return text
    
    # Simple find and replace translation
    translated_text = text
    for english_text, translated in translations[target_lang].items():
        translated_text = translated_text.replace(english_text, translated)
    
    return translated_text