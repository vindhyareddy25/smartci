
import sys
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: python scripts/summarize_log.py build.log")
    sys.exit(1)

log_file = Path(sys.argv[1])

if not log_file.exists():
    print(f"Error: {log_file} not found.")
    sys.exit(1)

log = log_file.read_text(encoding="utf-8", errors="replace")[-6000:]

prompt = f"""
You are a CI build assistant.

Analyze the following build/error log.

Return:
1. Root cause of the failure.
2. Name of the failing test.
3. Suggested fix.

Use ONLY the information available in this log.
Do not invent errors or file names.

BUILD LOG:
{log}
"""

print("\n========== LLM SUMMARY PROMPT ==========\n")
print(prompt)
