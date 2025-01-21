import json
from datetime import datetime
from app.models import MongoDB

def save_results(username, answers, score, total_questions):
    result_data = {
        "username": username,
        "score": score,
        "total_questions": total_questions,
        "answers": answers,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Save to MongoDB
    MongoDB.save_result(result_data)

    # Save to local JSON files
    with open("results/full_results.json", "r") as f:
        all_results = json.load(f)

    all_results.append(result_data)

    with open("results/full_results.json", "w") as f:
        json.dump(all_results, f, indent=4)

    sorted_results = sorted(all_results, key=lambda x: x["score"], reverse=True)
    with open("results/sorted_results.json", "w") as f:
        json.dump(sorted_results, f, indent=4)