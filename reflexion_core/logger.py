import datetime
from pathlib import Path

class MarkdownLogger:
    def __init__(self, log_file_path: str = "reflexion_logs.md"):
        self.log_path = Path(log_file_path)
        if not self.log_path.exists():
            with open(self.log_path, 'w', encoding='utf-8') as f:
                f.write("# 🧠 Agent Reflexion Memory Logs\n\n")
                f.write("This file logs all the rules the agent has learned over time.\n\n---\n")

    def log_rule(self, task: str, failure: str, rule: str):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_path, 'a', encoding='utf-8') as f:
            f.write(f"### 📅 {timestamp}\n")
            f.write(f"**Task Attempted:** {task}\n\n")
            f.write(f"**Failure Reason:** {failure}\n\n")
            f.write(f"**✅ Distilled Rule Learned:**\n> {rule}\n\n---\n")