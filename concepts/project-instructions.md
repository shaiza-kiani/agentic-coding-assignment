# Project instructions
A project instructions file (like AGENTS.md) holds rules for one project.
The agent reads it before working, so I don't repeat the rules in every prompt.
My AGENTS.md rules:
- Follow PEP 8 and add type hints to new functions.
- Test command: python -m pytest -q.
- Don't edit files under tests/ unless the task asks for a new test.
- Don't open any .env file.
Followed: OpenCode added "-> None" and left the old tests alone. Its commit
only touched cart.py, the new test file and AGENTS.md.
Not fully followed: Codex's plan skipped type hints until I reminded it.
Also, the test command failed in Cline's terminal (system Python has no
pytest), so I added the venv Python line to AGENTS.md.
Lesson: rules help, but I still check the diff and run the tests myself.
