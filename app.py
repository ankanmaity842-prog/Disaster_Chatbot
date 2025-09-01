from flask import Flask, request, jsonify, render_template
from modules.query_handler import handle_query
import json, os, random

app = Flask(__name__, static_folder='static', template_folder='templates')


dq_path = os.path.join(app.static_folder, 'disaster_queries.json')
with open(dq_path, 'r', encoding='utf-8') as f:
    dq_data = json.load(f)

disaster_queries = dq_data.get("disaster_queries", {})


intro_phrases = [
    "Great! Let’s take the next step together.",
    "Awesome, you’re doing really well.",
    "Want to explore this a bit more?",
    "Can I show you something helpful?",
    "Let me walk you through this.",
    "You’re on the right track. Want to go deeper?",
    "Let’s make this easier together.",
    "I’ve got something useful for you.",
    "Shall we dive into the next part?",
    "Let’s stay safe and smart. Want to hear more?"
]

# Disaster type detection
def detect_disaster_type(message: str):
    msg = message.lower()

    if any(word in msg for word in ["earthquake", "भूकंप", "ভূমিকম্প", "நிலநடுக்கம்", "భూకంపం"]):
        return "earthquake"
    if any(word in msg for word in ["flood", "बाढ़", "বন্যা", "வெள்ளம்", "వరద"]):
        return "flood"
    if any(word in msg for word in ["fire", "आग", "আগুন", "தீ", "అగ్ని"]):
        return "fire"
    if any(word in msg for word in ["cyclone", "चक्रवात", "ঘূর্ণিঝড়", "சுழற்சி புயல்", "చక్రవాతం"]):
        return "cyclone"

    return None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").strip()
    user_lang = request.json.get("language", "en")

    if not user_input:
        return jsonify({"response": "Please enter a message.", "followup": None})

    
    raw_response = handle_query(user_input, user_lang)
    response = raw_response.get("text") if isinstance(raw_response, dict) else str(raw_response)

    
    disaster_type = detect_disaster_type(user_input)
    followup = None
    matched_messages = []

    
    if disaster_type and disaster_queries:
        disaster_data = disaster_queries.get(disaster_type, {})

    
        followups_by_lang = disaster_data.get("followups", {})
        keyword_blocks = followups_by_lang.get("keyword", [])

        
        for block in keyword_blocks:
            for kw in block.get("keywords", []):
                if kw.lower() in user_input.lower():
                    matched_messages.extend(block.get("messages", []))

        if not matched_messages and keyword_blocks:
            fallback_block = random.choice(keyword_blocks)
            matched_messages.extend(random.sample(
                fallback_block.get("messages", []),
                min(3, len(fallback_block.get("messages", [])))
            ))

        if matched_messages:
            intro = random.choice(intro_phrases)
            followup = f"{intro} {random.choice(matched_messages)}"

    # Debug logs
    print("User input:", user_input)
    print("Detected disaster:", disaster_type)
    print("Matched followups:", matched_messages if matched_messages else "None")

    return jsonify({
        "response": response,
        "followup": followup
    })

if __name__ == "__main__":
    app.run(debug=True)