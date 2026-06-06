from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import json
import os
import random
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Data files
NOTES_FILE = 'study_notes.json'
PROGRESS_FILE = 'study_progress.json'
QUIZ_FILE = 'quiz_history.json'

def load_data(filename, default):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return default

def save_data(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

# Sample knowledge base for AI responses
KNOWLEDGE_BASE = {
    "math": {
        "quadratic formula": "The quadratic formula is x = (-b ± √(b²-4ac)) / 2a. It helps solve equations in the form ax² + bx + c = 0.",
        "pythagorean theorem": "In a right triangle, a² + b² = c², where c is the hypotenuse.",
        "area of circle": "A = πr², where r is the radius.",
        "fractions": "To add fractions, find a common denominator, then add the numerators.",
        "derivatives": "The derivative of x^n is n*x^(n-1). It measures the rate of change."
    },
    "science": {
        "photosynthesis": "Plants convert sunlight, water, and CO₂ into glucose and oxygen. 6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂",
        "atom": "An atom has protons (+), neutrons (neutral), and electrons (-) in shells.",
        "periodic table": "Elements are arranged by atomic number. Groups have similar properties.",
        "newton's laws": "1st: Objects stay in motion/rest. 2nd: F=ma. 3rd: Action-reaction pairs.",
        "cell": "The cell is the basic unit of life. It has a nucleus, mitochondria, and membrane."
    },
    "english": {
        "metaphor": "A metaphor compares two things without 'like' or 'as'. Example: 'Time is money.'",
        "thesis statement": "A thesis is your main argument, usually one sentence at the end of the introduction.",
        "active voice": "Active voice: 'The dog bit the man.' Passive: 'The man was bitten by the dog.'",
        "essay structure": "Introduction → Body paragraphs (3) → Conclusion. Each paragraph needs a topic sentence.",
        "comma rules": "Use commas for lists, after introductory words, and to separate independent clauses."
    },
    "history": {
        "world war 2": "1939-1945. Axis (Germany, Japan, Italy) vs Allies. Ended with atomic bombs on Japan.",
        "cold war": "1947-1991. Tension between USA and USSR. No direct fighting, but proxy wars.",
        "industrial revolution": "1760-1840. Shift from farming to factories. Steam engine changed everything.",
        "french revolution": "1789-1799. People overthrew monarchy. Liberty, Equality, Fraternity.",
        "renaissance": "14th-17th century. Rebirth of art and science in Europe. Da Vinci, Michelangelo."
    }
}

# Quiz questions database
QUIZ_QUESTIONS = {
    "math": [
        {"q": "What is the value of π (pi) to 2 decimal places?", "a": "3.14", "options": ["3.14", "3.16", "3.12", "3.18"]},
        {"q": "Solve: 2x + 4 = 10", "a": "3", "options": ["2", "3", "4", "5"]},
        {"q": "What is the square root of 144?", "a": "12", "options": ["10", "11", "12", "14"]},
        {"q": "Area of rectangle = ?", "a": "length × width", "options": ["length + width", "length × width", "2(length + width)", "length²"]},
        {"q": "What is 15% of 200?", "a": "30", "options": ["20", "25", "30", "35"]}
    ],
    "science": [
        {"q": "What is the chemical symbol for water?", "a": "H₂O", "options": ["CO₂", "H₂O", "O₂", "NaCl"]},
        {"q": "How many planets in our solar system?", "a": "8", "options": ["7", "8", "9", "10"]},
        {"q": "What gas do plants absorb?", "a": "Carbon dioxide", "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"]},
        {"q": "What is the speed of light?", "a": "300,000 km/s", "options": ["150,000 km/s", "300,000 km/s", "450,000 km/s", "600,000 km/s"]},
        {"q": "What is the powerhouse of the cell?", "a": "Mitochondria", "options": ["Nucleus", "Mitochondria", "Ribosome", "Golgi body"]}
    ],
    "english": [
        {"q": "What is a noun?", "a": "A person, place, thing, or idea", "options": ["An action word", "A person, place, thing, or idea", "A describing word", "A connecting word"]},
        {"q": "Which is a metaphor?", "a": "Her voice is music to my ears", "options": ["He runs like the wind", "Her voice is music to my ears", "She is as brave as a lion", "The water was as clear as crystal"]},
        {"q": "What is the past tense of 'go'?", "a": "went", "options": ["goed", "went", "gone", "going"]},
        {"q": "How many syllables in 'beautiful'?", "a": "3", "options": ["2", "3", "4", "5"]},
        {"q": "What punctuation ends a question?", "a": "?", "options": [".", "!", "?", ","]}
    ],
    "history": [
        {"q": "Who was the first US President?", "a": "George Washington", "options": ["Thomas Jefferson", "George Washington", "Abraham Lincoln", "John Adams"]},
        {"q": "When did World War 2 end?", "a": "1945", "options": ["1943", "1944", "1945", "1946"]},
        {"q": "Who wrote the Declaration of Independence?", "a": "Thomas Jefferson", "options": ["George Washington", "Thomas Jefferson", "Benjamin Franklin", "John Adams"]},
        {"q": "What ancient wonder still stands today?", "a": "Great Pyramid of Giza", "options": ["Colossus of Rhodes", "Great Pyramid of Giza", "Hanging Gardens", "Lighthouse of Alexandria"]},
        {"q": "The Renaissance began in which country?", "a": "Italy", "options": ["France", "England", "Italy", "Germany"]}
    ]
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    question = data.get('question', '').lower()
    subject = data.get('subject', 'general')
    
    # Search knowledge base
    response = "I'm not sure about that. Try asking your teacher or check your textbook!"
    
    if subject in KNOWLEDGE_BASE:
        for key, value in KNOWLEDGE_BASE[subject].items():
            if key in question or any(word in question for word in key.split()):
                response = value
                break
    
    # Save to progress
    progress = load_data(PROGRESS_FILE, {"questions_asked": 0, "subjects": {}})
    progress["questions_asked"] += 1
    if subject not in progress["subjects"]:
        progress["subjects"][subject] = 0
    progress["subjects"][subject] += 1
    save_data(PROGRESS_FILE, progress)
    
    return jsonify({
        "question": data.get('question'),
        "answer": response,
        "subject": subject,
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/quiz/<subject>', methods=['GET'])
def get_quiz(subject):
    questions = QUIZ_QUESTIONS.get(subject, [])
    if not questions:
        return jsonify({"error": "Subject not found"}), 404
    
    # Get 3 random questions
    selected = random.sample(questions, min(3, len(questions)))
    return jsonify({
        "subject": subject,
        "questions": selected,
        "total": len(questions)
    })

@app.route('/api/quiz/submit', methods=['POST'])
def submit_quiz():
    data = request.get_json()
    answers = data.get('answers', [])
    score = 0
    
    for ans in answers:
        if ans.get('selected') == ans.get('correct'):
            score += 1
    
    # Save to history
    history = load_data(QUIZ_FILE, [])
    history.append({
        "date": datetime.now().isoformat(),
        "score": score,
        "total": len(answers)
    })
    save_data(QUIZ_FILE, history[-10:])  # Keep last 10
    
    return jsonify({
        "score": score,
        "total": len(answers),
        "percentage": round(score/len(answers)*100) if answers else 0
    })

@app.route('/api/notes', methods=['GET', 'POST'])
def notes():
    if request.method == 'GET':
        notes = load_data(NOTES_FILE, [])
        return jsonify({"notes": notes})
    
    data = request.get_json()
    new_note = {
        "id": len(load_data(NOTES_FILE, [])) + 1,
        "title": data.get('title', 'Untitled'),
        "content": data.get('content', ''),
        "subject": data.get('subject', 'general'),
        "created_at": datetime.now().isoformat()
    }
    notes = load_data(NOTES_FILE, [])
    notes.append(new_note)
    save_data(NOTES_FILE, notes)
    
    return jsonify({"note": new_note, "message": "Note saved!"})

@app.route('/api/progress', methods=['GET'])
def get_progress():
    progress = load_data(PROGRESS_FILE, {"questions_asked": 0, "subjects": {}})
    history = load_data(QUIZ_FILE, [])
    
    total_quizzes = len(history)
    avg_score = sum(h['score']/h['total']*100 for h in history)/total_quizzes if total_quizzes else 0
    
    return jsonify({
        "questions_asked": progress.get("questions_asked", 0),
        "subjects_studied": list(progress.get("subjects", {}).keys()),
        "quizzes_taken": total_quizzes,
        "average_score": round(avg_score, 1),
        "study_streak": "3 days"  # Placeholder
    })

@app.route('/api/subjects', methods=['GET'])
def get_subjects():
    return jsonify({
        "subjects": list(KNOWLEDGE_BASE.keys()),
        "description": "Choose a subject to study!"
    })

if __name__ == '__main__':
    print("🎓 AI Study Buddy starting...")
    print("📍 Open http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)

