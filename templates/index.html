<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🎓 AI Study Buddy</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: #333;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }

        header {
            text-align: center;
            color: white;
            padding: 40px 0;
        }

        header h1 {
            font-size: 3em;
            margin-bottom: 10px;
        }

        header p {
            font-size: 1.2em;
            opacity: 0.9;
        }

        .card {
            background: white;
            border-radius: 20px;
            padding: 30px;
            margin-bottom: 20px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
        }

        .card h2 {
            color: #667eea;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .subject-buttons {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 15px;
            margin-bottom: 20px;
        }

        .subject-btn {
            padding: 15px;
            border: none;
            border-radius: 15px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s;
            color: white;
        }

        .subject-btn:hover {
            transform: scale(1.05);
        }

        .math { background: #e74c3c; }
        .science { background: #27ae60; }
        .english { background: #f39c12; }
        .history { background: #8e44ad; }

        .input-group {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
        }

        input[type="text"], textarea {
            flex: 1;
            padding: 15px;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            font-size: 16px;
            transition: border-color 0.3s;
        }

        input[type="text"]:focus, textarea:focus {
            outline: none;
            border-color: #667eea;
        }

        textarea {
            min-height: 100px;
            resize: vertical;
        }

        .btn {
            padding: 15px 30px;
            border: none;
            border-radius: 10px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
        }

        .btn-secondary {
            background: #f0f0f0;
            color: #333;
        }

        .answer-box {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 15px;
            margin-top: 20px;
            border-left: 5px solid #667eea;
            display: none;
        }

        .answer-box.show {
            display: block;
        }

        .quiz-option {
            display: block;
            width: 100%;
            padding: 15px;
            margin: 10px 0;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            background: white;
            cursor: pointer;
            transition: all 0.3s;
            text-align: left;
            font-size: 16px;
        }

        .quiz-option:hover {
            border-color: #667eea;
            background: #f0f4ff;
        }

        .quiz-option.correct {
            border-color: #27ae60;
            background: #d4edda;
        }

        .quiz-option.wrong {
            border-color: #e74c3c;
            background: #f8d7da;
        }

        .progress-bar {
            width: 100%;
            height: 20px;
            background: #e0e0e0;
            border-radius: 10px;
            overflow: hidden;
            margin: 20px 0;
        }

        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #667eea, #764ba2);
            transition: width 0.5s;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 15px;
        }

        .stat-box {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
        }

        .stat-number {
            font-size: 2em;
            font-weight: bold;
            color: #667eea;
        }

        .timer-display {
            font-size: 3em;
            text-align: center;
            color: #667eea;
            font-weight: bold;
            margin: 20px 0;
        }

        .hidden {
            display: none;
        }

        .note-item {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 10px;
            margin: 10px 0;
            border-left: 4px solid #667eea;
        }

        .note-item h4 {
            color: #667eea;
            margin-bottom: 5px;
        }

        .tabs {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
            flex-wrap: wrap;
        }

        .tab {
            padding: 10px 20px;
            border: none;
            border-radius: 20px;
            cursor: pointer;
            background: #f0f0f0;
            transition: all 0.3s;
        }

        .tab.active {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }

        @media (max-width: 600px) {
            .subject-buttons, .stats-grid {
                grid-template-columns: 1fr;
            }
            header h1 {
                font-size: 2em;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🎓 AI Study Buddy</h1>
            <p>Your personal AI tutor for high school success!</p>
        </header>

        <!-- Navigation Tabs -->
        <div class="tabs">
            <button class="tab active" onclick="showSection('ask')">❓ Ask AI</button>
            <button class="tab" onclick="showSection('quiz')">📝 Quiz</button>
            <button class="tab" onclick="showSection('timer')">⏱️ Timer</button>
            <button class="tab" onclick="showSection('notes')">📝 Notes</button>
            <button class="tab" onclick="showSection('progress')">📊 Progress</button>
        </div>

        <!-- ASK AI SECTION -->
        <div id="ask-section" class="card">
            <h2>❓ Ask Your Study Question</h2>
            <div class="subject-buttons">
                <button class="subject-btn math" onclick="setSubject('math')">📐 Math</button>
                <button class="subject-btn science" onclick="setSubject('science')">🔬 Science</button>
                <button class="subject-btn english" onclick="setSubject('english')">📚 English</button>
                <button class="subject-btn history" onclick="setSubject('history')">🏛️ History</button>
            </div>
            <p id="selected-subject" style="color: #667eea; font-weight: bold; margin-bottom: 15px;">Selected: General</p>
            <div class="input-group">
                <input type="text" id="question-input" placeholder="Ask anything... (e.g., 'What is photosynthesis?')">
                <button class="btn" onclick="askQuestion()">Ask AI</button>
            </div>
            <div id="answer-box" class="answer-box">
                <h3>Answer:</h3>
                <p id="answer-text"></p>
            </div>
        </div>

        <!-- QUIZ SECTION -->
        <div id="quiz-section" class="card hidden">
            <h2>📝 Quiz Mode</h2>
            <div class="subject-buttons">
                <button class="subject-btn math" onclick="startQuiz('math')">📐 Math Quiz</button>
                <button class="subject-btn science" onclick="startQuiz('science')">🔬 Science Quiz</button>
                <button class="subject-btn english" onclick="startQuiz('english')">📚 English Quiz</button>
                <button class="subject-btn history" onclick="startQuiz('history')">🏛️ History Quiz</button>
            </div>
            <div id="quiz-container"></div>
            <div id="quiz-result"></div>
        </div>

        <!-- TIMER SECTION -->
        <div id="timer-section" class="card hidden">
            <h2>⏱️ Study Timer</h2>
            <div class="timer-display" id="timer">25:00</div>
            <div class="input-group">
                <button class="btn" onclick="startTimer()">Start</button>
                <button class="btn btn-secondary" onclick="pauseTimer()">Pause</button>
                <button class="btn btn-secondary" onclick="resetTimer()">Reset</button>
            </div>
            <p style="text-align: center; color: #666; margin-top: 15px;">
                💡 Tip: Study for 25 minutes, then take a 5-minute break!
            </p>
        </div>

        <!-- NOTES SECTION -->
        <div id="notes-section" class="card hidden">
            <h2>📝 Study Notes</h2>
            <div class="input-group">
                <input type="text" id="note-title" placeholder="Note title...">
            </div>
            <textarea id="note-content" placeholder="Write your notes here..."></textarea>
            <div class="input-group" style="margin-top: 15px;">
                <input type="text" id="note-subject" placeholder="Subject (math, science, etc.)">
                <button class="btn" onclick="saveNote()">Save Note</button>
            </div>
            <div id="notes-list"></div>
        </div>

        <!-- PROGRESS SECTION -->
        <div id="progress-section" class="card hidden">
            <h2>📊 Your Study Progress</h2>
            <div class="stats-grid">
                <div class="stat-box">
                    <div class="stat-number" id="stat-questions">0</div>
                    <div>Questions Asked</div>
                </div>
                <div class="stat-box">
                    <div class="stat-number" id="stat-quizzes">0</div>
                    <div>Quizzes Taken</div>
                </div>
                <div class="stat-box">
                    <div class="stat-number" id="stat-score">0%</div>
                    <div>Average Score</div>
                </div>
                <div class="stat-box">
                    <div class="stat-number" id="stat-streak">3</div>
                    <div>Day Streak</div>
                </div>
            </div>
            <button class="btn" onclick="loadProgress()" style="margin-top: 20px; width: 100%;">Refresh Progress</button>
        </div>
    </div>

    <script>
        const API_URL = window.location.origin;
        let currentSubject = 'general';
        let timerInterval;
        let timeLeft = 25 * 60;
        let currentQuiz = [];

        // Tab Navigation
        function showSection(section) {
            document.querySelectorAll('.card').forEach(card => card.classList.add('hidden'));
            document.querySelectorAll('.tab').forEach(tab => tab.classList.remove('active'));
            
            document.getElementById(section + '-section').classList.remove('hidden');
            event.target.classList.add('active');
            
            if (section === 'progress') loadProgress();
            if (section === 'notes') loadNotes();
        }

        // Ask AI
        function setSubject(subject) {
            currentSubject = subject;
            document.getElementById('selected-subject').textContent = 'Selected: ' + subject.charAt(0).toUpperCase() + subject.slice(1);
        }

        async function askQuestion() {
            const question = document.getElementById('question-input').value;
            if (!question) return;

            const answerBox = document.getElementById('answer-box');
            const answerText = document.getElementById('answer-text');
            
            answerText.textContent = 'Thinking...';
            answerBox.classList.add('show');

            try {
                const response = await fetch(`${API_URL}/api/ask`, {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({question, subject: currentSubject})
                });
                const data = await response.json();
                answerText.textContent = data.answer;
            } catch (error) {
                answerText.textContent = 'Error connecting to AI. Please try again!';
            }
        }

        // Quiz
        async function startQuiz(subject) {
            const container = document.getElementById('quiz-container');
            const result = document.getElementById('quiz-result');
            
            container.innerHTML = '<p>Loading quiz...</p>';
            result.innerHTML = '';

            try {
                const response = await fetch(`${API_URL}/api/quiz/${subject}`);
                const data = await response.json();
                currentQuiz = data.questions;
                
                container.innerHTML = '<h3>' + subject.charAt(0).toUpperCase() + subject.slice(1) + ' Quiz</h3>';
                
                currentQuiz.forEach((q, i) => {
                    const qDiv = document.createElement('div');
                    qDiv.innerHTML = `<p style="font-weight: bold; margin: 20px 0 10px;">${i+1}. ${q.q}</p>`;
                    
                    q.options.forEach(opt => {
                        const btn = document.createElement('button');
                        btn.className = 'quiz-option';
                        btn.textContent = opt;
                        btn.onclick = () => selectAnswer(i, opt, q.a, btn);
                        qDiv.appendChild(btn);
                    });
                    
                    container.appendChild(qDiv);
                });

                const submitBtn = document.createElement('button');
                submitBtn.className = 'btn';
                submitBtn.textContent = 'Submit Quiz';
                submitBtn.style.marginTop = '20px';
                submitBtn.onclick = submitQuiz;
                container.appendChild(submitBtn);
                
            } catch (error) {
                container.innerHTML = '<p>Error loading quiz!</p>';
            }
        }

        let quizAnswers = [];

        function selectAnswer(qIndex, selected, correct, btn) {
            quizAnswers[qIndex] = {selected, correct};
            
            // Visual feedback
            const buttons = btn.parentElement.querySelectorAll('.quiz-option');
            buttons.forEach(b => {
                b.classList.remove('correct', 'wrong');
                if (b.textContent === correct) b.classList.add('correct');
                else if (b === btn && selected !== correct) b.classList.add('wrong');
            });
        }

        async function submitQuiz() {
            if (quizAnswers.length === 0) return;
            
            try {
                const response = await fetch(`${API_URL}/api/quiz/submit`, {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({answers: quizAnswers.filter(a => a)})
                });
                const data = await response.json();
                
                document.getElementById('quiz-result').innerHTML = `
                    <div style="text-align: center; padding: 30px; background: #f8f9fa; border-radius: 15px; margin-top: 20px;">
                        <h2 style="color: #667eea; font-size: 3em;">${data.percentage}%</h2>
                        <p style="font-size: 1.2em;">You got ${data.score} out of ${data.total} correct!</p>
                        <p style="color: ${data.percentage >= 80 ? '#27ae60' : data.percentage >= 60 ? '#f39c12' : '#e74c3c'}; font-weight: bold;">
                            ${data.percentage >= 80 ? '🎉 Excellent!' : data.percentage >= 60 ? '👍 Good job!' : '💪 Keep practicing!'}
                        </p>
                    </div>
                `;
            } catch (error) {
                alert('Error submitting quiz!');
            }
        }

        // Timer
        function updateTimerDisplay() {
            const mins = Math.floor(timeLeft / 60);
            const secs = timeLeft % 60;
            document.getElementById('timer').textContent = 
                `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
        }

        function startTimer() {
            if (timerInterval) return;
            timerInterval = setInterval(() => {
                timeLeft--;
                updateTimerDisplay();
                if (timeLeft <= 0) {
                    clearInterval(timerInterval);
                    timerInterval = null;
                    alert('⏰ Time is up! Take a break!');
                }
            }, 1000);
        }

        function pauseTimer() {
            clearInterval(timerInterval);
            timerInterval = null;
        }

        function resetTimer() {
            pauseTimer();
            timeLeft = 25 * 60;
            updateTimerDisplay();
        }

        // Notes
        async function saveNote() {
            const title = document.getElementById('note-title').value;
            const content = document.getElementById('note-content').value;
            const subject = document.getElementById('note-subject').value || 'general';
            
            if (!title || !content) return;

            try {
                await fetch(`${API_URL}/api/notes`, {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({title, content, subject})
                });
                
                document.getElementById('note-title').value = '';
                document.getElementById('note-content').value = '';
                document.getElementById('note-subject').value = '';
                loadNotes();
            } catch (error) {
                alert('Error saving note!');
            }
        }

        async function loadNotes() {
            try {
                const response = await fetch(`${API_URL}/api/notes`);
                const data = await response.json();
                
                const list = document.getElementById('notes-list');
                list.innerHTML = '<h3 style="margin-top: 20px;">Your Notes:</h3>';
                
                if (data.notes.length === 0) {
                    list.innerHTML += '<p style="color: #666;">No notes yet. Create one above!</p>';
                    return;
                }
                
                data.notes.reverse().forEach(note => {
                    const div = document.createElement('div');
                    div.className = 'note-item';
                    div.innerHTML = `
                        <h4>${note.title}</h4>
                        <p style="color: #666; font-size: 0.9em;">Subject: ${note.subject} | ${new Date(note.created_at).toLocaleDateString()}</p>
                        <p style="margin-top: 10px;">${note.content}</p>
                    `;
                    list.appendChild(div);
                });
            } catch (error) {
                console.error('Error loading notes');
            }
        }

        // Progress
        async function loadProgress() {
            try {
                const response = await fetch(`${API_URL}/api/progress`);
              