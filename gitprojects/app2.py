from flask import Flask, request, jsonify

app = Flask(__name__)

# Temporary storage (list)
reviews = []
@app.route("/")
def home():
    return "Flask API is running"

# 🔹 POST: Add review
@app.route('/review', methods=['POST'])
def add_review():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    review = data.get("review")
    rating = data.get("rating")
    if not review or not rating:
        return jsonify({"error": "Review and rating are required"}), 400

    reviews.append({
        "review": review,
        "rating": rating
    })

    return jsonify({"message": "Review added"}), 201

# 🔹 GET: Get all reviews
@app.route('/review', methods=['GET'])
def get_reviews():
    return jsonify(reviews)

if __name__ == '__main__':
    app.run(debug=True,port=5001)