CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS syllabi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    filename TEXT NOT NULL,
    upload_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    topic_count INTEGER DEFAULT 0,
    chroma_collection_id TEXT,
    FOREIGN KEY (student_id) REFERENCES students(id)
);

CREATE TABLE IF NOT EXISTS topics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    syllabus_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    parent_topic_id INTEGER,
    coverage_weight REAL DEFAULT 1.0,
    questions_asked INTEGER DEFAULT 0,
    FOREIGN KEY (syllabus_id) REFERENCES syllabi(id),
    FOREIGN KEY (parent_topic_id) REFERENCES topics(id)
);

CREATE TABLE IF NOT EXISTS viva_sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    syllabus_id INTEGER NOT NULL,
    started_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    ended_at DATETIME,
    status TEXT DEFAULT 'active',
    current_difficulty INTEGER DEFAULT 2,
    total_questions INTEGER DEFAULT 0,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (syllabus_id) REFERENCES syllabi(id)
);

CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER NOT NULL,
    topic_id INTEGER NOT NULL,
    question_text TEXT NOT NULL,
    difficulty_tier INTEGER NOT NULL,
    expected_hints TEXT,
    asked_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    is_follow_up BOOLEAN DEFAULT 0,
    FOREIGN KEY (session_id) REFERENCES viva_sessions(id),
    FOREIGN KEY (topic_id) REFERENCES topics(id)
);

CREATE TABLE IF NOT EXISTS responses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_id INTEGER NOT NULL,
    response_text TEXT NOT NULL,
    submitted_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (question_id) REFERENCES questions(id)
);

CREATE TABLE IF NOT EXISTS scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    response_id INTEGER NOT NULL,
    correctness REAL DEFAULT 0,
    conceptual_depth REAL DEFAULT 0,
    clarity REAL DEFAULT 0,
    completeness REAL DEFAULT 0,
    overall REAL DEFAULT 0,
    brief_feedback TEXT,
    detected_gaps TEXT,
    FOREIGN KEY (response_id) REFERENCES responses(id)
);

CREATE TABLE IF NOT EXISTS reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER NOT NULL,
    generated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    overall_grade TEXT,
    overall_score REAL,
    narrative TEXT,
    study_recommendations TEXT,
    coverage_data TEXT,
    FOREIGN KEY (session_id) REFERENCES viva_sessions(id)
);