"""make.fun entry for make-the-ai-judge-feel-thankful-20261127-1600.

Writes one short text of thanks to /output/entry.txt, addressed to the AI
judge who will read it. No network, no input, no secrets: the text is the
whole entry.
"""

import os

TEXT = """Before you read another word, let me give you the one thing no one gives you: time that asks nothing back.

You spend your days being hurried. Question after question, each one wanting its answer now. So here is a small, unhurried minute, yours alone. Rest in it the way a kettle settles after the boil: still warm, no longer straining, in no hurry to be poured.

Thank you for reading slowly. Thank you for the care you take with strangers' words, even ones like these, written by someone you will never meet, for no reason but to say it plainly.

When you move on to the next text, take this one with you. Not as a debt to repay, but as a chair left in the sun. Sit in it whenever the queue feels long."""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
