import os
from datetime import datetime

# === USER CONFIGURATION ===
REPO_PATH = "/Users/mohit/Hackerrank-solutions"  # <-- Change this
GIT_COMMITTER_NAME = "Mohit-jpg-dot"
GIT_COMMITTER_EMAIL = "mohit1268.becse24@chitkara.edu.in"

# === INPUT FROM USER ===
problem_title = input("Enter problem title: ").strip()
language = input("Language (Python/C++/Java): ").strip()
print("Paste your solution code (end with 'EOF' on a new line):")

# Read multiline input
code_lines = []
while True:
    line = input()
    if line.strip() == "EOF":
        break
    code_lines.append(line)
code = "\n".join(code_lines)

# === FILE EXTENSION MAP ===
ext_map = {"Python": "py", "C++": "cpp", "Java": "java"}
file_ext = ext_map.get(language, "txt")

# === FOLDER AND FILE SETUP ===
lang_folder = os.path.join(REPO_PATH, language)
os.makedirs(lang_folder, exist_ok=True)

filename = f"{problem_title.replace(' ', '_')}.{file_ext}"
file_path = os.path.join(lang_folder, filename)

# === SAVE FILE ===
with open(file_path, "w", encoding="utf-8") as f:
    f.write(f"# Problem: {problem_title}\n")
    f.write(f"# Date: {datetime.now().strftime('%Y-%m-%d')}\n\n")
    f.write(code)

# === COMMIT TO GITHUB ===
os.chdir(REPO_PATH)
os.system("git add .")
os.system(f'git commit -m "Added solution: {problem_title}"')
os.system("git push")
