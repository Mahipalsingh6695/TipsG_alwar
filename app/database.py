import sqlite3
import json

def init_db():
    conn = sqlite3.connect("questions.db")
    cursor = conn.cursor()

    # Create questions table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY,
            question TEXT NOT NULL,
            option_a TEXT NOT NULL,
            option_b TEXT NOT NULL,
            option_c TEXT NOT NULL,
            option_d TEXT NOT NULL,
            correct_option TEXT NOT NULL
        )
    """)

    # Load questions from JSON
    with open("data/questions.json", "r") as f:
        questions = json.load(f)

    for question in questions:
        cursor.execute(
            """
            INSERT OR IGNORE INTO questions (id, question, option_a, option_b, option_c, option_d, correct_option)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                question["id"],
                question["question"],
                question["option_a"],
                question["option_b"],
                question["option_c"],
                question["option_d"],
                question["correct_option"]
            )
        )

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized and data loaded.")