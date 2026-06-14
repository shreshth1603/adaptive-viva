import requests
import json
from backend.config import OLLAMA_BASE_URL, LLM_MODEL

def extract_topics(text: str) -> list[dict]:
    prompt = f"""You are an academic syllabus analyzer.

Given the following syllabus content, extract a structured list of main topics and their subtopics.

Return ONLY a valid JSON array. No explanation, no markdown, no code blocks. Just the raw JSON array.

Format:
[
  {{
    "name": "Topic Name",
    "subtopics": ["subtopic1", "subtopic2"]
  }}
]

Syllabus content:
{text[:3000]}

Return only the JSON array:"""

    response = requests.post(
        f"{OLLAMA_BASE_URL}/api/generate",
        json={
            "model": LLM_MODEL,
            "prompt": prompt,
            "stream": False,
            "options": {"temperature": 0.1}
        }
    )

    result = response.json()
    raw = result.get("response", "").strip()

    try:
        if "```" in raw:
            raw = raw.split("```")[1]
            if raw.startswith("json"):
                raw = raw[4:]
        topics = json.loads(raw)
        return topics
    except json.JSONDecodeError:
        return [{"name": "General Topics", "subtopics": ["Review syllabus manually"]}]