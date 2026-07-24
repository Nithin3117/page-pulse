from flask import Flask, render_template, request, jsonify
from parser import analyze_website

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    try:

        data = request.get_json()

        if not data:
            return jsonify({
                "error": "Request body is missing."
            }), 400

        url = data.get("url", "").strip()

        if not url:
            return jsonify({
                "error": "Please enter a website URL."
            }), 400

        result = analyze_website(url)

        return jsonify(result)

    except Exception:
        return jsonify({
            "error": "Internal server error."
        }), 500


if __name__ == "__main__":
    app.run(debug=True)