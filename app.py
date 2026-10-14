
import os
import random
import gradio as gr

QUERIES = [
    "How can I manage exam stress?",
    "How should I handle criticism?",
    "How can I build self-confidence?",
    "What can I do when I feel lonely?",
    "How can I stay motivated?",
    "How should I deal with failure?",
    "How can I control my anger?",
    "How can I stop overthinking?",
    "How can I overcome public-speaking fear?",
    "How can I develop a positive mindset?",
    "How can I manage my time better?",
    "How can I build good habits?",
    "How can I handle disappointment?",
    "How can I improve communication?",
    "How can I achieve my goals?",
    "How should I handle peer pressure?",
    "How can I develop discipline?",
    "How can I balance study and personal life?",
    "How can I become more patient?",
    "How can I learn from role models?"
]

RESPONSES = [
    "Divide your syllabus into small tasks, practise regularly, and take breaks.",
    "Learn from constructive feedback without letting hurtful comments define your worth.",
    "Build confidence through small achievements and regular practice.",
    "Contact a trusted friend, family member, teacher, or campus support service.",
    "Choose one achievable task and work on it for 15 minutes.",
    "Treat failure as information, identify a lesson, and try a different approach.",
    "Pause, breathe gently, and respond when you feel calmer.",
    "Write down your concern and identify one practical action you can take.",
    "Prepare three key points and practise speaking aloud.",
    "Acknowledge difficult feelings and look for one realistic next step.",
    "Prioritize three important tasks and schedule focused work with breaks.",
    "Start with one small habit and repeat it consistently.",
    "Give yourself time to process disappointment and focus on what you can change.",
    "Listen carefully, ask questions, and communicate respectfully.",
    "Set a specific goal and divide it into manageable milestones.",
    "Practise saying no politely and seek support from people who respect your choices.",
    "Create a consistent routine and reduce distractions.",
    "Schedule study, sleep, meals, exercise, and leisure.",
    "Slow down your response and focus on what you can control.",
    "Learn from qualities such as courage, kindness, integrity, and perseverance."
]

MOODS = [
    "Happy", "Calm", "Stressed", "Sad",
    "Anxious", "Angry", "Lonely", "Unmotivated"
]

MOOD_RESPONSES = {
    "Happy": "Appreciate your progress and share your positive energy.",
    "Calm": "Reflect on your priorities and choose your next step.",
    "Stressed": "Relax your shoulders, breathe gently, and focus on one task.",
    "Sad": "Be gentle with yourself and talk to someone you trust.",
    "Anxious": "Notice five things you can see around you.",
    "Angry": "Give yourself space before responding.",
    "Lonely": "Contact a trusted friend or consider joining a group activity.",
    "Unmotivated": "Begin with a small task that takes five minutes."
}

AFFIRMATIONS = [
    "I can make progress one step at a time.",
    "My mistakes can help me learn.",
    "I deserve patience and respect.",
    "I can ask for help when I need it.",
    "Small, consistent efforts matter.",
    "I can learn new skills through practice.",
    "I do not need to be perfect to improve.",
    "I can focus on what is within my control."
]

def query_response(query, mood):
    if not query:
        return "Please select a query."
    index = QUERIES.index(query)
    return (
        f"SELECTED QUERY\n\n{query}\n\n"
        f"PERSONALIZED GUIDANCE\n\n{RESPONSES[index]}\n\n"
        f"YOUR MOOD: {mood}\n{MOOD_RESPONSES[mood]}\n\n"
        "Choose one small, practical action to try at your own pace."
    )

def mood_response(mood):
    return f"YOUR MOOD: {mood}\n\n{MOOD_RESPONSES[mood]}"

def affirmation():
    return random.choice(AFFIRMATIONS)

def breathing():
    return (
        "GENTLE BREATHING EXERCISE\n\n"
        "1. Sit comfortably and relax your shoulders.\n"
        "2. Breathe in gently for about 4 seconds.\n"
        "3. Breathe out slowly for about 6 seconds.\n"
        "4. Repeat gently for around one minute.\n\n"
        "Stop if you feel dizzy or uncomfortable."
    )

with gr.Blocks(
    theme=gr.themes.Soft(primary_hue="blue"),
    title="Personalized Wellness Companion"
) as demo:
    gr.Markdown("""
    # Human Role-Model Inspired Personalized Wellness Companion

    Explore practical wellbeing guidance inspired by courage,
    kindness, discipline, resilience, and perseverance.
    """)

    query = gr.Dropdown(
        choices=QUERIES,
        value=QUERIES[0],
        label="Choose one of the 20 queries"
    )

    mood = gr.Dropdown(
        choices=MOODS,
        value="Happy",
        label="How are you feeling?"
    )

    with gr.Row():
        query_btn = gr.Button("Get Query Output", variant="primary")
        mood_btn = gr.Button("Get Mood Support")

    output = gr.Textbox(label="Query Output", lines=10)

    query_btn.click(query_response, [query, mood], output)
    mood_btn.click(mood_response, mood, output)

    gr.Markdown("## Positive Affirmations")
    affirmation_btn = gr.Button("Generate Positive Affirmation")
    affirmation_output = gr.Textbox(label="Your Affirmation")
    affirmation_btn.click(affirmation, [], affirmation_output)

    gr.Markdown("## Breathing Exercise")
    breathing_btn = gr.Button("Show Breathing Guide")
    breathing_output = gr.Textbox(label="Breathing Instructions", lines=5)
    breathing_btn.click(breathing, [], breathing_output)

    gr.Markdown(
        "Educational wellbeing guidance only; not a substitute "
        "for professional mental health support."
    )

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", "10000"))
    )
