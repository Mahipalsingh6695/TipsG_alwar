from flask import Flask, request, jsonify
from app.database import fetch_questions
from app.test_utils import save_results

app = Flask(__name__)

@app.route("/api/questions", methods=["GET"])
def get_questions():
    questions = fetch_questions()
    return jsonify(questions)

@app.route("/api/submit", methods=["POST"])
def submit_test():
    data = request.json
    username = data.get("username")
    answers = data.get("answers")

    # Mock scoring logic
    score = sum(1 for k, v in answers.items() if v == "c")  # Replace with real scoring
    total_questions = len(answers)

    save_results(username, answers, score, total_questions)
    return jsonify({"message": "Results saved."})