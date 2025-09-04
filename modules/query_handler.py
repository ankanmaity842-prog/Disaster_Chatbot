from modules.language_support import translate_input, translate_output
from modules.context_manager import get_context
from modules.student_queries import enrich_student_query
import google.generativeai as genai
from modules.language_support import detect_language, normalize_mixed_input
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key="AIzaSyB-8oD9GZ1Gh88YnwVdkkmqlLn7T9K7xhw")

model = genai.GenerativeModel("gemini-2.5-flash")

def handle_query(user_input, user_lang):
    mixed_input = normalize_mixed_input(user_input)
    detected_lang = detect_language(mixed_input)
    translated_input = translate_input(mixed_input, detected_lang)
    context = get_context(translated_input)
    enriched = enrich_student_query(translated_input)

    prompt = (
        f"{context}\n"
        f"{enriched}\n"
        f"Show respone in one to 3 lines for definition,first aid,kit,regions,global data,place,time like questions.Exclude bullet points for specific question like this .\n"
        f"Respond in 5 to 7 short bullet points as required .Exclude asterics. Use simple, student-friendly language.\n"
        f"Most important point on the first rest others.\n"
        f"Show response only for the disaster related question including earthquake,flood,fir ,cyclone .\n"
        f"Be accurate and specific. Avoid general advice.\n"
        f"Show each points on the next line to previous point.\n"
        f"Respond briefly and precisely. Focus only on what the student needs to know.\n"
        f"Your task is to give a clear, accurate, and student-friendly answer.\n"
        f"Your task is to give response based on answers related to India.\n"
        f"Do not include introductions or conclusions.\n"
        f"User question (mixed language): {user_input}\n"
        f"Answer:"
    )

    try:
        response = model.generate_content(prompt)
        translated_output = translate_output(response.text.strip(), user_lang)
        return translated_output
    except Exception as e:
        return f"⚠️ Unable to process your request: {str(e)}"
