# loan_app.py

import numpy as np
import pandas as pd
from flask import Flask, request, render_template_string
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# -----------------------------
# 1. Create realistic dataset
# -----------------------------
np.random.seed(42)

data_size = 5000

data = pd.DataFrame({
    "income": np.random.randint(20000, 150000, data_size),
    "credit_score": np.random.randint(300, 850, data_size),
    "loan_amount": np.random.randint(5000, 50000, data_size),
    "employment_status": np.random.randint(0, 2, data_size),  # 0 = Unemployed, 1 = Employed
    "existing_loans": np.random.randint(0, 5, data_size),
})

# Approval logic (simple & realistic)
data["approved"] = (
    (data["income"] > 50000) &
    (data["credit_score"] > 650) &
    (data["loan_amount"] < data["income"] * 0.5)
).astype(int)

# -----------------------------
# 2. Train Logistic Regression
# -----------------------------
X = data.drop("approved", axis=1)
y = data["approved"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression()
model.fit(X_train, y_train)

# -----------------------------
# 3. Flask App
# -----------------------------
app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Loan Approval Prediction</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(to right, #667eea, #764ba2);
            color: #333;
        }
        .container {
            width: 420px;
            background: white;
            margin: 60px auto;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0px 10px 30px rgba(0,0,0,0.2);
        }
        h2 {
            text-align: center;
            color: #444;
        }
        input, select {
            width: 100%;
            padding: 10px;
            margin: 8px 0;
            border-radius: 5px;
            border: 1px solid #ccc;
        }
        button {
            width: 100%;
            padding: 12px;
            background: #667eea;
            border: none;
            color: white;
            font-size: 16px;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background: #5a67d8;
        }
        .result {
            text-align: center;
            margin-top: 20px;
            font-size: 18px;
            font-weight: bold;
        }
        .approved {
            color: green;
        }
        .rejected {
            color: red;
        }
    </style>
</head>

<body>
<div class="container">
    <h2>🏦 Loan Approval Prediction</h2>

    <form method="post">
        <input type="number" name="income" placeholder="Annual Income" required>
        <input type="number" name="credit_score" placeholder="Credit Score" required>
        <input type="number" name="loan_amount" placeholder="Loan Amount" required>

        <select name="employment_status">
            <option value="1">Employed</option>
            <option value="0">Unemployed</option>
        </select>

        <input type="number" name="existing_loans" placeholder="Existing Loans Count" required>

        <button type="submit">Predict</button>
    </form>

    {% if result %}
        <div class="result {{ color }}">
            {{ result }}
        </div>
    {% endif %}
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def predict():
    result = None
    color = ""

    if request.method == "POST":
        features = [
            int(request.form["income"]),
            int(request.form["credit_score"]),
            int(request.form["loan_amount"]),
            int(request.form["employment_status"]),
            int(request.form["existing_loans"])
        ]

        prediction = model.predict([features])[0]

        if prediction == 1:
            result = "✅ Loan Approved"
            color = "approved"
        else:
            result = "❌ Loan Rejected"
            color = "rejected"

    return render_template_string(HTML_TEMPLATE, result=result, color=color)

# -----------------------------
# 4. Run App
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)


