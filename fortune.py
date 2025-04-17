# fortune.py

import random

def get_fortune(mood):
    fortunes = {
        "happy": [
            "🌈 Bright days are ahead, keep shining!",
            "✨ Your joy is contagious, Vaibhav!",
        ],
        "sad": [
            "💖 It's okay to feel down. Better days are coming.",
            "🌧 Even storms pass. You're stronger than you know.",
        ],
        "neutral": [
            "🌟 A surprise is around the corner, stay curious!",
            "💫 Balance brings clarity. Trust yourself.",
        ],
        "stressed": [
            "🧘‍♂ Breathe in peace, breathe out stress.",
            "🌿 Take a break, Indranil. You’ve earned it!",
        ]
    }
    if mood in fortunes:
        return random.choice(fortunes[mood])
    else:
        return "🤔 I can't predict that mood. Try happy, sad, neutral, or stressed."

def main():
    print("🔮 Welcome to Vaibhav Jains's Fortune Teller (21JE1014) 🔮")
    mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").strip().lower()
    print(f"\n✨ Your fortune: {get_fortune(mood)} ✨")

if _name_ == "_main_":
    main()
