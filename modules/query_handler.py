from .language_support import translate_input, translate_output

def handle_query(user_input, user_lang='en'):
    """
    Handle user queries and return appropriate disaster response
    """
    # First translate input to English if needed
    translated_input = translate_input(user_input, user_lang)
    user_input_processed = translated_input.lower()
    
    # Disaster response database
    responses = {
        'earthquake': {
            'en': "🚨 EARTHQUAKE SAFETY:\n• Drop, Cover, and Hold On immediately\n• Stay away from windows and heavy objects\n• If outdoors, move away from buildings\n• Check for injuries after shaking stops\n• Be prepared for aftershocks",
            'hi': "🚨 भूकंप सुरक्षा:\n• तुरंत झुकें, छुपें और पकड़ें\n• खिड़कियों और भारी वस्तुओं से दूर रहें\n• यदि बाहर हैं तो भवनों से दूर चले जाएं\n• हिलना बंद होने के बाद चोटों की जांच करें\n• बाद के झटकों के लिए तैयार रहें",
            'bn': "🚨 ভূমিকম্প সুরক্ষা:\n• অবিলম্বে নিচে নেমে আশ্রয় নিন\n• জানালা এবং ভারী বস্তু থেকে দূরে থাকুন\n• বাইরে থাকলে ভবন থেকে দূরে সরে যান\n• কম্পন বন্ধ হওয়ার পর আঘাতের জন্য পরীক্ষা করুন\n• পরবর্তী ঝাঁকুনির জন্য প্রস্তুত থাকুন"
        },
        'flood': {
            'en': "🌊 FLOOD SAFETY:\n• Move to higher ground immediately\n• Avoid walking/driving through flood water\n• Stay away from downed power lines\n• Listen to emergency broadcasts\n• Have emergency supplies ready",
            'hi': "🌊 बाढ़ सुरक्षा:\n• तुरंत ऊंची जगह पर चले जाएं\n• बाढ़ के पानी में चलने/गाड़ी चलाने से बचें\n• गिरी हुई बिजली की तारों से दूर रहें\n• आपातकालीन प्रसारण सुनें\n• आपातकालीन आपूर्ति तैयार रखें",
            'bn': "🌊 বন্যা সুরক্ষা:\n• অবিলম্বে উঁচু জমিতে চলে যান\n• বন্যার পানিতে হাঁটা/গাড়ি চালানো এড়িয়ে চলুন\n• পড়ে যাওয়া বিদ্যুৎ লাইন থেকে দূরে থাকুন\n• জরুরী সম্প্রচার শুনুন\n• জরুরী সরবরাহ প্রস্তুত রাখুন"
        },
        'fire': {
            'en': "🔥 FIRE SAFETY:\n• Call emergency services immediately (112)\n• Get low and crawl under smoke\n• Feel doors before opening them\n• Have an escape plan and meeting point\n• Never use elevators during a fire",
            'hi': "🔥 आग की सुरक्षा:\n• तुरंत आपातकालीन सेवाओं को कॉल करें (112)\n• नीचे झुकें और धुएं के नीचे रेंगें\n• दरवाजे खोलने से पहले उन्हें छूकर देखें\n• बचने की योजना और मिलने का स्थान रखें\n• आग के दौरान लिफ्ट का उपयोग न करें",
            'bn': "🔥 অগ্নি সুরক্ষা:\n• অবিলম্বে জরুরী পরিষেবায় কল করুন (112)\n• নিচে নেমে ধোঁয়ার নিচে হামাগুড়ি দিন\n• দরজা খোলার আগে স্পর্শ করে দেখুন\n• পালানোর পরিকল্পনা এবং মিলনস্থল রাখুন\n• আগুনের সময় লিফট ব্যবহার করবেন না"
        },
        'cyclone': {
            'en': "🌪️ CYCLONE SAFETY:\n• Stay indoors and away from windows\n• Stock up on emergency supplies\n• Charge all electronic devices\n• Listen to weather updates regularly\n• Secure outdoor items",
            'hi': "🌪️ चक्रवात सुरक्षा:\n• घर के अंदर रहें और खिड़कियों से दूर रहें\n• आपातकालीन आपूर्ति का भंडार करें\n• सभी इलेक्ट्रॉनिक उपकरणों को चार्ज करें\n• नियमित रूप से मौसम अपडेट सुनें\n• बाहरी वस्तुओं को सुरक्षित करें",
            'bn': "🌪️ ঘূর্ণিঝড় সুরক্ষা:\n• ঘরের ভিতরে থাকুন এবং জানালা থেকে দূরে থাকুন\n• জরুরী সরবরাহের মজুদ করুন\n• সমস্ত ইলেকট্রনিক ডিভাইস চার্জ করুন\n• নিয়মিত আবহাওয়া আপডেট শুনুন\n• বাইরের জিনিসপত্র সুরক্ষিত করুন"
        }
    }
    
    # Check for specific disaster types
    for disaster_type, disaster_responses in responses.items():
        if disaster_type in user_input_processed or any(keyword in user_input.lower() for keyword in [
            'भूकंप', 'ভূমিকম্প', 'நிலநடுக்கம்' if disaster_type == 'earthquake' else '',
            'बाढ़', 'বন্যা', 'வெள்ளம்' if disaster_type == 'flood' else '',
            'आग', 'অগ্নি', 'தீ' if disaster_type == 'fire' else '',
            'चक्रवात', 'ঘূর্ণিঝড়', 'சூறாவளி' if disaster_type == 'cyclone' else ''
        ]):
            return disaster_responses.get(user_lang, disaster_responses['en'])
    
    # General help responses
    general_responses = {
        'en': "🤖 DisastraBot Help:\n• Ask me about: earthquake, flood, fire, cyclone safety\n• I support multiple languages\n• For immediate emergencies, call 112\n• Type specific disaster names for detailed safety tips",
        'hi': "🤖 DisastraBot सहायता:\n• मुझसे पूछें: भूकंप, बाढ़, आग, चक्रवात सुरक्षा\n• मैं कई भाषाओं का समर्थन करता हूं\n• तत्काल आपातकाल के लिए 112 पर कॉल करें\n• विस्तृत सुरक्षा सुझावों के लिए विशिष्ट आपदा नाम टाइप करें",
        'bn': "🤖 DisastraBot সহায়তা:\n• আমাকে জিজ্ঞাসা করুন: ভূমিকম্প, বন্যা, অগ্নি, ঘূর্ণিঝড় সুরক্ষা\n• আমি একাধিক ভাষা সমর্থন করি\n• তাৎক্ষণিক জরুরী অবস্থার জন্য 112 কল করুন\n• বিস্তারিত নিরাপত্তা টিপসের জন্য নির্দিষ্ট দুর্যোগের নাম টাইপ করুন"
    }
    
    # Check for help keywords
    help_keywords = ['help', 'मदद', 'সাহায্য', 'safety', 'सुरक्षा', 'নিরাপত্তা', 'what', 'कैसे', 'কিভাবে']
    if any(keyword in user_input_processed for keyword in help_keywords):
        response = general_responses.get('en', general_responses['en'])
        return translate_output(response, user_lang)
    
    # Default response
    default_response = "Hello! I'm DisastraBot. Ask me about earthquake, flood, fire, or cyclone safety. Type 'help' for more options."
    return translate_output(default_response, user_lang)