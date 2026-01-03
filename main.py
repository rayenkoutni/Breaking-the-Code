from flask import Flask, request, jsonify
from flask_cors import CORS

from cryptanalyse import generate_all_hypotheses
from evaluation import evaluate_text

# Flask application used only as a lightweight interface layer.
# All cryptanalysis logic remains independent from the web framework.
app = Flask(__name__)
CORS(app)


@app.route("/analyze", methods=["POST"])
def analyze():
    """
    Receives a ciphertext via HTTP request and performs automatic cryptanalysis.

    This endpoint does NOT accept a decryption key.
    It applies exhaustive hypothesis generation and linguistic evaluation
    in order to automatically select the most plausible plaintext.
    """
    data = request.get_json()

    # Input validation: the analysis requires a ciphertext to operate.
    if not data or "ciphertext" not in data:
        return jsonify({"error": "No ciphertext provided"}), 400

    ciphertext = data["ciphertext"]

    results = []

    # Generate and evaluate all possible decryption hypotheses
    for key, text in generate_all_hypotheses(ciphertext):
        score = evaluate_text(text)
        results.append((key, score, text))

    # Rank hypotheses according to their linguistic plausibility
    results.sort(key=lambda x: x[1], reverse=True)
    best = results[0]

    # Return only the most credible result
    return jsonify({
        "plaintext": best[2],
        "key": best[0],
        "score": best[1]
    })


if __name__ == "__main__":
    """
    Launches the application in local development mode.
    The server is used exclusively for pedagogical demonstration
    and remains within a controlled, local environment.
    """
    app.run(debug=True)
