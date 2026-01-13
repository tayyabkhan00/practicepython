# ==========================================
# Spam Detection Web App using Flask
# Kaggle Dataset + Logistic Regression
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt

from flask import Flask, request, render_template_string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# ----------------------------------
# 1. Load & Clean Kaggle Dataset
# ----------------------------------
df = pd.read_csv("/Users/tayyabkhan/python/spam_copy.csv", encoding="latin-1")

# Keep only required columns
df = df[["v1", "v2"]]
df.columns = ["label", "message"]

# Convert labels to numbers
df["label"] = df["label"].map({"ham": 0, "spam": 1})

print("Dataset loaded:", df.shape)


# ----------------------------------
# 2. Train-Test Split
# ----------------------------------
X = df["message"]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# ----------------------------------
# 3. TF-IDF Vectorization
# ----------------------------------
vectorizer = TfidfVectorizer(stop_words="english")
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)


# ----------------------------------
# 4. Train Logistic Regression
# ----------------------------------
model = LogisticRegression()
model.fit(X_train_vec, y_train)


# ----------------------------------
# 5. Evaluate Model
# ----------------------------------
y_pred = model.predict(X_test_vec)
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", round(accuracy * 100, 2), "%")


# ----------------------------------
# 6. Flask Web App
# ----------------------------------
app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Spam Detection App</title>

    <!-- Bootstrap CDN -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">

</head>
<body class="bg-light">

    <div class="container mt-5">
        <div class="row justify-content-center">
            <div class="col-md-6">

                <div class="card shadow-lg rounded-4">
                    <div class="card-body p-4">

                        <h3 class="text-center mb-4">📩 Spam Detection System</h3>

                        <form method="POST">
                            <div class="mb-3">
                                <label class="form-label">Enter Message</label>
                                <textarea 
                                    class="form-control" 
                                    name="message" 
                                    rows="4"
                                    placeholder="Type your message here..."
                                    required></textarea>
                            </div>

                            <button type="submit" class="btn btn-primary w-100">
                                Check Message
                            </button>
                        </form>

                        {% if result %}
                            <div class="alert mt-4 
                                {% if 'SPAM' in result %}alert-danger{% else %}alert-success{% endif %}">
                                <strong>{{ result }}</strong>
                            </div>
                        {% endif %}

                    </div>
                </div>

                <p class="text-center text-muted mt-3">
                    Logistic Regression + TF-IDF | Kaggle Dataset
                </p>

            </div>
        </div>
    </div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        msg = request.form["message"]
        msg_vec = vectorizer.transform([msg])
        prediction = model.predict(msg_vec)

        if prediction[0] == 1:
            result = "🚨 SPAM MESSAGE"
        else:
            result = "✅ NOT SPAM"

    return render_template_string(HTML_PAGE, result=result)


# ----------------------------------
# 7. Run Flask App
# ----------------------------------
if __name__ == "__main__":
    app.run(debug=True)
