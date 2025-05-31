import os

# A simple map of file extensions to languages
EXTENSION_TO_LANGUAGE = {
    ".py": "Python",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".java": "Java",
    ".cpp": "C++",
    ".c": "C",
    ".cs": "C#",
    ".html": "HTML",
    ".css": "CSS",
    ".rb": "Ruby",
    ".go": "Go",
    ".rs": "Rust",
    ".php": "PHP",
    ".sh": "Shell",
    ".json": "JSON",
    ".yml": "YAML",
    ".yaml": "YAML",
    ".md": "Markdown",
}

def detect_languages(repo_path):
    language_count = {}

    for root, dirs, files in os.walk(repo_path):
        for file in files:
            _, ext = os.path.splitext(file)
            language = EXTENSION_TO_LANGUAGE.get(ext.lower())
            if language:
                language_count[language] = language_count.get(language, 0) + 1

    return language_count
