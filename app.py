from flask import Flask, render_template, request, redirect, url_for, session
from graphs import TutorBotGraph

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Required for session handling

tutor_bot = TutorBotGraph()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        topic = request.form.get("topic", "").strip()

        if not topic:
            return redirect(url_for("index"))  # Ensure a topic is entered

        session["topic"] = topic  # Store topic in session
        results = tutor_bot.run(topic)

        # Store initial results in session
        session["subtopics"] = results.get("subtopics", {})
        session["flashcards"] = results.get("flashcards", {})
        session["resources"] = results.get("resources", {})

        return redirect(url_for("review"))

    # ✅ Check if review is available
    review_ready = "subtopics" in session and session["subtopics"]
    return render_template("index.html", review_ready=review_ready)

@app.route("/review", methods=["GET", "POST"])
def review():
    if "topic" not in session or "subtopics" not in session:
        return redirect(url_for("index"))

    if request.method == "POST":
        edited_subtopics = {
            key.replace("subtopic_", ""): value if value.strip() else session["subtopics"][key.replace("subtopic_", "")]
            for key, value in request.form.items() if key.startswith("subtopic_")
        }
        session["subtopics"] = edited_subtopics  # Store reviewed subtopics

        return redirect(url_for("results"))

    return render_template("review.html", subtopics=session.get("subtopics", {}))

@app.route("/results")
def results():
    if "topic" not in session or "subtopics" not in session:
        return redirect(url_for("index"))

    return render_template(
        "results.html",
        topic=session.get("topic", "Unknown Topic"),
        subtopics=session.get("subtopics", {}),
        flashcards=session.get("flashcards", {}),
        resources=session.get("resources", []),
    )

if __name__ == "__main__":
    app.run(debug=True)
