import random

responses = {
    "hello": ["Hello! How are you feeling today?", "Hi there. What would you like to talk about?", "Hello! Tell me what is on your mind."],
    "hi": ["Hello! How are you feeling today?", "Hi there. What would you like to talk about?", "Hello! Tell me what is on your mind."],
    "hey": ["Hello! How are you feeling today?", "Hi there. What would you like to talk about?", "Hello! Tell me what is on your mind."],

    "sad": ["Why do you feel that way?", "How long have you been feeling like this?", "Do you think something caused that feeling?"],
    "angry": ["Why do you feel that way?", "How long have you been feeling like this?", "Do you think something caused that feeling?"],
    "happy": ["What makes you feel happy?", "How long have you felt like this?", "Tell me more about why you feel this way."],

    "mother": ["Tell me more about your family.", "How is your relationship with your family?", "Does your family affect how you feel?"],
    "father": ["Tell me more about your family.", "How is your relationship with your family?", "Does your family affect how you feel?"],
    "family": ["Tell me more about your family.", "How is your relationship with your family?", "Does your family affect how you feel?"],

    "school": ["How do you feel about school right now?", "What do you think about your teachers?", "Do exams make you feel stressed?"],
    "teacher": ["How do you feel about school right now?", "What do you think about your teachers?", "Do exams make you feel stressed?"],
    "exam": ["How do you feel about exams?", "Do exams stress you?", "How do you prepare for exams?"]
}

fallback = [
    "Can you tell me more about that?",
    "Why do you say that?",
    "How does that make you feel?"
]

while True:
    user_input = input("You: ").lower()
    found = False

    for keyword in responses:
        if keyword in user_input:
            print("Bot:", random.choice(responses[keyword]))
            found = True
            break

    if not found:
        print("Bot:", random.choice(fallback))