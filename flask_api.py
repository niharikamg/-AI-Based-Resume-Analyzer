from flask import Flask, request, jsonify
from resume_scoring import resume_scoring

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze_resume():
    data = request.json
    resume_text = data.get("resume", "")
    job_desc = data.get("job_description", "")

    if not resume_text or not job_desc:
        return jsonify({"error": "Missing resume or job description"}), 400

    score = resume_scoring(resume_text, job_desc)
    return jsonify({"resume_score": score})

if __name__ == "__main__":
    app.run(debug=True)
