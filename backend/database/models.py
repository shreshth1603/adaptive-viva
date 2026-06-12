from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=func.now())

class Syllabus(Base):
    __tablename__ = "syllabi"
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    filename = Column(String, nullable=False)
    upload_time = Column(DateTime, default=func.now())
    topic_count = Column(Integer, default=0)
    chroma_collection_id = Column(String)

class Topic(Base):
    __tablename__ = "topics"
    id = Column(Integer, primary_key=True, autoincrement=True)
    syllabus_id = Column(Integer, ForeignKey("syllabi.id"), nullable=False)
    name = Column(String, nullable=False)
    parent_topic_id = Column(Integer, ForeignKey("topics.id"), nullable=True)
    coverage_weight = Column(Float, default=1.0)
    questions_asked = Column(Integer, default=0)

class VivaSession(Base):
    __tablename__ = "viva_sessions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    syllabus_id = Column(Integer, ForeignKey("syllabi.id"), nullable=False)
    started_at = Column(DateTime, default=func.now())
    ended_at = Column(DateTime, nullable=True)
    status = Column(String, default="active")
    current_difficulty = Column(Integer, default=2)
    total_questions = Column(Integer, default=0)

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(Integer, ForeignKey("viva_sessions.id"), nullable=False)
    topic_id = Column(Integer, ForeignKey("topics.id"), nullable=False)
    question_text = Column(Text, nullable=False)
    difficulty_tier = Column(Integer, nullable=False)
    expected_hints = Column(Text)
    asked_at = Column(DateTime, default=func.now())
    is_follow_up = Column(Boolean, default=False)

class Response(Base):
    __tablename__ = "responses"
    id = Column(Integer, primary_key=True, autoincrement=True)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)
    response_text = Column(Text, nullable=False)
    submitted_at = Column(DateTime, default=func.now())

class Score(Base):
    __tablename__ = "scores"
    id = Column(Integer, primary_key=True, autoincrement=True)
    response_id = Column(Integer, ForeignKey("responses.id"), nullable=False)
    correctness = Column(Float, default=0)
    conceptual_depth = Column(Float, default=0)
    clarity = Column(Float, default=0)
    completeness = Column(Float, default=0)
    overall = Column(Float, default=0)
    brief_feedback = Column(Text)
    detected_gaps = Column(Text)

class Report(Base):
    __tablename__ = "reports"
    id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(Integer, ForeignKey("viva_sessions.id"), nullable=False)
    generated_at = Column(DateTime, default=func.now())
    overall_grade = Column(String)
    overall_score = Column(Float)
    narrative = Column(Text)
    study_recommendations = Column(Text)
    coverage_data = Column(Text)